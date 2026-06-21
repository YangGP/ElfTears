# Rollback-safe phone state and the public story API.

default phone_enabled = True
default phone_hidden = False
default phone_unlocked_contacts = ["x", "k"]
default phone_thread_messages = {
    "x": ["x_001", "x_002", "x_003", "x_004"],
    "k": ["k_001"],
}
default phone_unread_counts = {"x": 4, "k": 1}
default phone_reply_offers = {
    "x": ["reply_home_safe", "reply_park_photo", "reply_voice_ok", "reply_sticker_smile"],
}
default phone_story_flags = set()
default phone_current_app = "home"
default phone_current_thread = None
default phone_media_filter = None
default phone_image_preview = None
default phone_voice_playing = None
default phone_saved_quick_menu = True
default phone_chat_scroll_request = 0
default phone_chat_scroll_handled = -1

init -10 python:
    renpy.music.register_channel("phone_voice", mixer="sfx", loop=False)

init -5 python:
    import datetime as _phone_datetime

    def phone_local_time():
        return _phone_datetime.datetime.now().strftime("%H:%M")

    def phone_local_date():
        now = _phone_datetime.datetime.now()
        weekdays = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
        return "{}月{}日  {}".format(now.month, now.day, weekdays[now.weekday()])

    _phone_chat_yadjustment = ui.adjustment()

    def phone_scroll_chat_to_bottom():
        _phone_chat_yadjustment.change(_phone_chat_yadjustment.range)

    def phone_request_chat_scroll():
        global phone_chat_scroll_request
        phone_chat_scroll_request += 1

    def phone_toggle_media_filter(filter_id):
        global phone_media_filter
        phone_media_filter = None if phone_media_filter == filter_id else filter_id
        phone_request_chat_scroll()
        renpy.restart_interaction()

    def phone_unlock_contact(contact_id):
        global phone_unlocked_contacts
        if contact_id not in phone_contacts:
            renpy.log("Phone: unknown contact id {!r}".format(contact_id))
            return False
        if contact_id not in phone_unlocked_contacts:
            phone_unlocked_contacts = list(phone_unlocked_contacts) + [contact_id]
        return True

    def phone_push(thread_id, message_id, unread=True):
        global phone_thread_messages, phone_unread_counts
        if thread_id not in phone_contacts or message_id not in phone_message_catalog:
            renpy.log("Phone: invalid message {!r} for thread {!r}".format(message_id, thread_id))
            return False

        phone_unlock_contact(thread_id)
        updated_threads = dict(phone_thread_messages)
        messages = list(updated_threads.get(thread_id, []))
        if message_id not in messages:
            messages.append(message_id)
            updated_threads[thread_id] = messages
            phone_thread_messages = updated_threads
            if phone_current_app == "thread" and phone_current_thread == thread_id:
                phone_request_chat_scroll()

            if unread and not (phone_current_app == "thread" and phone_current_thread == thread_id and renpy.get_screen("phone_shell")):
                updated_unread = dict(phone_unread_counts)
                updated_unread[thread_id] = updated_unread.get(thread_id, 0) + 1
                phone_unread_counts = updated_unread
        return True

    def phone_offer_reply(thread_id, reply_id):
        global phone_reply_offers
        reply = phone_reply_catalog.get(reply_id)
        if reply is None or reply.get("thread") != thread_id:
            renpy.log("Phone: invalid reply {!r} for thread {!r}".format(reply_id, thread_id))
            return False
        updated = dict(phone_reply_offers)
        offers = list(updated.get(thread_id, []))
        if reply_id not in offers:
            offers.append(reply_id)
            updated[thread_id] = offers
            phone_reply_offers = updated
        return True

    def phone_clear_replies(thread_id):
        global phone_reply_offers
        updated = dict(phone_reply_offers)
        updated[thread_id] = []
        phone_reply_offers = updated

    def phone_has_flag(flag_id):
        return flag_id in phone_story_flags

    def phone_send_reply(thread_id, reply_id):
        global phone_reply_offers, phone_story_flags
        reply = phone_reply_catalog.get(reply_id)
        offers = list(phone_reply_offers.get(thread_id, []))
        if reply is None or reply_id not in offers or reply.get("thread") != thread_id:
            return

        phone_push(thread_id, reply["message"], unread=False)
        offers.remove(reply_id)
        updated = dict(phone_reply_offers)
        updated[thread_id] = offers
        phone_reply_offers = updated

        flags = set(phone_story_flags)
        if reply.get("flag"):
            flags.add(reply["flag"])
        phone_story_flags = flags
        renpy.restart_interaction()
        # Screen Actions must return None or they can end an underlying interaction.
        return

    def phone_mark_read(thread_id):
        global phone_unread_counts
        updated = dict(phone_unread_counts)
        updated[thread_id] = 0
        phone_unread_counts = updated

    def phone_open_thread(thread_id):
        global phone_current_app, phone_current_thread, phone_media_filter
        if thread_id not in phone_contacts:
            return
        phone_current_thread = thread_id
        phone_current_app = "thread"
        phone_media_filter = None
        phone_mark_read(thread_id)
        phone_request_chat_scroll()
        renpy.restart_interaction()

    def phone_last_message(thread_id):
        ids = phone_thread_messages.get(thread_id, [])
        if not ids:
            return "暂无消息"
        message = phone_get_message(ids[-1])
        message_type = message.get("type")
        if message_type == "text":
            return message.get("content", "")
        return {
            "image": "图片消息",
            "voice": "语音消息",
            "sticker": "表情消息",
            "system": "系统消息",
        }.get(message_type, "新消息")

    def phone_available_replies(thread_id, media_filter=None):
        result = []
        for reply_id in phone_reply_offers.get(thread_id, []):
            reply = phone_reply_catalog.get(reply_id)
            if reply and (media_filter is None or reply.get("type") == media_filter):
                result.append(reply_id)
        return result

    def phone_total_unread():
        return sum(phone_unread_counts.get(contact_id, 0) for contact_id in phone_unlocked_contacts)

    def phone_begin():
        global phone_current_app, phone_current_thread, phone_media_filter
        global phone_image_preview, phone_saved_quick_menu, quick_menu
        phone_current_app = "home"
        phone_current_thread = None
        phone_media_filter = None
        phone_image_preview = None
        phone_saved_quick_menu = quick_menu
        quick_menu = False

    def phone_close():
        global phone_image_preview, phone_voice_playing, quick_menu
        renpy.music.stop(channel="phone_voice")
        phone_image_preview = None
        phone_voice_playing = None
        quick_menu = phone_saved_quick_menu

    def phone_back():
        global phone_current_app, phone_current_thread, phone_media_filter, phone_image_preview
        if phone_image_preview:
            phone_image_preview = None
        elif phone_current_app == "thread":
            phone_current_app = "messages"
            phone_current_thread = None
            phone_media_filter = None
        elif phone_current_app in ("contacts", "messages"):
            phone_current_app = "home"
        else:
            phone_close()
            renpy.hide_screen("phone_shell")
        renpy.restart_interaction()

    def phone_toggle_voice(message_id, audio_file):
        global phone_voice_playing
        if phone_voice_playing == message_id:
            renpy.music.stop(channel="phone_voice")
            phone_voice_playing = None
        else:
            renpy.music.play(audio_file, channel="phone_voice", loop=False)
            phone_voice_playing = message_id
        renpy.restart_interaction()


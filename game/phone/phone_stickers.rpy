# Sticker packs are discovered from game/images/ui/phone/stickers/<pack_id>/.

define phone_sticker_root = "images/ui/phone/stickers/"
define phone_sticker_pack_labels = {
    "custom_01": "自制 1",
    "custom_02": "自制 2",
}

default phone_sticker_pack = None

init -5 python:
    _phone_sticker_pack_cache = None

    def phone_get_sticker_packs():
        global _phone_sticker_pack_cache
        if _phone_sticker_pack_cache is not None:
            return _phone_sticker_pack_cache

        grouped = {}
        valid_extensions = (".png", ".jpg", ".jpeg", ".webp")
        for raw_path in renpy.list_files():
            path = raw_path.replace("\\", "/")
            if not path.startswith(phone_sticker_root) or not path.lower().endswith(valid_extensions):
                continue
            relative = path[len(phone_sticker_root):]
            parts = relative.split("/", 1)
            if len(parts) != 2 or not parts[0] or not parts[1]:
                continue
            grouped.setdefault(parts[0], []).append(path)

        packs = []
        for pack_id in sorted(grouped):
            files = sorted(grouped[pack_id])
            packs.append({
                "id": pack_id,
                "label": phone_sticker_pack_labels.get(pack_id, pack_id.replace("_", " ")),
                "icon": files[0],
                "stickers": files,
            })
        _phone_sticker_pack_cache = packs
        return packs

    def phone_active_sticker_pack():
        packs = phone_get_sticker_packs()
        if not packs:
            return None
        valid_ids = [pack["id"] for pack in packs]
        if phone_sticker_pack in valid_ids:
            return phone_sticker_pack
        return valid_ids[0]

    def phone_get_message(message_id):
        message = phone_message_catalog.get(message_id)
        if message is not None:
            return message
        if isinstance(message_id, str) and message_id.startswith("sticker:"):
            sticker_file = message_id[len("sticker:"):]
            for pack in phone_get_sticker_packs():
                if sticker_file in pack["stickers"]:
                    return {
                        "sender": "player",
                        "type": "sticker",
                        "file": sticker_file,
                        "alt": sticker_file.rsplit("/", 1)[-1].rsplit(".", 1)[0],
                        "time": "",
                    }
        return {}

    def phone_send_sticker(thread_id, sticker_file):
        global phone_thread_messages, phone_story_flags
        message_id = "sticker:" + sticker_file
        if thread_id not in phone_contacts or not phone_get_message(message_id):
            return

        updated = dict(phone_thread_messages)
        messages = list(updated.get(thread_id, []))
        messages.append(message_id)
        updated[thread_id] = messages
        phone_thread_messages = updated
        phone_request_chat_scroll()

        flags = set(phone_story_flags)
        flags.add("sent_phone_sticker")
        phone_story_flags = flags
        renpy.restart_interaction()
        return


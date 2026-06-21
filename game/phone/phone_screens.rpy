init -4 python:
    if "phone_launcher" not in config.overlay_screens:
        config.overlay_screens.append("phone_launcher")


screen phone_launcher():
    zorder 95

    if (phone_enabled and not phone_hidden and not main_menu and quick_menu
            and not renpy.get_screen("phone_shell")
            and not renpy.get_screen("choice")
            and not renpy.get_screen("input")):
        fixed:
            xpos 1818
            ypos 30
            xsize 80
            ysize 82
            xanchor 1.0

            button:
                style "phone_launcher_button"
                at phone_launcher_idle
                action [Function(phone_begin), Show("phone_shell")]
                tooltip _("打开手机")

                add Transform("images/ui/phone/icons/device-mobile.svg", size=(38, 38)):
                    xalign 0.5
                    yalign 0.5

            if phone_total_unread() > 0:
                frame:
                    xpos 50
                    ypos -7
                    xminimum 30
                    yminimum 30
                    padding (6, 2)
                    background Solid("#b84c58")

                    text str(phone_total_unread()):
                        size 15
                        color "#ffffff"
                        xalign 0.5
                        yalign 0.5


screen phone_shell():
    tag phone_shell
    modal True
    zorder 200

    $ phone_screen_background = "#c9b9ab" if phone_current_app == "home" else "#f5f2ec"

    on "hide" action Function(phone_close)
    key "game_menu" action Function(phone_back)

    add Solid("#12101399")

    fixed:
        at phone_slide_in
        xsize 484
        ysize 960
        xalign 0.5
        yalign 0.5

        add "images/ui/phone/device/device_base.png"

        add AlphaMask(
            Solid(phone_screen_background, xysize=(484, 960)),
            "images/ui/phone/device/device_mask.png",
        )

        use phone_status_bar


        frame:
            style "phone_content_frame"
            xpos 35
            ypos 90
            xsize 414
            ysize 780

            fixed:
                xfill True
                yfill True

                if phone_current_app == "home":
                    use phone_home
                elif phone_current_app == "contacts":
                    use phone_contacts_app
                elif phone_current_app == "messages":
                    use phone_messages_app
                elif phone_current_app == "thread" and phone_current_thread:
                    use phone_thread_app(phone_current_thread)



        if phone_current_app == "thread":
            add AlphaMask(
                LiveComposite(
                    (484, 960),
                    (0, 870), Solid("#e8dfd5", xysize=(484, 40)),
                ),
                "images/ui/phone/device/device_mask.png",
            )

        if phone_image_preview:
            use phone_image_lightbox(phone_image_preview)


screen phone_status_bar():
    timer 1.0 repeat True action Function(renpy.restart_interaction)

    fixed:
        xpos 35
        ypos 58
        xsize 414
        ysize 32

        text phone_local_time():
            style "phone_small_text"
            xpos 12
            yalign 0.5
            color "#4f4a46"

        fixed:
            xpos 362
            yalign 0.5
            xsize 40
            ysize 18

            add Solid("#4f4a46"):
                xpos 0
                ypos 1
                xsize 31
                ysize 2
            add Solid("#4f4a46"):
                xpos 0
                ypos 15
                xsize 31
                ysize 2
            add Solid("#4f4a46"):
                xpos 0
                ypos 1
                xsize 2
                ysize 16
            add Solid("#4f4a46"):
                xpos 29
                ypos 1
                xsize 2
                ysize 16
            add Solid("#4f4a46"):
                xpos 33
                ypos 6
                xsize 3
                ysize 7
            add Solid("#4f4a46"):
                xpos 4
                ypos 5
                xsize 21
                ysize 8


screen phone_header(title, back=True):
    frame:
        style "phone_header_frame"
        xpos 0
        ypos 0
        xsize 414
        ysize 61

        if back:
            button:
                style "phone_nav_button"
                xpos 0
                yalign 0.5
                action Function(phone_back)

                add Transform("images/ui/phone/icons/arrow-left.svg", size=(27, 27)):
                    xalign 0.5
                    yalign 0.5

        text title:
            style "phone_title_text"
            xalign 0.5
            yalign 0.5


screen phone_home():
    fixed:
        xpos 0
        ypos 0
        xsize 414
        ysize 780

        add Solid("#c9b9ab")

        text phone_local_time():
            xalign 0.5
            ypos 70
            size 54
            color "#ffffff"
            bold True

        text phone_local_date():
            xalign 0.5
            ypos 133
            size 20
            color "#fffaf4"

        hbox:
            xalign 0.5
            ypos 250
            spacing 22

            use phone_app_icon("contacts", "通讯录", "images/ui/phone/icons/address-book.svg", "#779286")
            use phone_app_icon("messages", "聊天", "images/ui/phone/icons/message-circle.svg", "#9c6d78")

        button:
            style "phone_nav_button"
            xalign 0.5
            yalign 1.0
            yoffset -14
            action Function(phone_back)

            add Transform("images/ui/phone/icons/home.svg", size=(27, 27)):
                xalign 0.5
                yalign 0.5


screen phone_app_icon(app_id, label, icon_file, app_color):
    button:
        style "phone_app_button"
        action SetVariable("phone_current_app", app_id)

        vbox:
            xalign 0.5
            spacing 8

            frame:
                xsize 84
                ysize 84
                padding (18, 18)
                background Solid(app_color)

                add Transform(icon_file, size=(48, 48)):
                    xalign 0.5
                    yalign 0.5

            text label:
                xalign 0.5
                size 20
                color "#ffffff"


screen phone_avatar(person_id, avatar_size=58):
    $ avatar_file = phone_avatar_path(person_id)
    $ mask_file = "images/ui/phone/avatars/avatar_circle_mask.svg"

    fixed:
        xsize avatar_size
        ysize avatar_size
        yalign 0.5

        if avatar_file:
            add AlphaMask(
                Transform(avatar_file, size=(avatar_size, avatar_size)),
                Transform(mask_file, size=(avatar_size, avatar_size)),
            )
        else:
            add AlphaMask(
                Solid(phone_avatar_color(person_id), xysize=(avatar_size, avatar_size)),
                Transform(mask_file, size=(avatar_size, avatar_size)),
            )
            text phone_avatar_initial(person_id):
                xalign 0.5
                yalign 0.5
                size int(avatar_size * 0.46)
                color "#ffffff"


screen phone_contacts_app():
    use phone_header("通讯录")

    viewport:
        xpos 0
        ypos 61
        xsize 414
        ysize 719
        draggable True
        mousewheel True
        scrollbars None

        vbox:
            xfill True
            spacing 2

            for contact_id in phone_unlocked_contacts:
                $ contact = phone_contacts.get(contact_id)
                if contact:
                    button:
                        style "phone_list_button"
                        action Function(phone_open_thread, contact_id)

                        hbox:
                            spacing 12
                            yalign 0.5

                            use phone_avatar(contact_id, 58)

                            vbox:
                                yalign 0.5
                                spacing 2

                                text contact["name"] style "phone_body_text"
                                text contact["subtitle"]:
                                    style "phone_small_text"
                                    xmaximum 238


screen phone_messages_app():
    use phone_header("聊天")

    viewport:
        xpos 0
        ypos 61
        xsize 414
        ysize 719
        draggable True
        mousewheel True
        scrollbars None

        vbox:
            xfill True
            spacing 2

            for contact_id in phone_unlocked_contacts:
                $ contact = phone_contacts.get(contact_id)
                if contact:
                    button:
                        style "phone_list_button"
                        action Function(phone_open_thread, contact_id)

                        fixed:
                            xfill True
                            ysize 62

                            use phone_avatar(contact_id, 58)

                            text contact["name"]:
                                style "phone_body_text"
                                xpos 70
                                ypos 5
                                bold True

                            text phone_last_message(contact_id):
                                style "phone_small_text"
                                xpos 70
                                ypos 34
                                xmaximum 205
                                substitute False

                            if phone_unread_counts.get(contact_id, 0) > 0:
                                frame:
                                    xalign 1.0
                                    yalign 0.5
                                    xminimum 27
                                    yminimum 27
                                    padding (6, 2)
                                    background Solid("#b84c58")

                                    text str(phone_unread_counts.get(contact_id, 0)):
                                        size 14
                                        color "#ffffff"
                                        xalign 0.5
                                        yalign 0.5


screen phone_thread_app(thread_id):
    $ contact = phone_contacts[thread_id]
    $ media_panel_open = phone_media_filter is not None
    $ sticker_panel_open = phone_media_filter == "sticker"
    $ chat_viewport_height = 405 if sticker_panel_open else (521 if media_panel_open else 637)
    $ composer_ypos = 480 if sticker_panel_open else (596 if media_panel_open else 712)
    $ composer_height = 300 if sticker_panel_open else (184 if media_panel_open else 68)
    use phone_header(contact["name"])

    if phone_chat_scroll_handled != phone_chat_scroll_request:
        timer 0.10 action [
            SetVariable("phone_chat_scroll_handled", phone_chat_scroll_request),
            Function(phone_scroll_chat_to_bottom),
        ]

    viewport:
        id "phone_chat_viewport"
        xpos 8
        ypos 68
        xsize 394
        ysize chat_viewport_height
        yadjustment _phone_chat_yadjustment
        draggable True
        mousewheel True
        scrollbars None
        yinitial 1.0

        vbox:
            xfill True
            spacing 9

            null height 4
            for message_id in phone_thread_messages.get(thread_id, []):
                use phone_message_bubble(message_id)
            null height 8

    frame:
        xpos 0
        ypos composer_ypos
        xsize 414
        ysize composer_height
        padding (8, 7)
        background Solid("#e8dfd5")

        vbox:
            xfill True
            spacing 6

            hbox:
                xalign 0.5
                spacing 8

                use phone_filter_button("text", "images/ui/phone/icons/message-circle.svg")
                use phone_filter_button("image", "images/ui/phone/icons/photo.svg")
                use phone_filter_button("voice", "images/ui/phone/icons/microphone.svg")
                use phone_filter_button("sticker", "images/ui/phone/icons/mood-smile.svg")

            if sticker_panel_open:
                use phone_sticker_picker(thread_id)
            elif media_panel_open:
                $ available_replies = phone_available_replies(thread_id, phone_media_filter)
                if available_replies:
                    viewport:
                        xfill True
                        ysize 116
                        draggable True
                        mousewheel True
                        scrollbars None

                        vbox:
                            xfill True
                            spacing 5

                            for reply_id in available_replies:
                                $ reply = phone_reply_catalog[reply_id]
                                textbutton reply["label"]:
                                    style "phone_reply_button"
                                    text_style "phone_reply_button_text"
                                    action Function(phone_send_reply, thread_id, reply_id)
                else:
                    text "暂无可发送的内容":
                        style "phone_small_text"
                        xalign 0.5
                        ypos 27


screen phone_sticker_picker(thread_id):
    $ sticker_packs = phone_get_sticker_packs()
    $ active_pack_id = phone_active_sticker_pack()

    if sticker_packs and active_pack_id:
        $ active_pack = next(pack for pack in sticker_packs if pack["id"] == active_pack_id)

        vbox:
            xfill True
            spacing 5

            vpgrid:
                cols 3
                xfill True
                ysize 166
                spacing 5
                draggable True
                mousewheel True
                scrollbars None

                for sticker_file in active_pack["stickers"]:
                    button:
                        xsize 94
                        ysize 94
                        padding (7, 7)
                        background Solid("#f3efea")
                        hover_background Solid("#ded4ca")
                        action Function(phone_send_sticker, thread_id, sticker_file)

                        add Transform(sticker_file, size=(80, 80)):
                            xalign 0.5
                            yalign 0.5

            viewport:
                xfill True
                ysize 48
                draggable True
                mousewheel "horizontal"
                scrollbars None

                hbox:
                    spacing 6

                    for pack in sticker_packs:
                        button:
                            xsize 46
                            ysize 46
                            padding (5, 5)
                            selected active_pack_id == pack["id"]
                            background Solid("#eee9e2")
                            hover_background Solid("#ded5ca")
                            selected_background Solid("#c7b9aa")
                            action SetVariable("phone_sticker_pack", pack["id"])
                            tooltip pack["label"]

                            add Transform(pack["icon"], size=(36, 36)):
                                xalign 0.5
                                yalign 0.5
    else:
        text "请将表情图片放入 stickers/<组名>/ 文件夹":
            style "phone_small_text"
            xalign 0.5
            text_align 0.5
            xmaximum 290


screen phone_filter_button(filter_id, icon_file):
    button:
        style "phone_media_button"
        selected phone_media_filter == filter_id
        action Function(phone_toggle_media_filter, filter_id)

        add Transform(icon_file, size=(25, 25)):
            xalign 0.5
            yalign 0.5


screen phone_message_bubble(message_id):
    $ message = phone_get_message(message_id)
    $ outgoing = message.get("sender") == "player"
    $ bubble_align = 1.0 if outgoing else 0.0
    $ bubble_color = "#806574" if outgoing else "#ffffff"
    $ message_text_style = "phone_bubble_out_text" if outgoing else "phone_bubble_text"

    hbox:
        xalign bubble_align
        box_reverse outgoing
        spacing 8

        use phone_avatar(message.get("sender"), 44)

        vbox:
            xalign bubble_align
            spacing 2

            if message.get("type") == "sticker":
                button:
                    xalign bubble_align
                    xsize 104
                    ysize 104
                    padding (12, 12)
                    background None
                    action NullAction()

                    add Transform(message.get("file"), size=(80, 80))
            else:
                frame:
                    xalign bubble_align
                    xmaximum 270
                    padding (12, 9)
                    background Solid(bubble_color)

                    if message.get("type") == "text":
                        text message.get("content", ""):
                            style message_text_style
                            xmaximum 242
                    elif message.get("type") == "image":
                        button:
                            xsize 232
                            ysize 132
                            padding (0, 0)
                            background None
                            action SetVariable("phone_image_preview", message.get("file"))

                            add Transform(message.get("file"), size=(232, 132))
                    elif message.get("type") == "voice":
                        button:
                            xsize 210
                            ysize 46
                            padding (2, 2)
                            background None
                            action Function(phone_toggle_voice, message_id, message.get("file"))

                            hbox:
                                spacing 12
                                yalign 0.5

                                add Transform(
                                    "images/ui/phone/icons/player-pause.svg" if phone_voice_playing == message_id else "images/ui/phone/icons/player-play.svg",
                                    size=(28, 28))
                                text "{} 秒".format(message.get("duration", 0)):
                                    style message_text_style
                                    yalign 0.5
                    else:
                        text "无法显示的消息":
                            style "phone_small_text"

            text message.get("time", ""):
                style "phone_small_text"
                xalign bubble_align
                color "#8c8580"


screen phone_image_lightbox(image_file):
    fixed:
        xpos 48
        ypos 70
        xsize 388
        ysize 820

        add Solid("#161416ee")

        button:
            xfill True
            yfill True
            background None
            action SetVariable("phone_image_preview", None)

        add Transform(image_file, size=(348, 560)):
            xalign 0.5
            yalign 0.5

        button:
            style "phone_nav_button"
            xpos 376
            xanchor 1.0
            ypos 10
            action SetVariable("phone_image_preview", None)

            add Transform("images/ui/phone/icons/x.svg", size=(28, 28)):
                xalign 0.5
                yalign 0.5


label phone_demo:
    scene bg park_1_day
    $ phone_enabled = True
    $ phone_hidden = False
    $ phone_begin()
    show screen phone_shell
    "手机功能测试已启用。请点击画面右上角的手机图标。"
    "测试结束后可以从聊天回复产生的 phone_story_flags 中读取剧情选择。"
    return


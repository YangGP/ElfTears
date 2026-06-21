transform phone_slide_in:
    on show:
        alpha 0.0
        yoffset 900
        easein_back 0.38 alpha 1.0 yoffset 0
    on hide:
        easeout 0.18 alpha 0.0 yoffset 180

transform phone_launcher_idle:
    zoom 1.0

    on hover:
        ease 0.12 zoom 1.06
    on idle:
        ease 0.12 zoom 1.0

style phone_launcher_button is button:
    xsize 68
    ysize 68
    padding (15, 15)
    background Solid("#f8f5f0e8")
    hover_background Solid("#ffffff")
    insensitive_background Solid("#b8b8b8aa")

style phone_content_frame is empty:
    background Solid("#f5f2ec")
    padding (0, 0)

style phone_header_frame is empty:
    background Solid("#f5f2ec")
    padding (10, 8)

style phone_title_text is text:
    font gui.interface_text_font
    size 25
    color "#302d2b"
    bold True

style phone_body_text is text:
    font gui.interface_text_font
    size 20
    color "#3c3936"

style phone_small_text is text:
    font gui.interface_text_font
    size 14
    color "#77716b"

style phone_list_button is button:
    xfill True
    yminimum 78
    padding (10, 9)
    background Solid("#fffdfa")
    hover_background Solid("#ece6dd")

style phone_app_button is button:
    xsize 126
    ysize 150
    padding (13, 13)
    background None
    hover_background Solid("#ffffff55")

style phone_nav_button is button:
    xsize 46
    ysize 46
    padding (9, 9)
    background None
    hover_background Solid("#e7e0d7")

style phone_media_button is button:
    xsize 48
    ysize 42
    padding (9, 6)
    background Solid("#eee9e2")
    hover_background Solid("#ded5ca")
    selected_background Solid("#c7b9aa")

style phone_reply_button is button:
    xfill True
    yminimum 42
    padding (10, 7)
    background Solid("#755b68")
    hover_background Solid("#8f7180")

style phone_reply_button_text is button_text:
    font gui.interface_text_font
    size 16
    color "#ffffff"
    hover_color "#ffffff"
    xalign 0.5
    text_align 0.5

style phone_bubble_text is text:
    font gui.interface_text_font
    size 18
    color "#302d2b"

style phone_bubble_out_text is phone_bubble_text:
    color "#ffffff"


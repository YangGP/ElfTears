## 读取和保存屏幕 #####################################################################
##
## 这些屏幕负责让用户保存游戏并能够再次读取。由于它们几乎完全一样，因此这两个屏
## 幕都是以第三个屏幕 file_slots 来实现的。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#save https://doc.renpy.cn/zh-
## CN/screen_special.html#load

## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 450
define config.thumbnail_height = 230


screen save():

    tag menu

    add HBox(Transform("#101623", xsize=350), "#101623b2") # The background; can be whatever

    use file_slots(_("保存"))


screen load():

    tag menu

    add HBox(Transform("#101623", xsize=350), "#101623b2") # The background; can be whatever

    use file_slots(_("读取游戏"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))

    use game_menu(title)

    fixed:
        xsize 1500 xalign 1.0
        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True

        ## The page name, which can be edited by clicking on it.
        ## This can be pretty easily removed if you want.
        ## Don't forget to also remove the `default` at the top if so.
        button:
            style "page_label"
            key_events True
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value

        ## The grid of file slots.
        grid 3 2:
            style_prefix "slot"

            for i in range(3*2):
                $ slot = i + 1

                button:
                    action FileAction(slot)
                    has vbox

                    add FileScreenshot(slot) xalign 0.5

                    ## https://www.fabriziomusacchio.com/blog/2021-08-15-strftime_Cheat_Sheet/
                    text FileTime(slot,
                            format=_("{#file_time}%A, %B %d %Y, %H:%M"),
                            empty=_("空存档位")):
                        style "slot_time_text"

                    text FileSaveName(slot) style "slot_name_text"

                    # This means the player can hover this save
                    # slot and hit delete to delete it
                    key "save_delete" action FileDelete(slot)

        ## Buttons to access other pages.
        hbox:
            style_prefix "page"

            textbutton _("<") action FilePagePrevious()

            if config.has_autosave:
                textbutton _("{#auto_page}A") action FilePage("auto")

            if config.has_quicksave:
                textbutton _("{#quick_page}Q") action FilePage("quick")

            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, 10):
                textbutton "[page]" action FilePage(page)

            textbutton _(">") action FilePageNext()


style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color '#4a70cf'

style slot_grid:
    xalign 0.5
    yalign 0.5
    spacing 15

style slot_time_text:
    size 25
    xalign 0.5

style slot_vbox:
    spacing 12

style slot_button:
    xysize (480, 300)
    padding (15, 15, 15, 15)
    background "gui/button/slot_[prefix_]background.png"

style slot_button_text:
    size 21
    xalign 0.5
    idle_color '#aaaaaa'
    hover_color '#ff8335'
    selected_idle_color '#ffffff'

style page_hbox:
    xalign 0.5
    yalign 1.0
    spacing 5

style page_button:
    padding (15, 6, 15, 6)


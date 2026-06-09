
## 历史屏幕 ########################################################################
##
## 这是一个向用户显示对话历史的屏幕。虽然此屏幕没有什么特别之处，但它必须访问储
## 存在 _history_list 中的对话历史记录。
##
## https://doc.renpy.cn/zh-CN/history.html

define config.history_length = 250

screen history():

    tag menu

    ## 避免预缓存此屏幕，因为它可能非常大。
    predict False

    add HBox(Transform("#101623", xsize=350), "#101623b2") # The background; can be whatever

    use game_menu(_("历史"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical" yinitial 1.0

        has vbox

        style_prefix "history"

        for h in _history_list:

            frame:
                has hbox
                if h.who:
                    label h.who style 'history_name':
                        substitute False
                        ## 从 Character 对象中获取叙述角色的文字颜色，如果设置了
                        ## 的话。
                        if "color" in h.who_args:
                            text_color h.who_args["color"]
                        xsize 200   # this number and the null width
                                    # number should be the same
                else:
                    null width 200

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## 此代码决定了允许在历史记录屏幕上显示哪些标签。

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_frame:
    xsize 1400
    ysize None
    background None

style history_hbox:
    spacing 20

style history_vbox:
    spacing 20

style history_name:
    xalign 1.0

style history_name_text:
    text_align 1.0
    align (1.0, 0.0)
    color '#f93c3e'

style history_text:
    text_align 0.0

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

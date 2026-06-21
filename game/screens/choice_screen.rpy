
## 选择屏幕 ########################################################################
##
## 此屏幕用于显示由 menu 语句生成的游戏内选项。参数 items 是一个对象列表，每个对
## 象都有字幕和动作字段。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing 60

style choice_button:
    is default # This means it doesn't use the usual button styling
    xysize (960, 60)
    background Frame("gui/button/choice_[prefix_]background.png",
        150, 25, 150, 25, tile=False)
    padding (12, 12)

style choice_button_text:
    is default # This means it doesn't use the usual button text styling
    xalign 0.5 yalign 0.5
    idle_color "#303030"
    hover_color "#fff"
    insensitive_color "#303030"

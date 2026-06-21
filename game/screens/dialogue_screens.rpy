
## 对话屏幕 ########################################################################
##
## 对话屏幕用于向用户显示对话。它需要两个参数，who 和 what，分别是叙述角色的名字
## 和所叙述的文本。（如果没有名字，参数 who 可以是 None。）
##
## 此屏幕必须创建一个 id 为 what 的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为 who 和 id 为 window 的可视控件来应用样式属性。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    ## 如果有对话框头像，会将其显示在文本之上。请不要在手机界面下显示这个，因为
    ## 没有空间。
    add SideImage() xalign 0.0 yalign 1.0


## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

# Style for the dialogue window
style window:
    xalign 0.5
    yalign 0.95 
    xysize (1152, 240)
    padding (40, 40, 40, 40)
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

# Style for the dialogue
style say_dialogue:
    adjust_spacing False
    ypos 10

# The style for dialogue said by the narrator
style say_thought:
    is say_dialogue

# Style for the box containing the speaker's name
style namebox:
    xpos 30 
    ypos -70
    xysize (288, 60)
    background Frame("gui/namebox.png", 10, 10, 10, 10, tile=False, xalign=0)
    padding (10, 10, 10, 10)

# Style for the text with the speaker's name
style say_label:
    color '#ffffff'
    xalign 0.5
    yalign 0.5
    size 40
    


## 快捷菜单屏幕 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。

screen quick_menu():

    ## 确保该菜单出现在其他屏幕之上，
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            textbutton _("回退") action Rollback()
            textbutton _("历史") action ShowMenu('history')
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("保存") action ShowMenu('save')
            textbutton _("快存") action QuickSave()
            textbutton _("快读") action QuickLoad()
            textbutton _("设置") action ShowMenu('preferences')


## 此代码确保只要用户没有主动隐藏界面，就会在游戏中显示 quick_menu 屏幕。
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_hbox:
    xalign 0.5
    yalign 1.0 yoffset -8
    spacing 8

style quick_button:
    background None
    padding (15, 6, 15, 0)

style quick_button_text:
    size 21
    selected_color '#aaaaaa'
    idle_color "#444444"

## NVL 模式屏幕 ####################################################################
##
## 此屏幕用于 NVL 模式的对话和菜单。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#nvl



screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
        spacing 15

        use nvl_dialogue(dialogue)

        ## 显示菜单，如果给定的话。如果 config.narrator_menu 设置为 True，则菜单
        ## 可能显示不正确。
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit True

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 此语句控制一次可以显示的 NVL 模式条目的最大数量。
define config.nvl_list_length = 6

# The style for the NVL "textbox"
style nvl_window:
    is default
    xfill True yfill True
    background "gui/nvl.png"
    padding (0, 60, 0, 60)

# The style for the text of the speaker's name
style nvl_label:
    is say_label
    xpos 192 xanchor 1.0
    ypos 0 yanchor 0.0
    xsize 300 #225
    min_width 300 #225
    text_align 1.0

# The style for dialogue in NVL
style nvl_dialogue:
    is say_dialogue
    xpos 288
    ypos 12
    xsize 1440
    min_width 1440

# The style for dialogue said by the narrator in NVL
style nvl_thought:
    is nvl_dialogue

style nvl_button:
    xpos 288
    xanchor 0.0


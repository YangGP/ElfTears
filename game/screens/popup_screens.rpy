
## 确认屏幕 ########################################################################
##
## 当 Ren'Py 需要询问用户有关确定或取消的问题时，会调用确认屏幕。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#confirm

screen confirm(message, yes_action, no_action=None):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "#000000ff" # You can replace this with your own overlay image

    frame:
        has vbox

        label _(message) style "confirm_prompt"

        hbox:

            textbutton _("确定") action yes_action
            # Modified so you can just have a confirmation prompt
            if no_action is not None:
                textbutton _("取消") action no_action

    ## Right-click and escape answer "no".
    if no_action is not None:
        key "game_menu" action no_action
    else:
        key "game_menu" action yes_action

style confirm_frame:
    background Frame("gui/frame.png", 60, 60, 60, 60, tile=False)
    padding (60, 60, 60, 60)
    xalign 0.5
    yalign 0.5

style confirm_vbox:
    align (0.5, 0.5)
    spacing 45

style confirm_prompt:
    xalign 0.5

style confirm_prompt_text:
    text_align 0.5
    align (0.5, 0.5)
    layout "subtitle"

style confirm_hbox:
    xalign 0.5
    spacing 150

style confirm_button:
    xalign 0.5

style confirm_button_text:
    text_align 0.5


## 快进指示屏幕 ######################################################################
##
## skip_indicator 屏幕用于指示快进正在进行中。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:
        has hbox

        text _("正在快进")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_hbox:
    spacing 9

style skip_frame:
    is empty
    ypos 60
    background Frame("gui/skip.png", 24, 8, 75, 8, tile=False)
    padding (24, 8, 75, 8)

style skip_text:
    size 24

style skip_triangle:
    is skip_text
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"

## 通知屏幕 ########################################################################
##
## 通知屏幕用于向用户显示消息。（例如，当游戏快速保存或进行截屏时。）
##
## https://doc.renpy.cn/zh-CN/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 5 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame:
    is empty
    ypos 30
    xalign 1.0

    background Frame("gui/notify.png", 24, 8, 60, 8, tile=False)
    padding (40, 8, 30, 8)
            

style notify_text:
    size 24




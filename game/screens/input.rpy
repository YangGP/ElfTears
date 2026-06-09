
## 输入屏幕 ########################################################################
##
## 此屏幕用于显示 renpy.input。prompt 参数用于传递文本提示。
##
## 此屏幕必须创建一个 id 为 input 的输入可视控件来接受各种输入参数。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:
        # This makes the background the same as the ADV dialogue box

        vbox:
            xanchor 0.0 ypos 20 spacing 10
            text prompt style "input_prompt"
            input id "input"

style input_prompt:
    xalign 0.0

style input:
    xalign 0.0
    xmaximum 1116



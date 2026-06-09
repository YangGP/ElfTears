
## 设置屏幕 ########################################################################
##
## 设置屏幕允许用户配置游戏，使其更适合自己。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#preferences

screen preferences():

    tag menu

    add HBox(Transform("#101623", xsize=350), "#101623b2") # The background; can be whatever

    use game_menu(_("设置"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"
        has vbox

        hbox:
            box_wrap True

            if renpy.variant("pc") or renpy.variant("web"):
                # Only need fullscreen/windowed on desktop and web builds

                vbox:
                    style_prefix "radio"
                    label _("显示")
                    textbutton _("窗口"):
                        # Ensures this button is selected when
                        # not in fullscreen.
                        selected not preferences.fullscreen
                        action Preference("display", "window")
                    textbutton _("Fullscreen"):
                        action Preference("display", "fullscreen")

            vbox:
                style_prefix "check"
                label _("快进")
                textbutton _("未读文本") action Preference("skip", "toggle")
                textbutton _("选项后继续") action Preference("after choices", "toggle")
                textbutton _("忽略转场") action InvertSelected(Preference("transitions", "toggle"))

            ## 可在此处添加 radio_pref 或 check_pref 类型的额外 vbox，以添加
            ## 额外的创建者定义的偏好设置。

        null height 60

        hbox:
            style_prefix "slider"
            box_wrap True

            vbox:

                label _("文字速度")
                bar value Preference("text speed")

                label _("自动前进时间")
                bar value Preference("auto-forward time")

            vbox:

                if config.has_music:
                    label _("音乐音量")
                    hbox:
                        bar value Preference("music volume")

                if config.has_sound:
                    label _("音效音量")
                    hbox:
                        bar value Preference("sound volume")
                        if config.sample_sound:
                            textbutton _("测试") action Play("sound", config.sample_sound)


                if config.has_voice:
                    label _("语音音量")
                    hbox:
                        bar value Preference("voice volume")
                        if config.sample_voice:
                            textbutton _("测试") action Play("voice", config.sample_voice)

                if config.has_music or config.has_sound or config.has_voice:
                    null height 15
                    textbutton _("全部静音"):
                        style_prefix "check"
                        action Preference("all mute", "toggle")

### PREF
style pref_label:
    top_margin 20
    bottom_margin 20

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

## RADIO
style radio_label:
    is pref_label

style radio_label_text:
    is pref_label_text

style radio_vbox:
    is pref_vbox
    spacing 0

style radio_button:
    foreground "gui/button/radio_[prefix_]foreground.png"
    padding (50, -3, 10, 15)

## CHECK
style check_label:
    is pref_label
style check_label_text:
    is pref_label_text

style check_vbox:
    is pref_vbox
    spacing 0

style check_button:
    foreground "gui/button/check_[prefix_]foreground.png"
    padding (50, -3, 10, 15)

## SLIDER
style slider_label:
    is pref_label
style slider_label_text:
    is pref_label_text

style slider_slider:
    xsize 525

style slider_button:
    yalign 0.5
    left_margin 15

style slider_vbox:
    is pref_vbox
    xsize 675


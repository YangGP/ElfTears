
## 标题菜单屏幕 ######################################################################
##
## 用于在 Ren'Py 启动时显示标题菜单。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#main-menu

## Replace this with your background image, if you like
# image main_menu_background = HBox(
#     Solid("#1f2a45", xsize2=350),
#     Solid("#6b90eea2")
# )

image main_menu_background = "/gui/main_menu.png"

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add "main_menu_background"

    vbox:
        xpos 96
        yalign 0.5
        spacing 50

        textbutton _("开始游戏") action Start()

        textbutton _("读取游戏") action ShowMenu("load")

        textbutton _("设置") action ShowMenu("preferences")

        textbutton _("关于") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("帮助") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("退出") action Quit(confirm=not main_menu)


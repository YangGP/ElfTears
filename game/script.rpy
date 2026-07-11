# 游戏的脚本可置于此文件中。

# 默认名字，可以在游戏开始时让玩家输入
default player_name = "凛恩"
# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define p = Character("[player_name]", color="#1a365d")
define xwy = Character("希薇娅", color="#722f37")
define klls = Character("克拉丽丝", color="#0b5334")
define ql = Character("绮莉", color="#3a4750")
define s = Character(None, kind=nvl)

define n = Character("Nora", color="#0b5334")

# 假设你的游戏标准分辨率是 1920x1080
# 这是一个万能背景适配变换
transform bg_cover:
    # 确保图片锚点和位置都在正中央
    xanchor 0.5 yanchor 0.5
    xpos 0.5 ypos 0.5
    
    # 核心算法：让图片强行覆盖 1920x1080 的区域，Ren'Py 会自动做等比最大化处理
    size (1920, 1080)

# 动画定义
transform sudden_shock:
    subpixel True
    xoffset 0
    # 极短时间内高频左右晃动
    linear 0.05 xoffset 15
    linear 0.05 xoffset -15
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 0

transform flip_once:
    # 用 0.2 秒翻转过去
    linear 0.2 xzoom -1.0
    # 停留 0.5 秒（你可以根据需要调整停留时间）
    pause 0.5
    # 再用 0.2 秒翻转回来
    linear 0.2 xzoom 1.0

transform rotate_360_once:
    # 2. 设定初始角度为 0
    rotate 0
    
    # 3. 在 1.0 秒内，平滑旋转到 360 度
    linear 1.0 rotate 360

# 游戏在此开始。

label start:

    menu:
        "精灵之泪 第一章":
            jump chapter1_part1
        "精灵之泪 第二章":
            jump chapter2_part1
        "测试选项":
            n "您选择了测试选项。"
            jump menu_start

    label menu_start:
        $ first_meet = True

        # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
        # （命名为 bg room.png 或 bg room.jpg）来显示。

        scene bg park_1_day

        # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
        # eileen happy.png 的文件来将其替换掉。

        show nora casual open

        # 此处显示各行对话。

        n "您好，我是 Nora。"
        n "这是一个简单的 Ren'Py 游戏示例。"


    if first_meet:
        show nora casual smile
        n "这是我们第一次见面！"
        n "现在选择您想要的下一步："
    else:
        scene bg park_1_day
        show nora casual smile
        n "欢迎回来！"
        n "现在选择您想要的下一步："

    menu:
        "精灵之泪":
            n "您选择了查看精灵之泪。"
            n "这是一个非常有趣的选项！"
            jump chapter1_part1
        "新立绘":
            n "您选择了查看新立绘。"
            jump new_character
        "背景变化":
            n "您选择了查看背景变化。"
            jump bg_change
        "人物变化":
            n "您选择了查看人物变化。"
            jump char_change
        "简单动画":
            n "您选择了查看简单动画。"
            jump anim
        "结束游戏":
            n "这就结束了吗？好吧，结束游戏！"
            jump end


    label new_character:
        show klls uniform1 微笑 at custom_image_center
        klls "您好，我是克拉丽丝。"

    label bg_change:
        $ first_meet = False
        scene bg park_2_day
        with dissolve
        show nora casual closed smile
        n "我为您切换了背景！"
        show nora casual closed smile at right
        with move
        n "我也换了个位置！"
        n "不知道您喜欢吗？"
        scene bg park_2_afternoon
        show nora casual smile at right
        with dissolve
        n "不小心到下午了，该回去了！"
        jump menu_start

    label char_change:
        $ first_meet = False
        show nora casual smile at left
        with move
        n "我跑到了左边！"
        show nora casual smile at right
        with move
        n "又回到了右边！"
        "蹦！" with vpunch
        show nora casual closed smile at center
        with move
        n "啊！吓我一跳！"
        show nora casual smile
        extend "但是我通常很快就能恢复过来！"
        n "好了，继续吧！"
        jump menu_start

    label anim:
        $ first_meet = False
        show nora casual closed smile at sudden_shock
        n "我刚才被吓了一跳！"
        show nora casual closed smile at flip_once
        n "我转了一圈！感觉好像在跳舞一样！"
        show nora casual closed smile at rotate_360_once
        n "我还会这样转圈！"
        show nora casual smile
        n "不过我觉得还是有点晕了，先休息一下吧！"
        n "让我们回去吧！"
        jump menu_start

    label end:
        n "虽然有点突然，但我还是很高兴和您一起玩这个游戏！"
        n "感谢您的游玩！"

    # 此处为游戏结尾。

    return
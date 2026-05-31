init python:
    # 封装一个函数：输入你想要的“目标高度”，它会自动帮你计算出 zoom 比例
    def get_height_zoom(img_path, target_height):
        # 获取图片原始大小
        width, height = renpy.image_size(img_path)
        # 计算比例
        return float(target_height) / float(height)

# 定义立绘的缩放变换 依次为 稍近距离 正常距离
transform x_gal_base_near:
    zoom 1      # 等比缩小
    yanchor 1.0    # 锚点定在立绘底部
    ypos 2.3      # 在屏幕上的垂直位置（1.05 会让立绘脚部稍微沉入屏幕下方一点，更自然）

transform x_gal_base:
    zoom 0.74
    yanchor 1.0
    ypos 1.75

transform x_gal_left:
    x_gal_base
    xpos 0.2
    xanchor 0.5

transform x_gal_right:
    x_gal_base
    xpos 0.8
    xanchor 0.5

transform q_gal_sprite_near:
    zoom 0.6      # 等比缩小
    yanchor 1.0    # 锚点定在立绘底部
    ypos 2.0      # 在屏幕上的垂直位置（1.05 会让立绘脚部稍微沉入屏幕下方一点，更自然）

transform q_gal_base:
    zoom 0.5
    yanchor 1.0
    ypos 1.7

transform q_gal_left:
    q_gal_base
    xpos 0.2
    xanchor 0.5

transform q_gal_right:
    q_gal_base
    xpos 0.8
    xanchor 0.5

transform k_gal_sprite_near:
    zoom 0.9      # 等比缩小
    yanchor 1.0    # 锚点定在立绘底部
    ypos 2.15      # 在屏幕上的垂直位置（1.05 会让立绘脚部稍微沉入屏幕下方一点，更自然）

transform k_gal_base:
    zoom 0.7
    yanchor 1.0
    ypos 1.7

transform k_gal_left:
    k_gal_base
    xpos 0.2
    xanchor 0.5

transform k_gal_right:
    k_gal_base
    xpos 0.8
    xanchor 0.5

# 定义时直接计算 zoom
image nora casual open = Transform("images/Nora_NoranekoGames/nora casual_open.png", zoom=get_height_zoom("images/Nora_NoranekoGames/nora casual_open.png", 900), yalign=1.0)
image nora casual smile = Transform("images/Nora_NoranekoGames/nora casual_smile.png", zoom=get_height_zoom("images/Nora_NoranekoGames/nora casual_smile.png", 900), yalign=1.0)
image nora casual closed smile = Transform("images/Nora_NoranekoGames/nora casual_closed_smile.png", zoom=get_height_zoom("images/Nora_NoranekoGames/nora casual_closed_smile.png", 900), yalign=1.0)
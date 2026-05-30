init python:
    # 封装一个函数：输入你想要的“目标高度”，它会自动帮你计算出 zoom 比例
    def get_height_zoom(img_path, target_height):
        # 获取图片原始大小
        width, height = renpy.image_size(img_path)
        # 计算比例
        return float(target_height) / float(height)

# 定义时直接计算 zoom
image nora casual open = Transform("images/Nora_NoranekoGames/nora casual_open.png", zoom=get_height_zoom("images/Nora_NoranekoGames/nora casual_open.png", 900), yalign=1.0)
image nora casual smile = Transform("images/Nora_NoranekoGames/nora casual_smile.png", zoom=get_height_zoom("images/Nora_NoranekoGames/nora casual_smile.png", 900), yalign=1.0)
image nora casual closed smile = Transform("images/Nora_NoranekoGames/nora casual_closed_smile.png", zoom=get_height_zoom("images/Nora_NoranekoGames/nora casual_closed_smile.png", 900), yalign=1.0)

# 用来预处理人物立绘
image k clothes normal = Transform("images/character illustration/k clothes normal.jpg", zoom=get_height_zoom("images/character illustration/k clothes normal.jpg", 900), yalign=1.0)
image k clothes sleepwear = Transform("images/character illustration/k clothes sleepwear.png", zoom=get_height_zoom("images/character illustration/k clothes sleepwear.png", 900), yalign=1.0)
image k clothes uniform = Transform("images/character illustration/k clothes uniform.jpg", zoom=get_height_zoom("images/character illustration/k clothes uniform.jpg", 900), yalign=1.0)

image q clothes normal = Transform("images/character illustration/q clothes normal.jpg", zoom=get_height_zoom("images/character illustration/q clothes normal.jpg", 900), yalign=1.0)
image q clothes sleepwear = Transform("images/character illustration/q clothes sleepwear.png", zoom=get_height_zoom("images/character illustration/q clothes sleepwear.png", 900), yalign=1.0)
image q clothes uniform = Transform("images/character illustration/q clothes uniform.png", zoom=get_height_zoom("images/character illustration/q clothes uniform.png", 900), yalign=1.0)

image x clothes normal = Transform("images/character illustration/x clothes normal.png", zoom=get_height_zoom("images/character illustration/x clothes normal.png", 900), yalign=1.0)
image x clothes sleepwear = Transform("images/character illustration/x clothes sleepwear.jpg", zoom=get_height_zoom("images/character illustration/x clothes sleepwear.jpg", 900), yalign=1.0)
image x clothes uniform = Transform("images/character illustration/x clothes uniform.jpg", zoom=get_height_zoom("images/character illustration/x clothes uniform.jpg", 900), yalign=1.0)
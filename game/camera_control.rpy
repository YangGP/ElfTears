# 通用的近景拉近 Camera 动作
transform cam_zoom_in:
    anchor (0.5, 0.5)
    pos (0.5, 0.5) # 瞬间锁定初始位置，防止轨迹乱晃
    
    # 执行平滑拉近
    # zoom 1.4: 画面整体放大 1.4 倍
    # pos (0.5, 0.65): X轴死死钉在 0.5，Y轴下移到 0.65，让画面重心稍微下移，更符合视觉习惯
    ease 1.0 zoom 1.4 pos (0.5, 0.65)

# 通用的恢复 Camera 动作
transform cam_zoom_out:
    ease 1.0 zoom 1.0 pos (0.5, 0.5)
# Phone Avatars

Place the following square image files in this directory. PNG, JPG, JPEG and WEBP are supported:

- `player.png` or `player.jpg`: male protagonist / sender id `player`
- `female_1.png` or `female_1.jpg`: heroine 1, 希薇娅 / sender id `x`
- `female_2.png` or `female_2.jpg`: heroine 2, 克拉丽丝 / sender id `k`
- `female_3.png` or `female_3.jpg`: heroine 3, 绮莉 / sender id `q`

Recommended source size: 256x256 or 512x512. Keep the face near the center.
The phone UI crops each image with `avatar_circle_mask.svg`. Missing files use
a colored initial placeholder, so all four images can be added independently.


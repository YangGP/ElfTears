# ElfTears 手机系统设计与实施规范

状态：已确认，进入首版开发  
目标版本：Phone MVP 1.0  
基准环境：Ren'Py 8.5.3，虚拟分辨率 1920x1080

## 1. 首版目标

玩家可在普通剧情画面点击手机图标，打开一个不会切换到游戏菜单、不会破坏当前剧情执行栈的手机界面。首版包含：

- 手机桌面。
- 通讯录。
- 聊天列表和未读数。
- 文本、图片、语音、表情包四类消息。
- 玩家从剧情预设内容中选择并发送文本、图片、语音或表情包。
- 剧情脚本可解锁联系人、推送消息、开放回复并读取玩家选择结果。
- 手机状态支持存档、读档和回滚。

首版不包含真实麦克风录音、访问系统相册、自由文本 AI 聊天、朋友圈和来电系统。这些能力不得混入 MVP。

## 2. 现有项目判断

- 项目虚拟分辨率为 1920x1080。
- `game/PhoneTexting.rpy` 是未接线的 NVL 短信演出原型，引用资源不完整，且主角名硬编码为 `Nighten`。
- 新系统独立放在 `game/phone/`，不依赖旧原型。旧文件暂时保留，待新系统验证后再决定删除或改造成剧情演出模式。
- 手机入口采用 overlay screen；手机本体采用普通 modal screen，不使用 `ShowMenu()`。

## 3. 交互流程

1. `phone_enabled` 为真且当前不在主菜单、游戏菜单或强制隐藏阶段时，画面右上角显示手机入口。
2. 点击入口后背景变暗，手机从下方进入。
3. 手机桌面显示“通讯录”和“聊天”两个 App。
4. 通讯录只显示已解锁角色；点击联系人进入对应聊天。
5. 聊天列表显示头像、最后消息摘要和未读数。
6. 聊天页面按时间显示消息，打开会话后清除该会话未读数。
7. 底部发送区只展示当前剧情已经开放的回复。媒体按钮分别筛选图片、语音和表情包回复。
8. 关闭手机后回到原剧情交互，不进行 `Jump()` 或 `Call()`。

## 4. 模块与目录

```text
game/phone/
  phone_data.rpy       # 联系人、消息目录、回复定义
  phone_state.rpy      # 存档状态和剧情 API
  phone_screens.rpy    # 入口、外壳、桌面、通讯录、聊天
  phone_styles.rpy     # 手机专用样式和动画

game/images/ui/phone/
  device/              # 缩小后的框体、overlay、mask
  icons/               # 通用 UI 图标
  avatars/             # 联系人头像
  chat_images/         # 聊天图片
  stickers/            # 表情包

game/audio/phone/
  voice/               # 预录的主角/角色语音
```

## 5. 数据规范

静态定义使用稳定字符串 ID，存档只保存 ID 和简单值。禁止在存档状态中保存 Displayable、Screen Action、函数、lambda 或音频对象。

消息字段：

```python
{
    "sender": "x",
    "type": "text",       # text/image/voice/sticker/system
    "content": "到家了吗？",
    "file": None,
    "duration": None,
    "alt": "图片替代文本",
    "time": "20:16",
}
```

存档变量：

```renpy
default phone_enabled = True
default phone_unlocked_contacts = []
default phone_thread_messages = {}
default phone_read_counts = {}
default phone_reply_offers = {}
default phone_story_flags = set()
default phone_current_app = "home"
default phone_current_thread = None
```

嵌套集合更新应通过复制后重新赋值完成，确保 Ren'Py 回滚能准确追踪。

## 6. 剧情 API

```renpy
$ phone_unlock_contact("x")
$ phone_push("x", "x_001")
$ phone_offer_reply("x", "reply_home_safe")
$ phone_clear_replies("x")

if phone_has_flag("replied_x_home_safe"):
    x "看到你的回复，我就放心了。"
```

自由浏览手机时，回复只写入消息和剧情 flag，不从 screen 内跳转 label。未来确有“必须完成聊天才继续”的剧情时，另建 `call screen phone_required_reply(...)`，不复用自由浏览入口。

## 7. 手机框体素材

源素材目录：`D:/游戏开发/Renpy/素材库/手机电脑UI/Phone`

三张 PNG 均为 2420x4800，高度超过当前运行环境报告的 4096 最大纹理尺寸。运行时统一等比导出为 484x960：

- `phone PNG.png` -> `device_base.png`
- `phone overlay for PNG.png` 不用于运行时（白色高光会遮挡交互界面）
- `phone mask for PNG.png` -> `device_mask.png`

PSD、PDN、XCF 不复制进游戏发行目录。交互内容限制在屏幕安全区。首轮运行截图后再校准安全区坐标。

## 8. 图标与许可

首版采用 Tabler Icons 的 outline SVG 图标，来源为官方仓库 `tabler/tabler-icons`，项目采用 MIT License。下载的原始 SVG 与许可证副本一并保留，具体文件、来源 URL 和版本记录在 `game/images/ui/phone/icons/ATTRIBUTION.md`。

计划使用：device-mobile、address-book、message-circle、arrow-left、x、photo、microphone、mood-smile、send、player-play、player-pause。

如某个上游文件名变更，允许换成同项目语义最接近的图标，不允许改用来源不明的搜索图片。

## 9. 音频行为

- 注册 `phone_voice` 单独声道，混入 `sfx` mixer。
- 同时只能播放一条手机语音。
- 点击当前播放语音时停止；点击另一条时切换。
- 关闭手机时停止手机语音。
- 缺少真实录音时，语音消息仍可显示并使用短占位音频验证播放逻辑。

## 10. 可见性与输入约束

- 手机打开后 `modal True`，不得点击到底层对话、选择或 quick menu。
- 手机打开期间隐藏 quick menu。
- 主菜单、游戏菜单和手机被剧情锁定时隐藏入口。
- 支持鼠标滚轮、拖拽滚动和触屏按钮。
- Escape/右键优先返回手机上一层；在桌面再次返回则关闭手机。

## 11. 验收标准

- 右上角入口可打开和关闭手机，底层剧情不被误触。
- 桌面、通讯录、聊天列表、聊天详情均可导航。
- 五类消息能正确渲染，文本不溢出气泡。
- 玩家能发送至少一种文本、图片、语音和表情包预设回复。
- 图片可放大预览，语音可播放/停止。
- 未读数、已读状态和剧情 flag 正确。
- 保存、读取和回滚后手机数据一致。
- Ren'Py lint 无新增错误，运行时无缺失资源异常。
- 1920x1080 桌面布局可用，触屏 variant 的按钮具有足够点击面积。

## 12. 实施顺序

1. 固化本文档并准备有许可证记录的运行时素材。
2. 实现状态层、消息目录和剧情 API。
3. 实现入口、外壳与导航。
4. 实现通讯录、聊天列表和五类消息。
5. 实现回复选择、媒体预览与语音播放。
6. 接入独立测试 label，不侵入正式第一章剧情。
7. 执行 lint、启动和存档/回滚验证，记录剩余问题。


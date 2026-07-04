# Static phone content. Save files only store the stable ids declared here.

define phone_contacts = {
    "x": {
        "name": "希薇娅",
        "subtitle": "总是会认真确认你有没有平安到家",
        "color": "#9f6f75",
        "initial": "希",
    },
    "k": {
        "name": "克拉丽丝",
        "subtitle": "回复很简短，但从不会漏看消息",
        "color": "#547d69",
        "initial": "克",
    },
}

define phone_message_catalog = {
    "x_001": {
        "sender": "x",
        "type": "text",
        "content": "到家了吗？看到的话记得回我。",
        "time": "20:16",
    },
    "x_002": {
        "sender": "x",
        "type": "image",
        "file": "images/city/bg park_1_day.png",
        "alt": "白天的公园",
        "time": "20:17",
    },
    "x_003": {
        "sender": "x",
        "type": "voice",
        "file": "audio/phone/voice/demo_voice.wav",
        "duration": 3,
        "time": "20:18",
    },
    "x_004": {
        "sender": "x",
        "type": "sticker",
        "file": "images/ui/phone/icons/mood-smile.svg",
        "alt": "微笑",
        "time": "20:18",
    },
    "k_001": {
        "sender": "k",
        "type": "text",
        "content": "明天见。别迟到。",
        "time": "19:42",
    },
    "player_text_home": {
        "sender": "player",
        "type": "text",
        "content": "已经到了，放心吧。",
        "time": "20:20",
    },
    "player_image_park": {
        "sender": "player",
        "type": "image",
        "file": "images/city/bg park_2_day.png",
        "alt": "公园的另一张照片",
        "time": "20:20",
    },
    "player_voice_ok": {
        "sender": "player",
        "type": "voice",
        "file": "audio/phone/voice/demo_voice.wav",
        "duration": 3,
        "time": "20:20",
    },
    "player_sticker_smile": {
        "sender": "player",
        "type": "sticker",
        "file": "images/ui/phone/icons/mood-smile.svg",
        "alt": "微笑",
        "time": "20:20",
    },
}

define phone_reply_catalog = {
    "reply_home_safe": {
        "thread": "x",
        "type": "text",
        "label": "已经到了，放心吧。",
        "message": "player_text_home",
        "flag": "replied_x_home_safe",
    },
    "reply_park_photo": {
        "thread": "x",
        "type": "image",
        "label": "发送公园照片",
        "message": "player_image_park",
        "flag": "sent_x_park_photo",
    },
    "reply_voice_ok": {
        "thread": "x",
        "type": "voice",
        "label": "发送语音",
        "message": "player_voice_ok",
        "flag": "sent_x_voice",
    },
    "reply_sticker_smile": {
        "thread": "x",
        "type": "sticker",
        "label": "发送微笑表情",
        "message": "player_sticker_smile",
        "flag": "sent_x_sticker",
    },
}


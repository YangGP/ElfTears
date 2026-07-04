# Fixed avatar slots. Images are optional and discovered with renpy.loadable().

define phone_avatar_slots = {
    "player": "images/ui/phone/avatars/player",
    "x": "images/ui/phone/avatars/female_1",
    "k": "images/ui/phone/avatars/female_2",
    "q": "images/ui/phone/avatars/female_3",
}

define phone_avatar_fallback_colors = {
    "player": "#60758d",
    "x": "#9f6f75",
    "k": "#547d69",
    "q": "#69737c",
}

init -5 python:
    def phone_avatar_path(person_id):
        base_path = phone_avatar_slots.get(person_id)
        if not base_path:
            return None
        for extension in (".png", ".jpg", ".jpeg", ".webp"):
            path = base_path + extension
            if renpy.loadable(path):
                return path
        return None

    def phone_avatar_initial(person_id):
        if person_id == "player":
            return player_name[:1] if player_name else "主"
        contact = phone_contacts.get(person_id, {})
        return contact.get("initial", "?")

    def phone_avatar_color(person_id):
        contact = phone_contacts.get(person_id, {})
        return contact.get("color", phone_avatar_fallback_colors.get(person_id, "#777777"))


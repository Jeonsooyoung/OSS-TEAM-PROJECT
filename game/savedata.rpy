default player_name = None
default chanmi_affection = 20
default ari_affection = 20
default sena_affection = 20

init python:
    if persistent.game_data is None:
        persistent.game_data = {}
    
    def save_game_state():
        persistent.game_data = {
            "player_name": player_name,
            "chanmi_affection": chanmi_affection,
            "ari_affection": ari_affection,
            "sena_affection": sena_affection
        }
    
    def load_game_state():
        if persistent.game_data:
            global player_name, chanmi_affection, ari_affection, sena_affection
            player_name = persistent.game_data.get("player_name")
            chanmi_affection = persistent.game_data.get("chanmi_affection", 20)
            ari_affection = persistent.game_data.get("ari_affection", 20)
            sena_affection = persistent.game_data.get("sena_affection", 20)
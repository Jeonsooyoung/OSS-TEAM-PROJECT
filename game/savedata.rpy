default name_entered = False
default player_name = None
default chanmi_affection = 20
default ari_affection = 20
default sena_affection = 20

init python:
    if persistent.game_data is None:
        persistent.game_data = {
            "chanmi_affection": 20,
            "ari_affection": 20,
            "sena_affection": 20
        }
    
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

    def reset_persistent_data():
        persistent._clear()  # 모든 persistent 데이터 초기화
        
        # 기본 데이터 즉시 재설정
        persistent.game_data = {
            "chanmi_affection": 20,
            "ari_affection": 20,
            "sena_affection": 20
        }
        persistent.player_name = None
        persistent.chapter1_cleared = False
        persistent.chapter2_cleared = False
        persistent.chapter3_cleared = False
        persistent.chapter4_cleared = False
default name_entered = False
default player_name = None

default persistent.chanmi_affection = 20
default persistent.ari_affection = 20
default persistent.sena_affection = 20

default chanmi_affection = persistent.chanmi_affection
default ari_affection = persistent.ari_affection
default sena_affection = persistent.sena_affection

init python:
    def save_game_state():
        # 현재 상태를 저장
        persistent.chanmi_affection = chanmi_affection
        persistent.ari_affection = ari_affection
        persistent.sena_affection = sena_affection
        persistent.game_data = {
            "player_name": player_name,
            "chapter_selected": persistent.chapter_selected
        }
    
    def load_game_state():
        global player_name, chanmi_affection, ari_affection, sena_affection
        # persistent에서 직접 호감도 불러오기
        if hasattr(persistent, 'chanmi_affection'):
            chanmi_affection = persistent.chanmi_affection
        if hasattr(persistent, 'ari_affection'):
            ari_affection = persistent.ari_affection
        if hasattr(persistent, 'sena_affection'):
            sena_affection = persistent.sena_affection
        
        # 나머지 게임 데이터 불러오기
        if persistent.game_data:
            player_name = persistent.game_data.get("player_name", player_name)
            persistent.chapter_selected = persistent.game_data.get("chapter_selected", persistent.chapter_selected)

    def reset_persistent_data():
        # 초기화 시 호감도도 초기값으로 설정
        persistent.chanmi_affection = 20
        persistent.ari_affection = 20
        persistent.sena_affection = 20
        persistent.game_data = {
            "chapter_selected": 0
        }
        persistent.player_name = None
        persistent.chapter1_cleared = False
        persistent.chapter2_cleared = False
        persistent.chapter3_cleared = False
        persistent.chapter4_cleared = False
# 이 파일에 게임 스크립트를 입력합니다.

init python:
    def sync_player_name():
        global player_name
        player_name = persistent.player_name

default persistent.is_new_game = True

# 여기에서부터 게임이 시작합니다.
label start:
    stop music
    transform center:
        xalign 0.5
        yalign 0.6
    transform left:
        xalign 0.15
        yalign 0.6
    transform right:
        xalign 0.85
        yalign 0.6
    transform small_size:
        zoom 0.4   
    transform big_size:
        zoom 1.5


    $ renpy.block_rollback()

    
    # 새 게임이면 모든 데이터 초기화
    if persistent.is_new_game:
        $ reset_persistent_data()
        $ persistent.player_name = None
        $ player_name = None
        $ persistent.chapter_selected = 0
        $ persistent.is_new_game = False  # 초기화 후 플래그 변경
        
        "안녕하세요, 게임을 시작하기전 당신의 이름을 알려주세요!"

        while not persistent.player_name:
            $ persistent.player_name = renpy.input("이름을 입력해주세요.")
        
        $ sync_player_name()
        "당신의 이름은 [player_name]이군요! 게임을 시작합니다!"
        
        jump chapter1
    
    # 챕터 선택인 경우
    else:
        $ load_game_state()
        if persistent.chapter_selected == 0:
            jump chapter1
        elif persistent.chapter_selected == 1:
            jump chapter1
        elif persistent.chapter_selected == 2:
            jump chapter2
        elif persistent.chapter_selected == 3:
            jump chapter3
        elif persistent.chapter_selected == 4:
            jump chapter4
    
    return
# 이 파일에 게임 스크립트를 입력합니다.

init python:
    def sync_player_name():
        global player_name
        player_name = persistent.player_name

# 여기에서부터 게임이 시작합니다.
label start:
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

    $ reset_persistent_data()

    "안녕하세요, 게임을 시작하기전 당신의 이름을 알려주세요!"

    while not persistent.player_name:
        $ persistent.player_name = renpy.input("이름을 입력해주세요.")
    
    $ sync_player_name()

    "당신의 이름은 [player_name]이군요! 게임을 시작합니다!"
    $ load_game_state()
    jump chapter1
    
    return
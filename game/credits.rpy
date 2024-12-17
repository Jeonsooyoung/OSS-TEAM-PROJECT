init python:
    credits_list = [
        ('시나리오', '김선영\n박진용'),
        ('UI제작', '전수영'),
        ('시스템 구현', '서주영'),
        ('사운드 관리', '탁윤모'),
        ('Special Thanks', '김봉재 교수님')
    ]

    def credits_text():
        text = "{image=images/logo.png}\n\n"  # 로고 이미지를 맨 위에 추가
        text += "{color=#fff}{size=80}Credits\n\n"
        last_category = ""
        
        for category, name in credits_list:
            if category != last_category:
                text += "\n{size=40}" + category + "\n"
            text += "{size=60}" + name + "\n"
            last_category = category
            
        text += "\n\n\n\n{size=40}Made with\n{size=60}Ren'Py\n"
        text += "\n{size=40}2024 두근두근 충북대 by 옥수수수염차 All rights reserved\n"
        return text


init:
    image credits_logo = "images/logo.png"
    image credits_roll = Text(credits_text(), text_align=0.5, color="#fff")
    image end_text = Text("{size=80}Thank you for playing!", text_align=0.5, color="#fff")

label credits:
    scene black with dissolve
        # 퀵메뉴 숨기기
    $ _quick_menu = False
    $ credits_speed = 20.0  # 여기서 속도 조절 (숫자가 클수록 느림)
    $ renpy.pause(0.2)

    # 크레딧 스크롤
    show credits_roll at Move((0.5, 1.0), (0.5, -1.8), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="top")
    $ renpy.pause(credits_speed, hard=True)
    
    # # 크레딧 숨기기
    # hide credits_roll with dissolve
    # $ renpy.pause(2.0)
    
    # 엔딩 텍스트
    show end_text:
        xalign 0.5
        yalign 0.5
    with dissolve
    $ renpy.pause(5.0)
    
    hide end_text with dissolve
    $ renpy.full_restart()


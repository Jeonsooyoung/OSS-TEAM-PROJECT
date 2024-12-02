# 팝업창 애니메이션 정의
transform popup_appear:
    alpha 0.0
    linear 0.2 alpha 1.0
    pause 1.5
    linear 0.2 alpha 0.0

# 팝업창 스크린 정의
screen popup(message):
    zorder 100  # 다른 UI 요소들보다 앞에 표시
    
    frame:
        # 팝업창 배경 설정
        background Frame("gui/frame.png", 25, 25)  # gui 폴더의 frame.png 사용
        # 또는 단색 배경을 원한다면:
        # background "#000000B0"  # 마지막 B0는 투명도(알파값)
        
        # 팝업창 크기
        xsize 300
        ysize 150
        
        # 팝업창 위치
        xalign 0.0  # 0.0은 왼쪽, 1.0은 오른쪽, 0.5는 중앙
        yalign 0.0  # 0.0은 위쪽, 1.0은 아래쪽, 0.5는 중앙
        xoffset 20  # 왼쪽 여백
        yoffset 20  # 위쪽 여백
        
        # 내부 여백
        xpadding 20
        ypadding 10
        
        # 테두리 설정 (선택사항)
        # border (2, 2, 2, 2)  # 상하좌우 테두리 두께
        
        vbox:
            align (0.5, 0.5)  # 텍스트를 프레임 중앙에 배치
            spacing 10
            
            text message:
                size 20
                color "#ffffff"
                font "KCC-Ganpan.ttf"  # 원하는 폰트로 변경
                text_align 0.5  # 텍스트 중앙 정렬
                xalign 0.5
        
        at popup_appear  # 위에서 정의한 애니메이션 적용

# 팝업 표시 함수
init python:
    def show_popup(message):
        renpy.show_screen('popup', message=message)
        renpy.pause(2.0, hard=False)  # hard=True로 설정시 스킵 불가
        renpy.hide_screen('popup')
# 팝업창 애니메이션 정의
transform popup_appear:
    alpha 0.0
    linear 0.2 alpha 1.0
    pause 1.5
    linear 0.2 alpha 0.0

image increase_animation:   # 렌파이는 GIF파일을 지원하지 않음
    "gui/affection/increase1.png"
    pause 0.5
    "gui/affection/increase2.png"
    pause 0.1
    "gui/affection/increase3.png"
    pause 0.1
    "gui/affection/increase4.png"
    pause 0.1
    "gui/affection/increase5.png"
    pause 0.1
    "gui/affection/increase6.png"
    pause 0.1
    "gui/affection/increase7.png"
    pause 0.1
    "gui/affection/increase8.png"
    pause 0.1
    "gui/affection/increase9.png"
    pause 0.1
    #repeat   # 반복 여부

image decrease_animation:
    "gui/affection/decrease1.png"
    pause 0.5
    "gui/affection/decrease2.png"
    pause 0.1
    "gui/affection/decrease3.png"
    pause 0.1
    "gui/affection/decrease4.png"
    pause 0.1
    "gui/affection/decrease5.png"
    pause 0.1
    "gui/affection/decrease6.png"
    pause 0.1
    "gui/affection/decrease7.png"
    pause 0.1
    "gui/affection/decrease8.png"
    pause 0.1
    "gui/affection/decrease9.png"
    pause 0.1
    #repeat   # 반복 여부

# 팝업창 스크린 정의
screen increase_popup(message):
    hbox:
        spacing 10
        xalign 0.0
        yalign 0.0
        xoffset 20
        yoffset 20
        
        frame:
            background Frame("gui/frame.png", 25, 25)
            xsize 300
            ysize 150
            xalign 0.0
            yalign 0.0
            xpadding 20
            ypadding 10
            
            text message:
                size 20
                color "#ffffff"
                font "KCC-Ganpan.ttf"
                text_align 0.5
                xalign 0.5
        
        add "increase_animation":
            yalign 0.5
            size (180, 180)
        
        at popup_appear

screen decrease_popup(message):
    hbox:
        spacing 10
        xalign 0.0
        yalign 0.0
        xoffset 20
        yoffset 20
        
        frame:
            background Frame("gui/frame.png", 25, 25)
            xsize 300
            ysize 150
            xalign 0.0
            yalign 0.0
            xpadding 20
            ypadding 10
            
            text message:
                size 20
                color "#ffffff"
                font "KCC-Ganpan.ttf"
                text_align 0.5
                xalign 0.5
        
        add "decrease_animation":
            yalign 0.5
            size (180, 180)
        
        at popup_appear

init python:
    def show_increase_popup(message):
        renpy.show_screen('increase_popup', message=message)
        renpy.pause(2.0, hard=False)
        renpy.hide_screen('increase_popup')
        
    def show_decrease_popup(message):
        renpy.show_screen('decrease_popup', message=message)
        renpy.pause(2.0, hard=False)
        renpy.hide_screen('decrease_popup')
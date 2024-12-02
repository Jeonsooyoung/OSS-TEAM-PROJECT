screen popup(message):
    zorder 100
    frame:
        xalign 0.0
        yalign 0.0
        xpadding 20
        ypadding 10
        xoffset 20
        yoffset 20
        
        text message:
            size 20
            color "#ffffff"
            
        at transform:
            alpha 0.0
            linear 0.2 alpha 1.0
            pause 1.5
            linear 0.2 alpha 0.0

init python:
    def show_popup(message):
        renpy.show_screen('popup', message=message)
        renpy.pause(2.0)
        renpy.hide_screen('popup')
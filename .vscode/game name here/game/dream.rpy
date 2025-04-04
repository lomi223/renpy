label dream:
    stop music
    python hide:
        import webbrowser
        import os
        webbrowser.open('https://youtu.be/wJWksPWDKOc?t=1802&si=zaqwzP0pAnr9pPdV', new=0, autoraise=True)

    "...？"
    scene radio with Dissolve(2.0):
        zoom 1.5
    $ renpy.pause(5.0, hard=True)
    "也許我該讓音樂停下"
    play sound "fnaf-4-breathing.mp3" loop volume 0.3
    jump the_radio

label the_radio:
    if screen_changed:
        jump changed
    call screen radio_button

label not_here:
    if screen_changed:
        return
    "音樂似乎不是從這裡傳出來的......"
    
    call check_window_focus_label
    jump the_radio
    return

label check_window_focus_label:
    if screen_changed:
        return
    $ check_window_focus()
    return

label changed:
    scene black
    show b glitched:
        zoom 0.2
        xalign 0.5
        yalign 0.5
    $ renpy.pause(20.0, hard=True)
    hide b glitched
    stop sound
    play sound "glitch-from-doors.mp3"
    show bob very:
        xalign 0.6
        yalign 0.35
        zoom 0.1
        linear 0.5 zoom 5
    $ renpy.pause(2.0, hard=True)
    stop sound
    return

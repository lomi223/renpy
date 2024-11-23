label dream:
    stop music
    python:
        import webbrowser
        import os
        url = "https://youtu.be/wJWksPWDKOc?t=1802&si=zaqwzP0pAnr9pPdV"
        webbrowser.open(url, new=0, autoraise=True)
        real_name = os.getlogin()
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
    show b glitched
    $ renpy.pause(20.0, hard=True)
    stop sound
    play sound "glitch-from-doors.mp3"
    show b glitch:
        linear 0.5 zoom 5
    $ renpy.pause(2.0, hard=True)
    stop sound
    return
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
    pause 5.0
    "也許我該讓音樂停下"
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
    "changed"
    
    return
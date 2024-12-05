image hall:
    "scene/hallway.jpg"
    zoom 1.0
image class:
    "scene/classroom.webp"
    zoom 2.0
style test_style:
    color "#aa0000"

label bob_and_seak:
    scene black:
        zoom 2.0
    show hall
    stop music
    $ maze_layout = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    # Starting position
    $ player_x = 1
    $ player_y = 1

    jump maze_loop

label maze_loop:
    show screen arrow_down
    show screen arrow_left
    show screen arrow_right
    show screen arrow_up
    call screen maze_game
           
label pos_check:
    hide screen arrow_down
    hide screen arrow_left
    hide screen arrow_right
    hide screen arrow_up
    python:
        import math
        if player_x != 8 and player_y != 2:
            vol = 5/math.sqrt((player_x - 8)**2 + (player_y - 7)**2)
    play sound "SFX/laugh.mp3" volume vol
    if player_x == 8 and player_y == 2:
        scene black
        "You've reached the goal!"
        jump mend
    if maze_layout[player_y][player_x] == 0:
        call cammove
        hide class with dissolve
        show hall with dissolve
        call revcam
        
    if maze_layout[player_y][player_x] == 2:
        call cammove
        hide hall with dissolve
        show class with dissolve
        call revcam
    jump maze_loop
    return

label mend:
    scene class
    player "他似乎在這裡的樣子"
    call screen closet
    return

label foundu:
    scene black with dissolve
    centered "你打開了櫃子"
    scene class with dissolve
    show b norm with dissolve
    b "哎呀！居然被你發現了嘻嘻"
    b "那麼現在....."
    play sound "SFX/undertale-sound-effect-chara-jumpscare.mp3"
    b "{sc}{=test_style}{cps=5}{size=*1.5}輪．到．你．啦！{/size}{/cps}{/=test_style}{/sc}"
    call switch
    $ g_time = 30
    show screen timerFame(30, "hide_check")
    jump pl_turn
    return

label pl_turn:
    ""
    return

label hide_check:
    return

label switch:
    pause 0.1
    stop sound
    play sound "SFX/doors-lights-flicker.mp3"
    call flicker
    pause 0.1
    call flicker
    pause 0.5
    show class:
        subpixel True 
        matrixcolor TintMatrix("#110257ff")*InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.3)*HueMatrix(0.0) 
    pause 0.4
    show class:
        subpixel True 
        matrixcolor TintMatrix("#fff")*InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  
    pause 1.0
    show b scary
    pause 0.1
    hide b
    stop sound
    play sound "SFX/light-broke-doors.mp3"
    show class:
        subpixel True 
        matrixcolor TintMatrix("#110257ff")*InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.3)*HueMatrix(0.0) 
    return

label flicker:
    show class:
        subpixel True 
        matrixcolor TintMatrix("#110257ff")*InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.3)*HueMatrix(0.0) 
    pause 0.2
    show class:
        subpixel True 
        matrixcolor TintMatrix("#fff")*InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    pause 0.3
    show class:
        subpixel True 
        matrixcolor TintMatrix("#110257ff")*InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.3)*HueMatrix(0.0) 
    pause 0.2
    show class:
        subpixel True 
        matrixcolor TintMatrix("#fff")*InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    pause 0.1
    show class:
        subpixel True 
        matrixcolor TintMatrix("#110257ff")*InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.3)*HueMatrix(0.0) 
    pause 0.2
    show class:
        subpixel True 
        matrixcolor TintMatrix("#fff")*InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    return

label cammove:
    window auto hide
    camera:
        subpixel True blur 5.0
        parallel:
            xpos 0 zpos 0.0 
            linear 0.60 zpos -400.0 
        parallel:
            ypos 0 
            linear 0.10 ypos -40 
            linear 0.10 ypos 0 
            linear 0.10 ypos 40 
            linear 0.10 ypos 0 
            linear 0.10 ypos -40 
            linear 0.10 ypos 0 
            linear 0.10 ypos 40 
            linear 0.10 ypos 0 
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
            linear 0.60 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-1.0)*HueMatrix(0.0)
    with Pause(0.65)
    camera:
        blur 0.0
        pos (0, 0) zpos 0.0 
    return

label revcam:
    camera:
        linear 0.60 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    with Pause(0.65)
    return

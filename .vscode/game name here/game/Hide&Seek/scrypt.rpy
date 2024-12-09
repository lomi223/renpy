image hall:
    "scene/hallway.jpg"
    zoom 1.0
image class:
    "scene/classroom.webp"
    zoom 2.0
style test_style:
    color "#aa0000"

label bob_and_seak:
    $ player_at2 = False
    scene black:
        zoom 2.0
    show hall
    stop music
    $ maze_layout = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 2, 1]
    ]

    # Starting position
    $ player_x = 1
    $ player_y = 1
    "他似乎就在前面一點的位置"
    jump maze_loop

label maze_loop:
    show screen arrow_down
    show screen arrow_left
    show screen arrow_right
    call screen arrow_up
           
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
    b "{sc}{=test_style}{cps=5}{size=*1.5}輪‧到‧你‧啦！{/size}{/cps}{/=test_style}{/sc}"
    call switch
    
    jump pl_turn
    return

label pl_turn:
    play music "saiko-no-sutoka-no-shiki-ost.mp3"
    scene black:
        xpos -1000
        ypos -1000
        zoom 10.0
    $ player_at2 = True
    $ g_time = 120
    show screen timerFame(120, "hide_check")
    $ player_x = 1
    $ player_y = 18
    #20*20
    $ maze_layout = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
        [1, 1, 0, 2, 1, 0, 1, 1, 2, 0, 0, 0, 0, 1, 2, 0, 1, 1, 0, 1],
        [1, 1, 0, 1, 1, 0, 1, 2, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 0, 1, 1, 0, 1, 1, 2, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 2, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 2, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 2, 1, 2, 1, 1, 1, 0, 1, 2, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 2, 2, 2, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1, 0, 2, 1, 1],
        [1, 0, 1, 1, 1, 1, 2, 1, 0, 1, 0, 1, 1, 0, 2, 1, 0, 1, 1, 1],
        [1, 0, 2, 1, 1, 0, 0, 0, 1, 2, 2, 0, 1, 0, 1, 1, 2, 1, 1, 1],
        [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 2, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 2, 0, 1, 0, 1, 1, 2, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 2, 1, 2, 0, 0, 0, 1, 0, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    show class:
        subpixel True 
        zoom 0.8
        matrixcolor TintMatrix("#110257ff")*InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.3)*HueMatrix(0.0) 
    jump maze2
    return

label maze2:
    show screen arrow_down
    show screen arrow_left
    show screen arrow_right
    call screen arrow_up
    

label pos_check2:
    hide screen arrow_down
    hide screen arrow_left
    hide screen arrow_right
    hide screen arrow_up
    if player_x == 18 and player_y == 1:
        jump hide_check
    if maze_layout[player_y][player_x] == 0:
        call cammove2
        hide hall with Dissolve(0.2)
        hide class with Dissolve(0.2)
        show hall with Dissolve(0.2):
            zoom 1.0
            subpixel True 
            matrixcolor TintMatrix("#110257ff")*InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.3)*HueMatrix(0.0) 
        call revcam2
        
    if maze_layout[player_y][player_x] == 2:
        call cammove2
        hide class with Dissolve(0.2)
        hide hall with Dissolve(0.2)
        show class with Dissolve(0.2):
            zoom 1.0
            subpixel True 
            matrixcolor TintMatrix("#110257ff")*InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.3)*HueMatrix(0.0) 
        call revcam2
    jump maze2


label hide_check:
    stop music
    scene black
    if player_x != 18 and player_y != 1:
        jump fail
    jump success
    
    return

label fail:

    $ quick_menu = False
    play sound "SFX/clock-titan-sound.mp3"
    "時間停止的那刻你感覺空氣變得異常沉重{nw=2}"
    "你無法移動你的四肢{nw=1}"
    "你無法移動你的四肢{fast} 實際上你也感受不到他們{nw=1}"
    play music "halloween-logo-reveal-sounds--horror-sfx--no-copyright.mp3" noloop
    "四周一片{nw=0.17}"
    "{=test_style}{font=Terror.ttf}{size=*2}他在背後...{/font}{/size}{/=test_style}{nw=1.5}"
    stop sound
    $ renpy.pause(5.0,hard=True)
    play sound "<from 0 to 8.5>SFX/heart-beat.mp3" noloop
    $ renpy.pause(1.5,hard=True)
    play audio "SFX/breathing-sound-effect.mp3" noloop volume 0.05
    $ renpy.pause(8.5, hard=True)
    stop sound
    play sound "SFX/scary-girl.mp3"
    $ renpy.pause(3.2,hard=True)
    play music "ufail.mp3"
    $ renpy.pause(5.0,hard=True)
    $ caught = True
    $ delete_all_saves()
    $ persistent.bob = True
    $ renpy.quit()
    return

label success:
    $ quick_menu = False
    stop music
    scene black
    hide screen timerFame
    play sound "SFX/53271__the_bizniss__door-close-4.wav"
    show door with dissolve:
        default
        subpixel True xzoom 1.31 zoom 1.75 
    "你躲進了廁所的儲物間中"

    $ renpy.pause(2.0,hard=True)
    play sound "SFX/scary-riser_G_major.wav" volume 1.2 fadein 0.3
    window auto hide
    show door:
        subpixel True pos (0.67, 2.4) xzoom 1.71 zoom 6.39 
        zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 rotate 0.0 
        linear 5.50 zpos 0.0 xrotate 0.0 yrotate -45.0 zrotate 0.0 rotate 0.0 
    show frame:
        default
        subpixel True ypos -20 anchor (0, 0) matrixanchor (1.0, 1.0) xzoom 14.0 yzoom 3.38 
        xpos 0 zpos 0.0 
        linear 5.50 xpos -200 zpos 0.0 
    with Pause(5.60)
    show door:
        zpos 0.0 xrotate 0.0 yrotate -45.0 zrotate 0.0 rotate 0.0 
    show frame:
        pos (-200, -20) zpos 0.0 
    stop sound
    hide door
    hide frame
    
    play sound "SFX/野兽前辈原版.mp3" noloop
    $ renpy.pause(0.5)
    play audio "SFX/Woman Scream Sound Effect.mp3" noloop
    pause 7.0
    stop sound
    stop audio
    scene bathroom with dissolve:
        zoom 1.5
    $ quick_menu = True
    play music "snowdin-town.mp3" fadein 1.0
    show s norm with dissolve
    s "[player]你怎麼在這裡？"
    s "剛剛真是嚇到我了"
    player "對......對不起......"
    scene black with dissolve
    centered "你尷尬地跑開了"
    stop music fadeout 2.0
    play music "night.mp3" fadein 1.0
    show bedroom with dissolve:
        subpixel True 
        matrixcolor TintMatrix("#18213b")*InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.5)*HueMatrix(0.0) 
    player "今天究竟是怎麼回事啊？"
    player "算了，不去想了"
    player "今天真是累死我了"
    scene black with dissolve
    centered "你閉上了沉重的雙眼"
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

label cammove2:
    window auto hide
    camera:
        subpixel True blur 5.0
        parallel:
            ypos 0 
            linear 0.10 ypos -40 
            linear 0.10 ypos 0 
            linear 0.10 ypos 40 
            linear 0.10 ypos 0 
        parallel:
            xpos 0 zpos 0.0 
            linear 0.30 zpos -400.0 
        parallel:
            blur 1.0 
            linear 0.30 blur 10.0 
    with Pause(0.35)
    return

label revcam2:
    camera:
        linear 0.3 pos (0, 0) zpos 0.0 
        linear 0.35 blur 0.0
    with Pause(0.3)
    return
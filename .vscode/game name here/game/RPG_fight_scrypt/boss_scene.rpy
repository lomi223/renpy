label boss_fight:
    default end = False
    $ quick_menu = False
    scene boss_scene:
        xanchor 0.17
        yanchor 0.30
        zoom 2
    stop music
    play music "bergentrückung--asgore---epic-orchestral-cover--kāru.mp3" loop fadein 0.5    
    
    
    call ResetCam
    show floor
    show tse idle:
        subpixel True 
        pos (-1, 0.4) zpos -700.0 
    show ww idle:
        subpixel True 
        pos (-1, 0.65) zpos -700.0 
    show pr idle:
        subpixel True xpos 0.9 ypos 450 zpos -700.0
    camera:
        subpixel True zpos 0.0 
    show floor:
        subpixel True 
        yanchor 0.5 zoom 15.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(85.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show tse idle:
        subpixel True
        xpos -1.0 
        easein_back 0.60 xpos -0.25
    show ww idle:
        subpixel True 
        parallel:
            xpos -1.0 
            easein_back 0.80 xpos -0.2 
    with Pause(0.90)
    show tse idle:
        pos (-0.25, 0.4) 
    show ww idle:
        pos (-0.2, 0.65) 

    call initialize
    call StateDisplay

    pr "來了嗎？"
    pr "我很欣賞你們的能力"
    pr "居然能躲過教官們的視線翻出牆外"
    pr "但很可惜"
    pr "你們的旅途到此為止！"
    "試著說服校長吧！"

    jump the_fight

label the_fight:
    while True:
        call check
        call ResetCam
        call Relocate
        if mc.hp > 0 and mc_canmove == True:
            "[player]的回合！"
            call tseIdleCam
            call dice
            call mc_attack
        call ResetCam
        call Relocate
        if principal.hp < 0 or (mc.hp <= 0 and winwin.hp <= 0):
            jump CheckWL
        if winwin.hp > 0 and winwin_canmove == True:
            "[ww]的回合！"
            call wwIdleCam
            call dice
            call ww_attack
        call ResetCam
        call Relocate
        if principal.hp < 0 or (mc.hp <= 0 and winwin.hp <= 0):
            jump CheckWL
        if principal.hp > 0:
            call dice
            "校長的回合！"
            call boss_attack
        call ResetCam
        call Relocate
        if principal.hp < 0 or (mc.hp <= 0 and winwin.hp <= 0):
            jump CheckWL
        if Rh.hp > 0:
            call dice
            "右手的回合！"
            call Rh_attack
        call ResetCam
        call Relocate
        if principal.hp < 0 or (mc.hp <= 0 and winwin.hp <= 0):
            jump CheckWL
        if Lh.hp > 0:
            call dice
            "左手的回合！"
            show Lh heal
            call Lh_attack
        call ResetCam
        call Relocate
        if principal.hp < 0 or (mc.hp <= 0 and winwin.hp <= 0):
            jump CheckWL
        $ rd += 1
    return

label StateDisplay:
    
    show screen player_state
    show screen enemy_state
    
    return

label player_lost:
    scene black with dissolve
    "玩家失敗"
    return

label norm_win:
    scene black with dissolve
    "勝利"
    return
    
label perfect_win:
    scene black with dissolve
    "完美勝利"
    return

label tseIdleCam:
    window auto hide
    camera:
        subpixel True 
        pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
        linear 0.50 pos (-280, -200) zpos -200.0 xrotate 7.0 yrotate 0.0 zrotate 5.0 
    with Pause(0.60) 
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label wwIdleCam:
    window auto hide
    camera:
        subpixel True 
        pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
        linear 0.50 pos (-280, 200) zpos -200.0 xrotate 7.0 yrotate 0.0 zrotate 5.0 
    with Pause(0.60) 
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label tseAtkPrCam:
    window auto hide
    camera:
        subpixel True 
        pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
        linear 0.30 pos (280, -200) zpos -300.0 xrotate 18.0 yrotate -9.0 zrotate -9.0 
    show tse atk:
        subpixel True 
        parallel:
            'tse idle'
            0.30
            'tse atk'
        parallel:
            pos (-0.25, 0.4) zpos -700.0 
            linear 0.10 pos (0.6, 0.4) zpos -500.0 
    with Pause(0.70)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label tseAtkLhRhCam:
    window auto hide
    camera:
        subpixel True 
        linear 0.30 pos (280, 100) zpos -400.0 xrotate 9.0 yrotate -18.0 zrotate -18.0 
    show tse atk:
        subpixel True zpos -700.0 
        parallel:
            'tse idle'
            0.30
            'tse atk'
        parallel: 
            linear 0.30 pos (0.65, 0.6) 
    with Pause(0.40)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label wwAtkPrCam:
    window auto hide
    camera:
        subpixel True 
        pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
        linear 0.30 pos (280, -200) zpos -300.0 xrotate 18.0 yrotate -9.0 zrotate -9.0 
    show ww atk:
        subpixel True 
        parallel:
            'ww idle'
            0.30
            'ww atk'
        parallel:
            pos (-0.2, 0.65) zpos -700.0 
            linear 0.10 pos (0.6, 0.4) zpos -500.0 
    with Pause(0.70)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label wwAtkLhRhCam:
    window auto hide
    camera:
        subpixel True 
        linear 0.30 pos (280, 100) zpos -400.0 xrotate 9.0 yrotate -18.0 zrotate -18.0 
    show ww atk:
        subpixel True zpos -700.0 
        parallel:
            'ww idle'
            0.30
            'ww atk'
        parallel:
            linear 0.30 pos (0.65, 0.6) 
    with Pause(0.40)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label tseCheerCam: 
    window auto hide
    camera:
        linear 0.30 xpos -1100 zpos -700.0 xrotate 9.0 yrotate -18.0 zrotate 0.0 
    show tse cheer:
        subpixel True 
        'tse idle'
        0.30
        'tse cheer'
    with Pause(0.90)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label tseChillCam: 
    window auto hide
    camera:
        linear 0.30 xpos -1100 zpos -700.0 xrotate 9.0 yrotate -18.0 zrotate 0.0 
    show tse chill:
        subpixel True 
        'tse idle'
        0.30
        'tse chill'
    with Pause(0.90)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label wwShineCam:
    window auto hide
    camera:
        subpixel True
        linear 0.30 xpos -1000 zpos -700.0 xrotate 9.0 yrotate -9.0 zrotate -18.0 
    show ww shine:
        subpixel True 
        'ww idle'
        0.30
        'ww shine'
    with Pause(0.90)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label wwDefCam:
    window auto hide
    camera:
        subpixel True
        linear 0.30 xpos -1000 zpos -700.0 xrotate 9.0 yrotate -9.0 zrotate -18.0 
    show ww def:
        subpixel True 
        'ww idle'
        0.30
        'ww def'
        linear 0.29 pos (-0.1, 0.5) 
    with Pause(0.90)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label wwGuoinnCam:
    window auto hide
    camera:
        subpixel True
        linear 0.30 xpos -1000 zpos -700.0 xrotate 9.0 yrotate -9.0 zrotate -18.0 
    show ww guoinn:
        subpixel True 
        'ww idle'
        0.30
        'ww guoinn' 
    with Pause(0.90)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label prAtkTseCam:
    window auto hide
    camera:
        subpixel True 
        linear 0.30 pos (-350, -300) zpos -300.0 xrotate 18.0 yrotate 9.0 zrotate 0.0 
    show pr sing_atk:
        subpixel True 
        parallel:
            'pr idle'
            0.30
            'pr sing_atk'
        parallel:
            pos (0.9, 450) 
            linear 0.30 pos (-0.08, 400) 
    show tse hurt:
        'tse idle'
        0.30
        'tse hurt'
    with Pause(0.90)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label prAtkWwCam:
    camera:
        subpixel True 
        linear 0.30 pos (-450, 350) zpos -300.0 xrotate -9.0 yrotate 0.0 zrotate -9.0
    if not winwin_taunt:
        show pr sing_atk:
            subpixel True
            parallel:
                'pr idle'
                0.30
                'pr sing_atk'
            parallel:
                pos (0.9, 450) 
                linear 0.30 pos (0.05, 600) zpos -400 
        show ww hurt:
            'ww idle'
            0.30
            'ww hurt'
    elif winwin_taunt:
        show pr sing_atk:
            subpixel True
            parallel:
                'pr idle'
                0.30
                'pr sing_atk'
            parallel:
                pos (0.9, 450) 
                linear 0.30 pos (0.15, 450) zpos -400 
        show ww hurt:
            'ww idle'
            0.30
            'ww hurt'
    with Pause(0.90)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label prSummonLhCam:
    window auto hide
    camera:
        subpixel True 
        pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
        linear 0.30 pos (100, 100) zpos -200.0 xrotate 4.0 yrotate -4.0 zrotate -2.0 
    show Lh idle:
        default
        subpixel True 
        parallel:
            xpos 3000 
            easein_back 0.80 xpos 1900 
        parallel:
            ypos 1300 zpos -700.0 
            linear 0.80 ypos 1300 zpos -700.0 
    with Pause(0.90)
    camera:
        linear 0.1 subpixel True pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label prMulAtkCam:
    
    window auto hide
    camera:
        subpixel True 
        linear 0.30 pos (-300, -50) zpos -700.0 xrotate 18.0 yrotate 12.0 zrotate 0.0 
    show pr multi_atk:
        subpixel True 
        parallel:
            'pr idle'
            0.30
            'pr multi_atk'
        parallel:
            xpos 0.9 zpos -700.0 
            linear 0.30 xpos 0.05 zpos -400.0 
    show ww hurt:
            'ww idle'
            0.30
            'ww hurt'
    show tse hurt:
        'tse idle'
        0.30
        'tse hurt'
    with Pause(1.75)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label prAngerCam:
    window auto hide
    camera:
        subpixel True 
        linear 0.30 xpos 1000 zpos -500.0 xrotate 12.0 yrotate 10.0 zrotate 9.0 
    show pr anger:
        subpixel True 
        'pr idle'
        0.30
        'pr anger'
    with Pause(0.40)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label tseRetreat:
    show tse idle:
        subpixel True
        bop_out_time_warp 0.60 xpos -2000
    hide tse
    return

label wwRetreat:
    show ww idle:
        subpixel True
        bop_out_time_warp 0.60 xpos -2000
    hide ww
    return

label LhRetreat:
    window auto hide
    show Lh idle:
        subpixel True  
        bop_out_time_warp 0.60 xpos 3000 
    with Pause(0.70)
    hide Lh
    return

label ResetCam:
    camera:
        linear 0.1 subpixel True pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label Relocate:
    show tse idle
    show ww idle
    if mc.hp > 0:
        $ tseshown = True
        show tse idle:
            linear 0.1 pos (-0.25, 0.4) zpos -700.0 
    if mc.hp < 0:
        $ tseshown = False
        call tseRetreat
    if winwin.hp > 0:
        $ wwshown = True
        if wwrelocate:
            show ww idle:
                linear 0.1 pos (-0.2, 0.65) zpos -700.0 
    if winwin.hp < 0:
        $ wwshown = False
        call wwRetreat
    if principal.hp > 0:
        show pr idle:
            linear 0.1 subpixel True xpos 0.9 ypos 450 zpos -700.0 
    if Lh.hp > 0:
        $ Lhshown = True
        show Lh idle
    elif Lh.hp < 0 and Lhshown:
        $ Lhshown = False
        call LhRetreat
    return

label CheckWL:
    hide screen player_state
    hide screen enemy_state
    stop music fadeout 0.3
    if mc.hp <= 0 and winwin.hp <= 0:
        jump player_lost
    if principal.hp < 0 and (mc.hp > 0 and winwin.hp <= 0) or (mc.hp <= 0 and winwin.hp > 0):
        jump norm_win
        pr "咳......咳......"
        $ renpy.pause(3.0, hard=True)
        pr "我......認可你們"
        $ renpy.pause(3.0, hard=True)
    if principal.hp < 0 and mc.hp > 0 and winwin.hp > 0:
        jump perfect_win
        pr "咳......咳......"
        $ renpy.pause(3.0, hard=True)
        pr "我......認可你們"
        $ renpy.pause(3.0, hard=True)
    $ end = True
    return
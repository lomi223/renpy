label boss_fight:
    default end = False
    $ quick_menu = False
    scene boss_scene with dissolve:
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
    "成就：共患難"
    jump lose

label norm_win:
    scene black with dissolve
    "成就：險象環生"
    jump win
    
label perfect_win:
    scene black with dissolve
    "成就：欸！小恙"
    jump win

#cheats for testing
label heal:
    $ mc.hp = mc.max_hp
    $ winwin.hp = winwin.max_hp
    call StateDisplay
    return

label OnePunch:
    $ mc.max_attack = mc.max_attack * 1000
    $ winwin.max_attack = winwin.max_attack * 1000
    $ mc.attack = mc.max_attack
    $ winwin.attack = winwin.max_attack
    play sound "SFX/one-punch.mp3"
    call StateDisplay
    return

label DEF:
    $ mc.max_defence = mc.max_defence * 1000
    $ winwin.max_defence = winwin.max_defence * 1000
    $ mc.defence = mc.max_defence
    $ winwin.defence = winwin.max_defence
    call StateDisplay
    return

label OverFlowTP:
    $ mc.max_thoughts = mc.max_thoughts * 1000
    $ winwin.max_thoughts = winwin.max_thoughts * 1000
    $ mc.thoughts = mc.max_thoughts
    $ winwin.thoughts = winwin.max_thoughts
    call StateDisplay
    return

label ResetTimmer:
    $ winwin_defdebufftimmer = -1
    $ winwin_brighttimmer = -1
    $ mc_atkbufftimmer = -1
    $ mc_defbufftimmer = -1
    $ mc_attackbuffcd = -1
    $ winwin_brightcd = -1
    $ winwin_debuffcd = -1
    call StateDisplay
    return

label win:
    scene classroom with dissolve
    show w norm with dissolve:
        zoom 0.9
        xalign 0.5
        yalign 1.0
    w "剛剛還真是驚險"
    w "你還好嗎，哥們？"
    jump ok

label lose:
    scene classroom with dissolve
    show w norm with dissolve:
        zoom 0.9
        xalign 0.5
        yalign 1.0
    w "哎呀，吃了一支大過"
    w "你還好嗎，哥們？"
    jump ok

label ok:
    menu:
        "我沒事":
            w "沒事就好"
        "差點就沒啦":
            w "這樣啊"
            scene black with dissolve
            "勝勝突然靠近 舔了一下你的傷口"
            centered "沒有CG QAQ"
            player "！？"
            scene classroom with dissolve
            show w chill with dissolve:
                zoom 0.9
                xalign 0.5
                yalign 1.0
            w "聽說這樣會好比較快"
        "謝謝你，[ww]":
            show w shy
            w "你沒事就好"
    scene black with dissolve
    jump day4
            
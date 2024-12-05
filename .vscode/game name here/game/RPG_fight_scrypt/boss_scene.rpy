label boss_fight:
    $ ww = "勝勝" 

    stop music
    play music "bergentrückung--asgore---epic-orchestral-cover--kāru.mp3" loop fadein 0.5

    call initialize
    call StateDisplay
    show floor:
        default
        subpixel True matrixtransform ScaleMatrix(10.0, 1.0, 7.0)*OffsetMatrix(0.0, 500.0, -100.0)*RotateMatrix(72.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

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

        if mc.hp > 0 and mc_canmove == True:
            "[player]的回合！"
            call dice
            call mc_attack
            
        if winwin.hp > 0 and winwin_canmove == True:
            "[ww]的回合！"
            call dice
            call ww_attack

        if principal.hp > 0:
            call dice
            "校長的回合！"
            call boss_attack

        if Rh.hp > 0:
            call dice
            "右手的回合！"
            call Rh_attack

        if Lh.hp > 0:
            call dice
            "左手的回合！"
            call Lh_attack
        
        $ rd += 1
        if principal.hp < 0 or (mc.hp <= 0 and winwin.hp <= 0):
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
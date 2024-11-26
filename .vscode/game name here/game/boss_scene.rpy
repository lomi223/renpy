label boss_fight:
    $ ww = "勝勝" 

    call initialize

    show boss_scene with dissolve:
        subpixel True 
    "試著說服校長吧！"
    call state_upd
    jump the_fight

label the_fight:
    
    while True:

        call check

        if mc.hp > 0 and mc_canmove == True:
            "[player]的回合！"
            call dice
            call mc_attack
        elif mc_canmove == False:
            $ mc_canmove = True
            
        if winwin.hp > 0 and winwin_canmove == True:
            "[ww]的回合！"
            call dice
            call ww_attack
        elif winwin_canmove == False:
            $ winwin_canmove = True

        if principal.hp > 0:
            "校長的回合！"
            call dice
            call boss_attack
    
    return

label mc_attack:
    show screen player_state

    call screen mc_attackchoice

    call state_upd
    return

label ww_attack:
    show screen player_state
    menu:

        "以理服人":
            hide screen winwin_state
            if d10 > 8:
                "勝勝的理由強而有力！"
                $ atk = (d4 + d6)*2 + winwin.attack*3 - principal.defence
                $ principal.hp -= atk
                call state_upd
                return

            if d10 > 6:
                "勝勝說了個強大的理由"
                $ atk = d4 + d6 + winwin.attack*2 - principal.defence
                $ principal.hp -= atk
                call state_upd
                return

            if d10 > 1:
                "勝勝說了個普通的理由"
                $ atk = d4 + winwin.attack*2 - principal.defence
                $ principal.hp -= atk
                call state_upd
                return

            if d10 == 1:
                "勝勝的理由爛透了！"
                call state_upd
                return

        "嘴砲 - 2 靈感" if winwin_defdebufftimmer <= 0 and winwin.thoughts >= 2:
            hide screen winwin_state
            if d10 == 10:
                "勝勝把校長說破防了！"
                $ principal.defence = 0
                $ principal_break = True
                $ winwin_defdebufftimmer = 3
                $ winwin.thoughts -= 2
                $ principal.hp -= d4
                call state_upd
                return
            
            if d10 > 3:
                "校長的心理防線受到勝勝影響"
                $ principal.defence -= 2
                $ winwin_defdebufftimmer = 3
                $ winwin.thoughts -= 2
                $ principal.hp -= d4
                call state_upd
                return

            if d10 <= 3:
                "勝勝的話語意外地激怒了校長！"
                $ principal.attack += 2
                $ principal_angered = True
                $ winwin_defdebufftimmer = 3
                $ winwin.thoughts -= 2
                call state_upd
                return

        "我來扛":
            hide screen winwin_state
            "勝勝擋在了[player]的前面"
            $ winwin_taunt = True

        "陽光開朗大男孩":
            hide screen winwin_state
            "勝勝開始發光發熱"
            "校長被閃瞎了"
            "勝勝受到灼傷"
            $ winwin_bright = True
            $ winwin_brighttimmer = 3

        "休息":
            hide screen winwin_state
            "勝勝選擇休息一會兒，回復些許靈感"
            $ winwin.thoughts += 1
            if winwin.thoughts > winwin.max_thoughts:
                $ winwin.thoughts = winwin.max_thoughts
    call state_upd
    return

label boss_attack:

    if d100 > 75:
        call choose1
        if selected_player == 1:
            "校長對[player]使用記大過"
            if winwin_bright == False:

                if d20 >= 19:
                    "效果顯著"
                    $ atk = d4 + d6 + principal.attack*2 - mc.defence
                    $ mc.hp -= atk
                if d20 >=1:
                    "成效普通"
                    $ atk = d4 + principal.attack*2 - mc.defence
                    $ mc.hp -= atk
                if d20 == 1:
                    "未命中"
                return

            if winwin_bright == True:
                if d20 == 20:
                    "成效普通"
                    $ atk = d4 + principal.attack*2 - mc.defence
                    $ mc.hp -= atk
                if d20 <= 19:
                    "未命中"
                return   

        if selected_player == 2:
            "校長對[ww]使用記大過"
            if winwin_bright == False:

                if d20 >= 19:
                    "效果顯著"
                    $ atk = d4 + d6 + principal.attack*2 - winwin.defence
                    $ winwin.hp -= atk
                if d20 >=1:
                    "成效普通"
                    $ atk = d4 + principal.attack*2 - winwin.defence
                    $ winwin.hp -= atk
                if d20 == 1:
                    "未命中"
                return

            if winwin_bright == True:
                if d20 == 20:
                    "成效普通"
                    $ atk = d4 + principal.attack*2 - winwin.defence
                    $ winwin.hp -= atk
                if d20 <= 19:
                    "未命中"
                return

    if d100 > 60:
        call choose2
        "校長使用禁言"
        if selected_player == 1:
            $ mc_canmove = False
            "[player]被禁言了"
            return
        if selected_player == 2:
            $ winwin_canmove = False
            "[ww]被禁言了"
            return    
    
    
    
    return


label dice:
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d10 = renpy.random.randint(1, 10)
    $ d20 = renpy.random.randint(1, 20)
    $ d50 = renpy.random.randint(1, 50)
    $ d100 = renpy.random.randint(1,100)
    return

label state_upd:

    $ mc_currhp = mc.hp
    $ mc_currthoughts = mc.thoughts
    $ mc_currdefence = mc.defence
    $ mc_currattack = mc.attack

    $ winwin_currhp = winwin.hp
    $ winwin_currthoughts = winwin.thoughts
    $ winwin_currdefence = winwin.defence
    $ winwin_currattack = winwin.attack

    $ boss_currhp = principal.hp    
    $ boss_currthoughts = principal.thoughts
    $ boss_currdefence = principal.defence
    $ boss_currattack = principal.attack

    return

label choose1:
    if winwin_taunt == False:
        if mc_buffed:
            if d50 >= 28:
                $ selected_player = 1
            elif d50 <= 27:
                $ selected_player = 2
        elif winwin_buffed:
            if d50 >= 24:
                $ selected_player = 1
            elif d50 <= 23:
                $ selected_player = 2
        else:
            if d50 >= 26:
                $ selected_player = 1
            elif d50 <= 25:
                $ selected_player = 2
    elif winwin_taunt == True:
        $ selected_player = 2
    return

label choose2:
    if winwin_taunt == False:
        if mc_atkbufftimmer > 0:
            if d50 >= 31:
                $ selected_player = 1
            elif d50 <= 30:
                $ selected_player = 2
        else:
            if d50 >= 26:
                $ selected_player = 1
            elif d50 <= 25:
                $ selected_player = 2
    elif winwin_taunt == True:
        $ selected_player = 2
    return 

label check:

    if mc_atkbufftimmer > 0:
            $ mc_atkbufftimmer -= 1
        
    if mc_defbufftimmer > 0:
        $ mc_defbufftimmer -= 1

    if winwin_defdebufftimmer > 0:
        $ winwin_defdebufftimmer -= 1
    
    if winwin_brighttimmer > 0:
        $ winwin_brighttimmer -= 1
        $ winwin.hp -= 1

    if mc_atkbufftimmer == 0:
        $ mc.attack -= 2
        $ winwin.attack -= 2
        "加油的效果結束了！"
        $ mc_atkbufftimmer = -1

    if mc_defbufftimmer == 0:

        "沒事的的效果結束了！"

        if mc_buffed == True:
            $ mc.defence -= 2
            $ mc_buffed = False

        if winwin_buffed == True:
            $ winwin.defence -= 2
            $ winwin_buffed = False

        $ mc_defbufftimmer = -1

    if winwin_defdebufftimmer == 0:
        "嘴砲的效果結束了！"
        if principal_break == True:
            $ principal.defence = principal.max_defence
            $ principal_break = False
        
        elif principal_angered == True:
            $ principal.attack -= 2
            $ principal_angered = False

        else:
            $ principal.defence += 2
            
        $ winwin_defdebufftimmer = -1

    if winwin_brighttimmer == 0:
        "陽光開朗大男孩的效果結束了！"
        $ winwin_bright = False
        $ winwin_brighttimmer = -1

    return

label initialize:
    #(name,Mhp,hp,Mmp,mp,Mdef,def,Matk,atk)
    $ mc = fighter("[player]", 60, 60, 30, 30, 8, 8, 3, 3)
    $ winwin = fighter("[ww]", 80, 80, 10, 10, 10, 10, 5, 5)
    $ principal = fighter("校長", 200, 200, 50, 50, 5, 5, 8, 8)

    $ food = 3
    $ atk = 0
    $ winwin_defdebufftimmer = -1
    $ winwin_brighttimmer = -1
    $ mc_atkbufftimmer = -1
    $ mc_defbufftimmer = -1
    
    $ selected_player = -1
    
    $ mc_buffed = False
    $ winwin_buffed = False

    $ principal_break = False
    $ principal_angered = False
    $ winwin_taunt = False
    $ winwin_bright = False

    $ mc_canmove = True
    $ winwin_canmove = True

    $ mc.hp = mc.max_hp
    $ mc.thoughts = mc.max_thoughts
    $ mc.defence = mc.max_defence
    $ mc.max_attack = mc.max_attack

    $ winwin.hp = winwin.max_hp
    $ winwin.thoughts = winwin.max_thoughts
    $ winwin.defence = winwin.max_defence
    $ winwin.max_attack = winwin.max_attack

    $ principal.hp = principal.max_hp
    $ principal.thoughts = principal.max_thoughts
    $ principal.defence = principal.max_defence
    $ principal.max_attack = principal.max_attack
    return
    

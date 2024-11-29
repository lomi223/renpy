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
    return

label mc_attack:

    call screen mc_attackchoice

    call StateDisplay

    call state_upd
    return

label ww_attack:

    call screen ww_attackchoice
    
    call StateDisplay

    call state_upd
    return

label boss_attack:

    call StateDisplay

    if d100 > 75:
        call choose1
        if selected_player == 1:
            "校長對[player]使用記大過"
            if winwin_bright == False:

                if d20 >= 19:
                    "效果顯著"
                    $ atk = d4 + d6 + principal.attack*2 - mc.defence
                    if atk < 0:
                        $ atk = 0
                    $ mc.hp -= atk
                    call StateDisplay
                    return
                if d20 >=1:
                    "成效普通"
                    $ atk = d4 + principal.attack*2 - mc.defence
                    if atk < 0:
                        $ atk = 0
                    $ mc.hp -= atk
                    call StateDisplay
                    return
                if d20 == 1:
                    "未命中"
                    return

            if winwin_bright == True:
                if d20 == 20:
                    "成效普通"
                    $ atk = d4 + principal.attack*2 - mc.defence
                    if atk < 0:
                        $ atk = 0
                    $ mc.hp -= atk
                    call StateDisplay
                    return
                if d20 <= 19:
                    "未命中"
                    return   

        if selected_player == 2:
            "校長對[ww]使用記大過"
            if winwin_bright == False:

                if d20 >= 19:
                    "效果顯著"
                    $ atk = d4 + d6 + principal.attack*2 - winwin.defence
                    if atk < 0:
                        $ atk = 0
                    $ winwin.hp -= atk
                    call StateDisplay
                    return
                if d20 >=1:
                    "成效普通"
                    $ atk = d4 + principal.attack*2 - winwin.defence
                    if atk < 0:
                        $ atk = 0
                    $ winwin.hp -= atk
                    call StateDisplay
                    return
                if d20 == 1:
                    "未命中"
                    return

            if winwin_bright == True:
                if d20 == 20:
                    "成效普通"
                    $ atk = d4 + principal.attack*2 - winwin.defence
                    if atk < 0:
                        $ atk = 0
                    $ winwin.hp -= atk
                    call StateDisplay
                    return
                if d20 <= 19:
                    "未命中"
                return

    if d100 > 60:
        call choose2
        "校長使用禁言"
        if selected_player == 1:
            $ mc_canmove = False
            "[player]被禁言了"
            $ cantmove = 2
            $ mc_effects.append("q")
            $ mc_effectamount += 1
            return
        if selected_player == 2:
            $ winwin_canmove = False
            "[ww]被禁言了"
            $ cantmove = 2
            $ ww_effects.append("q")
            $ ww_effectamount += 1
            return    

    if d100 > 55 and summoned == False and rd > 2:
        "校長招喚了右手"
        $ Rh.hp = Rh.max_hp
        $ summoned = True
        return

    if d100 > 50 and summoned == False and rd > 2:
        "校長招喚了左手"
        $ Lh.hp = Lh.max_hp
        $ summoned = True
        return
        
    call dice
    call boss_attack
    return

label Rh_attack:
    
    call StateDisplay
    call choose1
    if selected_player == 1:
        "右手對[player]使用正面突襲"
        if winwin_bright == False:

            if d20 >= 19:
                "效果顯著"
                $ atk = d4 + d6 + Rh.attack - mc.defence
                if atk < 0:
                    $ atk = 0
                $ mc.hp -= atk
                call StateDisplay
                return
            if d20 >=1:
                "成效普通"
                $ atk = d4 + Rh.attack - mc.defence
                if atk < 0:
                    $ atk = 0
                $ mc.hp -= atk
                call StateDisplay
                return
            if d20 == 1:
                "未命中"
                return

        if winwin_bright == True:
            if d20 == 20:
                "成效普通"
                $ atk = d4 + Rh.attack - mc.defence
                if atk < 0:
                    $ atk = 0
                $ mc.hp -= atk
                call StateDisplay
                return
            if d20 <= 19:
                "未命中"
                return   

    if selected_player == 2:
        "右手對[ww]使用正面突襲"
        if winwin_bright == False:

            if d20 >= 19:
                "效果顯著"
                $ atk = d4 + d6 + Rh.attack - winwin.defence
                if atk < 0:
                    $ atk = 0
                $ winwin.hp -= atk
                call StateDisplay
                return
            if d20 >=1:
                "成效普通"
                $ atk = d4 + Rh.attack - winwin.defence
                if atk < 0:
                    $ atk = 0
                $ winwin.hp -= atk
                call StateDisplay
                return
            if d20 == 1:
                "未命中"
                return

        if winwin_bright == True:
            if d20 == 20:
                "成效普通"
                $ atk = d4 + Rh.attack - winwin.defence
                if atk < 0:
                    $ atk = 0
                $ winwin.hp -= atk
                call StateDisplay
                return
            if d20 <= 19:
                "未命中"
            return
    
    return

label Lh_attack:
    
    call StateDisplay
    "左手對校長使用了回復"
    $ principal.hp += 5
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

    $ Rh_currhp = Rh.hp    
    $ Rh_currthoughts = Rh.thoughts
    $ Rh_currdefence = Rh.defence
    $ Rh_currattack = Rh.attack

    return

label choose1:
    if winwin_taunt == True and winwin.hp > 0:
        $ selected_player = 2
    elif winwin_taunt == False:
        if mc_buffed:
            if d50 >= 28 and mc.hp > 0:
                $ selected_player = 1
            elif d50 <= 27 and winwin.hp > 0:
                $ selected_player = 2
            elif winwin.hp > 0:
                $ selected_player = 2
            else:
                $ selected_player = 1
        elif winwin_buffed:
            if d50 >= 24 and mc.hp > 0:
                $ selected_player = 1
            elif d50 <= 23 and winwin.hp > 0:
                $ selected_player = 2
            elif winwin.hp > 0:
                $ selected_player = 2
            else:
                $ selected_player = 1
        else:
            if d50 >= 26 and mc.hp > 0:
                $ selected_player = 1
            elif d50 <= 25 and winwin.hp > 0:
                $ selected_player = 2
            elif winwin.hp > 0:
                $ selected_player = 2
            else:
                $ selected_player = 1
    return

label choose2:
    if winwin_taunt == True and winwin.hp > 0:
        $ selected_player = 2
    elif winwin_taunt == False:
        if mc_atkbufftimmer > 0:
            if d50 >= 31 and mc.hp > 0:
                $ selected_player = 1
            elif d50 <= 30 and winwin.hp > 0:
                $ selected_player = 2
            elif winwin.hp > 0:
                $ selected_player = 2
            else:
                $ selected_player = 1
        else:
            if d50 >= 26 and mc.hp > 0:
                $ selected_player = 1
            elif d50 <= 25 and winwin.hp > 0:
                $ selected_player = 2
            elif winwin.hp > 0:
                $ selected_player = 2
            else:
                $ selected_player = 1
    return 

label check:

    if cantmove > 0:
        $ cantmove -= 1

    if Rh.hp <= 0:
        $ summoned = False
        
    if mc_attackbuffcd > 0:
        $ mc_attackbuffcd -= 1

    if winwin_debuffcd > 0:
        $ winwin_debuffcd -= 1

    if winwin_brightcd > 0:
        $ winwin_brightcd -= 1

    if mc_atkbufftimmer > 0:
        $ mc_atkbufftimmer -= 1
        
    if mc_defbufftimmer > 0:
        $ mc_defbufftimmer -= 1

    if winwin_defdebufftimmer > 0:
        $ winwin_defdebufftimmer -= 1
    
    if winwin_brighttimmer > 0:
        $ winwin_brighttimmer -= 1
        $ winwin.hp -= 1

    if mc_attackbuffcd == 0:
        "技能：加油 冷卻結束"
        $ mc_attackbuffcd = -1

    if mc_atkbufftimmer == 0:
        $ mc.attack -= 2
        $ winwin.attack -= 2
        $ mc_effectamount -= 1
        $ mc_effects.remove("a")
        $ ww_effectamount -= 1
        $ ww_effects.remove("a")
        "加油的效果結束了！"
        $ mc_atkbufftimmer = -1

    if mc_defbufftimmer == 0:

        "沒事的的效果結束了！"

        if mc_buffed == True:
            $ mc.defence -= 2
            $ mc_buffed = False
            $ mc_effectamount -= 1
            $ mc_effects.remove("h")

        if winwin_buffed == True:
            $ winwin.defence -= 2
            $ winwin_buffed = False
            $ ww_effectamount -= 1
            $ ww_effects.remove("h")


        $ mc_defbufftimmer = -1

    if winwin_defdebufftimmer == 0:
        "嘴砲的效果結束了！"
        if principal_break == True:
            $ principal.defence = principal.max_defence
            $ principal_break = False
            $ boss_effectamount -= 1
            $ Rh_effectamount -= 1
            $ Lh_effectamount -= 1
            $ Lh_effects.remove("nd")
            $ Rh_effects.remove("nd")
            $ boss_effects.remove("nd")

        elif principal_angered == True:
            $ principal.attack -= 2
            $ Rh.attack -= 2
            $ Lh.attack -= 2
            $ principal_angered = False
            $ boss_effectamount -= 1
            $ Rh_effectamount -= 1
            $ Lh_effectamount -= 1
            $ Lh_effects.remove("a")
            $ Rh_effects.remove("a")
            $ boss_effects.remove("a")

        else:
            $ principal.defence += 2
            $ boss_effectamount -= 1
            $ Rh_effectamount -= 1
            $ Lh_effectamount -= 1
            $ Lh_effects.remove("rd")
            $ Rh_effects.remove("rd")
            $ boss_effects.remove("rd")
        $ winwin_defdebufftimmer = -1

    if winwin_brighttimmer == 0:
        "陽光開朗大男孩的效果結束了！"
        $ winwin_bright = False
        $ winwin_brighttimmer = -1
        $ ww_effectamount -= 1
        $ boss_effectamount -= 1
        $ Rh_effectamount -= 1
        $ Lh_effectamount -= 1
        $ Lh_effects.remove("bl")
        $ Rh_effects.remove("bl")
        $ boss_effects.remove("bl")
        $ ww_effects.remove("b")

    if winwin_brightcd == 0:
        "技能：陽光開朗大男孩 冷卻結束"
        $ winwin_brightcd = -1

    if winwin_debuffcd == 0:
        "技能：嘴泡 冷卻結束"
        $ winwin_debuffcd = -1

    if winwin_taunt == True:
        $ winwin_taunt = False
        $ ww_effectamount -= 1
        $ ww_effects.remove("t")
    
    if cantmove == 0:
        $ cantmove = -1
        "禁言 效果結束"
        if mc_canmove == False:
            $ mc_canmove = True
            $ mc_effects.remove("q")
            $ mc_effectamount -= 1
        if winwin_canmove == False:
            $ winwin_canmove = True
            $ ww_effects.remove("q")
            $ ww_effectamount -= 1

    return

label initialize:

    #(name,Mhp,hp,Mmp,mp,Mdef,def,Matk,atk)
    $ mc = fighter("[player]", 50, 50, 30, 30, 8, 8, 3, 3)
    $ winwin = fighter("[ww]", 70, 70, 10, 10, 10, 10, 5, 5)
    $ principal = fighter("校長", 100, 100, 50, 50, 5, 5, 8, 8)
    $ Rh = fighter("右手", 15, 0, 5, 5, 0, 0, 20, 20)
    $ Lh = fighter("左手", 15, 0, 5, 5, 10, 10, 0, 0)

    call StateDisplay
    $ food = 3
    $ atk = 0
    $ winwin_defdebufftimmer = -1
    $ winwin_brighttimmer = -1
    $ mc_atkbufftimmer = -1
    $ mc_defbufftimmer = -1
    $ mc_attackbuffcd = -1
    $ winwin_brightcd = -1
    $ winwin_debuffcd = -1
    $ mc_effectamount = 0
    $ ww_effectamount = 0
    $ boss_effectamount = 0
    $ Rh_effectamount = 0
    $ Lh_effectamount = 0
    $ selected_player = -1
    $ cantmove = -1

    $ mc_buffed = False
    $ winwin_buffed = False

    $ principal_break = False
    $ principal_angered = False
    $ winwin_taunt = False
    $ winwin_bright = False

    $ mc_canmove = True
    $ winwin_canmove = True

    $ summoned = False

    $ rd = 0
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

    $ Rh.hp = 0
    $ Rh.thoughts = Rh.max_thoughts
    $ Rh.defence = Rh.max_defence
    $ Rh.max_attack = Rh.max_attack

    $ Lh.hp = 0
    $ Lh.thoughts = Lh.max_thoughts
    $ Lh.defence = Lh.max_defence
    $ Lh.max_attack = Lh.max_attack

    return
    
label StateDisplay:
    
    show screen player_state
    show screen enemy_state
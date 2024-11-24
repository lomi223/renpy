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

        if mc.hp > 0:
            "[player]的回合！"
            call dice
            call mc_attack

        if winwin.hp > 0:
            "[ww]的回合！"
            call dice
            call ww_attack

        if principal.hp > 0:
            "校長的回合！"
            call dice
            call boss_attack
    
    return

label mc_attack:
    show screen mc_state
    menu:

        "找藉口 - 1 靈感" if mc.thoughts >= 1:
            hide screen mc_state
            if d10 > 7:
                "[player]說了個強而有力的藉口！"
                "十分有效"
                $ atk = d4 + d6 + mc.attack*2 - principal.defence
                if atk < 0:
                    $ atk = 0
                $ principal.hp -= atk
                $ mc.thoughts -= 1
                call state_upd
                return

            if d10 > 1:
                "[player]說了個普通的藉口"
                $ atk = d4 + mc.attack*2 - principal.defence
                if atk < 0:
                    $ atk = 0
                $ principal.hp -= atk
                $ mc.thoughts -= 1
                call state_upd
                return
            
            if d10 == 1:
                "[player]的藉口爛透了！"
                call state_upd
                return
        
        "加油 - 2 靈感" if mc_atkbufftimmer <= 0 and mc.thoughts >=2:
            hide screen mc_state
            "[player]和勝勝的說服力上升了"
            $ mc.attack += 2
            $ winwin.attack += 2
            $ mc_atkbufftimmer = 2
            $ mc.thoughts -= 2

        "沒事的 - 3 靈感" if mc_defbufftimmer <= 0 and mc.thoughts >= 3:
            hide screen mc_state
            $ mc.thoughts -= 3
            $ mc_defbufftimmer = 1
            call healthsheild

        "吃外賣" if food > 0:
            hide screen mc_state
            $ food -= 1
            call eat

        "休息":
            hide screen mc_state
            "[player]選擇休息一會兒，回復些許靈感"
            $ mc.thoughts += 1
            if mc.thoughts > mc.max_thoughts:
                $ mc.thoughts = mc.max_thoughts
    
    call state_upd
    return

label ww_attack:
    show screen winwin_state
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
    return

label eat:
    menu:
        "給[player]吃":
            "[player]吃了一口外賣"
            "[player]充滿了靈感"
            $ mc.thoughts = mc.max_thoughts
        
        "給勝勝吃":
            "勝勝吃了一口你的外賣"
            "勝勝充滿了靈感"
            $ winwin.thoughts = winwin.max_thoughts
    if food == 0:
        "[player]的外賣被吃完了"

    return

label healthsheild:
    menu:
        "[player]":
            "[player]恢復了些許體力並為下一次的攻勢做好了準備"
            $ mc.hp += 5
            $ mc.defence += 2
            $ mc_buffed = True
            if mc.hp > mc.max_hp:
                $ mc.hp = mc.max_hp

        "勝勝":
            "勝勝恢復了些許體力並為下一次的攻勢做好了準備"
            $ winwin.hp += 5
            $ winwin.defence += 2
            $ winwin_buffed = True
            if winwin.hp > winwin.max_hp:
                $ winwin.hp = winwin.max_hp
    return

label dice:
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d10 = renpy.random.randint(1, 10)
    $ d20 = renpy.random.randint(1, 20)
    $ d50 = renpy.random.randint(1,50)
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
    $ mc = fighter("[player]", 60, 60, 30, 30, 10, 10, 3, 3)
    $ winwin = fighter("[ww]", 80, 80, 10, 10, 8, 8, 5, 5)
    $ principal = fighter("校長", 200, 200, 50, 50, 5, 5, 8, 8)

    $ food = 3
    $ atk = 0
    $ winwin_defdebufftimmer = -1
    $ winwin_brighttimmer = -1
    $ mc_atkbufftimmer = -1
    $ mc_defbufftimmer = -1
    
    $ mc_buffed = False
    $ winwin_buffed = False

    $ principal_break = False
    $ principal_angered = False
    $ winwin_taunt = False
    $ winwin_bright = False

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
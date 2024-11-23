label dice:
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d10 = renpy.random.randint(1, 10)
    $ d20 = renpy.random.randint(1, 20)
    return

label boss_fight:
    $ ww = "勝勝" 

    #(name,Mhp,hp,Mmp,mp,Mdef,def,Matk,atk)
    $ food = 3
    $ atk = 0
    $ mc_atkbufftimmer = -1
    $ mc_defbufftimmer = -1
    $ mc = fighter("[player]", 60, 60, 30, 30, 10, 10, 3, 3)
    $ winwin = fighter("[ww]", 80, 80, 10, 10, 8, 8, 5, 5)
    $ principal = fighter("校長", 200, 200, 50, 50, 5, 5, 8, 8)
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

    show boss_scene with dissolve:
        subpixel True 
    "試著說服校長吧！"
    jump the_fight

label the_fight:
    
    while True:

        if mc_atkbufftimmer > 0:
            $ mc_atkbufftimmer -= 1
        
        if mc_defbufftimmer > 0:
            $ mc_defbufftimmer -= 1

        if mc_atkbufftimmer == 0:
            $ mc.attack -= 2
            $ winwin.attack -= 2
            "加油的效果結束了！"
            $ mc_atkbufftimmer = -1

        if mc_defbufftimmer == 0:
            $ mc.attack -= 2
            $ winwin.attack -= 2
            "沒事的的效果結束了！"
            $ mc_defbufftimmer = -1

        if mc.hp > 0:
            "[player]的回合！"
            call dice
            call mc_attack


        if winwin.hp > 0:
            "[ww]的回合！"
            call dice
            call ww_attack

label mc_attack:
    menu:
        "找藉口 - 1 靈感" if mc.thoughts >= 1:
            if d10 > 7:
                "你說了個強而有力的藉口"
                "十分有效"
                $ atk = d4 + d6 + mc.attack*2 - principal.defence
                if atk < 0:
                    $ atk = 0
                $ principal.hp -= atk
                $ mc.thoughts -= 1
                return

            if d10 > 1:
                "你說了個普通的藉口"
                $ atk = d4 + mc.attack*2 - principal.defence
                if atk < 0:
                    $ atk = 0
                $ principal.hp -= atk
                $ mc.thoughts -= 1
                return
            
            if d10 == 1:
                "你的藉口爛透了！"
                return
        
        "加油 - 2 靈感" if mc_atkbufftimmer <= 0 and mc.thoughts >=2:
            "你和勝勝的說服力上升了"
            $ mc.attack += 2
            $ winwin.attack += 2
            $ mc_atkbufftimmer = 2
            $ mc.thoughts -= 2

        "沒事的 - 3 靈感" if mc_defbufftimmer <= 0 and mc.thoughts >= 3:
            $ mc.thoughts -= 3
            $ mc_defbufftimmer = 1
            call healthsheild

        "吃外賣" if food > 0:
            $ food -= 1
            call eat

    return

label ww_attack:
    ""
    return

label eat:
    menu:
        "給自己吃":
            "你吃了一口外賣"
            "你充滿了靈感"
            $ mc.thoughts = mc.max_thoughts
        
        "給勝勝吃":
            "勝勝吃了一口你的外賣"
            "勝勝充滿了靈感"
            $ winwin.thoughts = winwin.max_thoughts
    if food == 0:
        "你的外賣被吃完了"

    return

label healthsheild:
    menu:
        "自己":
            "你恢復了些許體力並為下一次的攻勢做好了準備"
            $ mc.hp += 5
            $ mc.defence += 2

        "勝勝":
            "勝勝恢復了些許體力並為下一次的攻勢做好了準備"
            $ winwin.hp += 5
            $ winwin.defence += 2
    
    return
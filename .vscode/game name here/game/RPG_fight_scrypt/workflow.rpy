label dice:
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d10 = renpy.random.randint(1, 10)
    $ d20 = renpy.random.randint(1, 20)
    $ d50 = renpy.random.randint(1, 50)
    $ d100 = renpy.random.randint(1,100)
    return

label check:

    if bosseffectcd > 0:
        $ bosseffectcd -= 1

    if bosseffectcd == 0:
        $ bosseffectcd = -1

    if bosseffecttimmer > 0:
        $ mc.hp -= 3
        $ winwin.hp -= 3
        $ mc.thoughts -= 3
        if mc.thoughts < 0:
            $ mc.thoughts = 0
        $ winwin.thoughts -= 3
        if winwin.thoughts < 0:
            $ winwin.thoughts = 0
        $ bosseffecttimmer -= 1

    if bosseffecttimmer == 0:
        "威嚴 的效果結束了"
        $ principal.attack -= 3
        $ mc.attack += 2
        $ winwin.attack += 2
        $ mc.defence += 2
        $ winwin.defence += 2

        $ boss_effectamount -= 1
        $ mc_effectamount -= 4
        $ ww_effectamount -= 4

        $ boss_effects.remove("a")
        $ mc_effects.remove("rd")
        $ mc_effects.remove("we")
        $ mc_effects.remove("wi")
        $ mc_effects.remove("rt")
        $ ww_effects.remove("rd")
        $ ww_effects.remove("we")
        $ ww_effects.remove("wi")
        $ ww_effects.remove("rt")
        $ bosseffecttimmer = -1

    if cantmove > 0:
        $ cantmove -= 1

    if Rh.hp <= 0 and Lh.hp <= 0 and summontimmer <= 0:
        $ summontimmer = 2  
        $ summoned = False

    if summontimmer > 0:
        $ summontimmer -= 1

    if Rh.hp > 0 or Lh.hp > 0:
        $ summoned = True

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
        $ wwrelocate = True
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
    $ principal = fighter("校長", 125, 125, 50, 50, 5, 5, 8, 8)
    $ Rh = fighter("右手", 15, 0, 5, 5, 0, 0, 20, 20)
    $ Lh = fighter("左手", 15, 0, 5, 5, 10, 10, 0, 0)

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
    $ summontimmer = -1

    $ wwrelocate = True
    $ tseshown = True
    $ wwshown = True
    $ prshown = True
    $ Rhshown = False
    $ Lhshown = False


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

    $ bosseffectcd = -1
    $ bosseffecttimmer = -1

    return
    





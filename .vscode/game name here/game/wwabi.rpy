label wwrest:
    "[ww]選擇休息一會兒，回復些許靈感"
    $ mc.thoughts += 1
    if mc.thoughts > mc.max_thoughts:
        $ mc.thoughts = mc.max_thoughts
    call state_upd
    return

label wwab1:
    if d10 > 8:
        "勝勝的理由強而有力！"
        if target == principal:
            $ atk = (d4 + d6)*2 + winwin.attack*3 - principal.defence
            if atk < 0:
                $ atk = 0
            $ principal.hp -= atk
        if target == Rh:
            $ atk = (d4 + d6)*2 + winwin.attack*3 - Rh.defence
            if atk < 0:
                $ atk = 0
            $ Rh.hp -= atk
        if target == Lh:
            $ atk = (d4 + d6)*2 + winwin.attack*3 - Lh.defence
            if atk < 0:
                $ atk = 0
            $ Lh.hp -= atk
        call state_upd
        return

    if d10 > 6:
        "勝勝說了個強大的理由"
        if target == principal:
            $ atk = d4 + d6 + winwin.attack*2 - principal.defence
            if atk < 0:
                $ atk = 0
            $ principal.hp -= atk
        if target == Rh:
            $ atk = d4 + d6 + winwin.attack*2 - Rh.defence
            if atk < 0:
                $ atk = 0
            $ Rh.hp -= atk
        if target == Lh:
            $ atk = d4 + d6 + winwin.attack*2 - Lh.defence
            if atk < 0:
                $ atk = 0
            $ Lh.hp -= atk
        call state_upd
        return

    if d10 > 1:
        "勝勝說了個普通的理由"
        if target == principal:
            $ atk = d4 + winwin.attack*2 - principal.defence
            if atk < 0:
                $ atk = 0
            $ principal.hp -= atk
        if target == Rh:
            $ atk = d4 + winwin.attack*2 - Rh.defence
            if atk < 0:
                $ atk = 0
            $ Rh.hp -= atk
        if target == Lh:
            $ atk = d4 + winwin.attack*2 - Lh.defence
            if atk < 0:
                $ atk = 0
            $ Lh.hp -= atk
        call state_upd
        return

    if d10 == 1:
        "勝勝的理由爛透了！"
        call state_upd
        return

label wwab2:
    "勝勝擋在了[player]的前面"
    $ winwin_taunt = True
    $ ww_effectamount += 1
    $ ww_effects.append("t")
    call state_upd
    return

label wwab3:
    "勝勝開始發光發熱"
    "對手被閃瞎了"
    "勝勝受到灼傷"
    $ winwin_bright = True
    $ winwin_brighttimmer = 3
    $ winwin_brightcd = 4
    $ ww_effectamount += 1
    $ boss_effectamount += 1
    $ Rh_effectamount += 1
    $ Lh_effectamount += 1
    $ Lh_effects.append("bl")
    $ Rh_effects.append("bl")
    $ boss_effects.append("bl")
    $ ww_effects.append("b")
    call state_upd
    return

label wwab4:
    if d10 == 10:
        "勝勝把對方說破防了！"
        $ principal.defence = 0
        $ principal_break = True
        $ winwin_defdebufftimmer = 3
        $ winwin.thoughts -= 2
        $ principal.hp -= d4
        $ Rh.hp -= d4
        $ Lh.hp -= d4
        $ winwin_debuffcd = 4
        $ boss_effectamount += 1
        $ Rh_effectamount += 1
        $ Lh_effectamount += 1
        $ Lh_effects.append("nd")
        $ Rh_effects.append("nd")
        $ boss_effects.append("nd")
        call state_upd
        return
    
    if d10 > 3:
        "對方的心理防線受到勝勝影響"
        $ principal.defence -= 2
        $ winwin_defdebufftimmer = 3
        $ winwin.thoughts -= 2
        $ principal.hp -= d4
        $ Rh.hp -= d4
        $ Lh.hp -= d4
        $ winwin_debuffcd = 4
        $ boss_effectamount += 1
        $ Rh_effectamount += 1
        $ Lh_effectamount += 1
        $ Lh_effects.append("rd")
        $ Rh_effects.append("rd")
        $ boss_effects.append("rd")
        call state_upd
        return

    if d10 <= 3:
        "勝勝的話語意外地激怒了對方！"
        $ principal.attack += 2
        $ Rh.attack += 2
        $ Lh.attack += 2
        $ principal_angered = True
        $ winwin_defdebufftimmer = 3
        $ winwin.thoughts -= 2
        $ principal.hp -= d4
        $ Rh.hp -= d4
        $ Lh.hp -= d4
        $ winwin_debuffcd = 4
        $ boss_effectamount += 1
        $ Rh_effectamount += 1
        $ Lh_effectamount += 1
        $ Lh_effects.append("a")
        $ Rh_effects.append("a")
        $ boss_effects.append("a")
        call state_upd
        return

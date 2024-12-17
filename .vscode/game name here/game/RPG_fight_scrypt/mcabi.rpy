label mcrest:
    "[player]選擇休息一會兒，回復些許靈感"
    $ mc.thoughts += 1
    if mc.thoughts > mc.max_thoughts:
        $ mc.thoughts = mc.max_thoughts
    return

label excuse:
    if d10 > 7:
        if target == principal:
            call tseAtkPrCam
            $ atk = d4 + d6 + mc.attack*2 - principal.defence
            if atk < 0:
                $ atk = 0
            $ principal.hp -= atk
        if target == Rh:
            call tseAtkLhRhCam
            $ atk = d4 + d6 + mc.attack*2 - Rh.defence
            if atk < 0:
                $ atk = 0
            $ Rh.hp -= atk
        if target == Lh:
            call tseAtkLhRhCam
            $ atk = d4 + d6 + mc.attack*2 - Lh.defence
            if atk < 0:
                $ atk = 0
            $ Lh.hp -= atk
        $ mc.thoughts -= 1
        "[player]說了個強而有力的藉口！"
        "十分有效"
        return

    if d10 > 1:
        if target == principal:
            call tseAtkPrCam
            $ atk = d4 + mc.attack*2 - principal.defence
            if atk < 0:
                $ atk = 0
            $ principal.hp -= atk
        if target == Rh:
            call tseAtkLhRhCam
            $ atk = d4 + mc.attack*2 - Rh.defence
            if atk < 0:
                $ atk = 0
            $ Rh.hp -= atk
        if target == Lh:
            call tseAtkLhRhCam
            $ atk = d4 + mc.attack*2 - Lh.defence
            if atk < 0:
                $ atk = 0
            $ Lh.hp -= atk
        $ mc.thoughts -= 1
        "[player]說了個普通的藉口"
        return
    
    if d10 == 1:
        "[player]的藉口爛透了！"
        return

label atk_buff:
    call tseCheerCam
    "[player]和勝勝的說服力上升了"
    $ mc.attack += 2
    $ winwin.attack += 2
    $ mc_atkbufftimmer = 3
    $ mc.thoughts -= 2
    $ mc_attackbuffcd = 5
    $ mc_effectamount += 1
    $ ww_effectamount += 1
    $ ww_effects.append("a")
    $ mc_effects.append("a")
    return

label eat:
    
    if chosen_player == player:
        "[player]吃了一口外賣"
        "[player]充滿了靈感"
        $ mc.thoughts = mc.max_thoughts
    if chosen_player == ww:
        "勝勝吃了一口你的外賣"
        "勝勝充滿了靈感"
        $ winwin.thoughts = winwin.max_thoughts
    $ food -= 1
    if food == 0:
        "[player]的外賣被吃完了"

    return

label healthsheild:
    call tseChillCam
    if chosen_player == player:
        "[player]恢復了些許體力並為下一次的攻勢做好了準備"
        $ mc.hp += 10
        $ mc.defence += 2
        $ mc_buffed = True
        $ mc_effectamount += 1
        $ mc_effects.append("h")
        if mc.hp > mc.max_hp:
            $ mc.hp = mc.max_hp

    if chosen_player == ww:
        "勝勝恢復了些許體力並為下一次的攻勢做好了準備"
        $ winwin.hp += 10
        $ winwin.defence += 2
        $ winwin_buffed = True
        $ ww_effectamount += 1
        $ ww_effects.append("h")
        if winwin.hp > winwin.max_hp:
            $ winwin.hp = winwin.max_hp

    $ mc.thoughts -= 3
    $ mc_defbufftimmer = 1
    return

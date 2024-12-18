label boss_attack:

    call StateDisplay
    
    if rd > 0:
        if summoned == False and rd == 3 and principal.hp > 70:
            $ d100 = 45
        if summoned == False and rd == 3 and principal.hp < 70:
            $ d100 = 36
        if bosseffecttimmer < 0 and (rd == 5 or rd % 10 == 0):
            $ d100 = 11

    if d100 > 70:
        call choose1
        if selected_player == 1:
            "校長對[player]使用記大過"
            if winwin_bright == False:
                if d20 >= 19:
                    call prAtkTseCam
                    play sound "SFX/wrong-buzzer-sound-effect.mp3"
                    $ atk = d4 + d6 + principal.attack*2 - mc.defence
                    if atk < 0:
                        $ atk = 0
                    $ mc.hp -= atk
                    call StateDisplay
                    "效果顯著"
                    return
                if d20 >=1:
                    call prAtkTseCam
                    play sound "SFX/wrong-buzzer-sound-effect.mp3"
                    $ atk = d4 + principal.attack*2 - mc.defence
                    if atk < 0:
                        $ atk = 0
                    $ mc.hp -= atk
                    call StateDisplay
                    "成效普通"
                    return
                if d20 == 1:
                    play sound "SFX/movie_1_C2K5NH0.mp3"
                    "未命中"
                    return

            if winwin_bright == True:
                if d20 == 20:
                    call prAtkTseCam
                    play sound "SFX/wrong-buzzer-sound-effect.mp3"
                    $ atk = d4 + principal.attack*2 - mc.defence
                    if atk < 0:
                        $ atk = 0
                    $ mc.hp -= atk
                    call StateDisplay
                    "成效普通"
                    return
                if d20 <= 19:
                    play sound "SFX/movie_1_C2K5NH0.mp3"
                    "未命中"
                    return   

        if selected_player == 2:
            "校長對[ww]使用記大過"
            if winwin_bright == False:
                if d20 >= 19:
                    call prAtkWwCam
                    play sound "SFX/wrong-buzzer-sound-effect.mp3"
                    $ atk = d4 + d6 + principal.attack*2 - winwin.defence
                    if atk < 0:
                        $ atk = 0
                    $ winwin.hp -= atk
                    call StateDisplay
                    "效果顯著"
                    return
                if d20 >=1:
                    call prAtkWwCam
                    play sound "SFX/wrong-buzzer-sound-effect.mp3"
                    $ atk = d4 + principal.attack*2 - winwin.defence
                    if atk < 0:
                        $ atk = 0
                    $ winwin.hp -= atk
                    call StateDisplay
                    "成效普通"
                    return
                if d20 == 1:
                    play sound "SFX/movie_1_C2K5NH0.mp3"
                    "未命中"
                    return

            if winwin_bright == True:
                if d20 == 20:
                    call prAtkWwCam
                    play sound "SFX/wrong-buzzer-sound-effect.mp3"
                    $ atk = d4 + principal.attack*2 - winwin.defence
                    if atk < 0:
                        $ atk = 0
                    $ winwin.hp -= atk
                    call StateDisplay
                    "成效普通"
                    return
                if d20 <= 19:
                    play sound "SFX/movie_1_C2K5NH0.mp3"
                    "未命中"
                return

    elif d100 > 50 and cantmove < 0:
        call choose2
        "校長使用禁言"
        if selected_player == 1:
            call prBanTseCam
            play sound "SFX/ban-sound-effect.mp3"
            $ mc_canmove = False
            "[player]被禁言了"
            $ cantmove = 2
            $ mc_effects.append("q")
            $ mc_effectamount += 1
            return
        if selected_player == 2:
            call prBanWwCam
            play sound "SFX/ban-sound-effect.mp3"
            $ winwin_canmove = False
            "[ww]被禁言了"
            $ cantmove = 2
            $ ww_effects.append("q")
            $ ww_effectamount += 1
            return    

    elif d100 > 40 and summoned == False and rd > 2 and principal.hp > 50:
        play sound "SFX/summon.mp3"
        call prSummonRhCam
        "校長招喚了右手"
        $ Rh.hp = Rh.max_hp
        $ summoned = True
        return

    elif d100 > 30 and summoned == False and rd > 2 and principal.hp > 50:
        play sound "SFX/summon.mp3"
        call prSummonLhCam
        "校長招喚了左手"
        $ Lh.hp = Lh.max_hp
        $ summoned = True
        return

    elif d100 > 35 and summoned == False and rd > 2 and principal.hp < 50:
        play sound "SFX/summon.mp3"
        call prSummonLhCam
        "校長招喚了左手"
        $ Lh.hp = Lh.max_hp
        $ summoned = True
        return

    elif d100 > 30 and summoned == False and rd > 2 and principal.hp < 50:
        play sound "SFX/summon.mp3"
        call prSummonRhCam
        "校長招喚了右手"
        $ Rh.hp = Rh.max_hp
        $ summoned = True
        return

    elif d100 > 15 and rd > 3:
        "範圍"
        if winwin_bright == False:
            if d20 > 1:
                call prMulAtkCam
                $ atk = d4 + principal.attack*2 
                if atk - mc.defence > 0:
                    $ mc.hp -= atk - mc.defence
                if atk - winwin.defence > 0:
                    $ winwin.hp -= atk - winwin.defence
            else:
                play sound "SFX/movie_1_C2K5NH0.mp3"
                "未命中"

        elif winwin_bright == True:
            if d20 > 19:
                call prMulAtkCam
                $ atk = d4 + principal.attack*2 
                if atk - mc.defence > 0:
                    $ amc = atk - mc.defence
                    $ mc.hp -= (atk - mc.defence)
                if atk - winwin.defence > 0:
                    $ winwin.hp -= (atk - winwin.defence)
                
            else:
                play sound "SFX/movie_1_C2K5NH0.mp3"
                "未命中"
        
        return

    elif d100 > 10 and rd > 4 and bosseffecttimmer < 0:
        call prAngerCam
        play sound "SFX/ping.mp3"
        "威嚴"
        $ bosseffecttimmer = 4
        $ bosseffectcd = 6
        $ principal.attack += 3
        $ mc.attack -= 2
        $ winwin.attack -= 2
        $ mc.defence -= 2
        $ winwin.defence -= 2

        $ boss_effectamount += 1
        $ mc_effectamount += 4
        $ ww_effectamount += 4

        $ boss_effects.append("a")
        $ mc_effects.append("rd")
        $ mc_effects.append("we")
        $ mc_effects.append("wi")
        $ mc_effects.append("rt")
        $ ww_effects.append("rd")
        $ ww_effects.append("we")
        $ ww_effects.append("wi")
        $ ww_effects.append("rt")

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
                call RhAtkTseCam
                $ atk = d4 + d6 + Rh.attack - mc.defence
                if atk < 0:
                    $ atk = 0
                $ mc.hp -= atk
                call StateDisplay
                play sound "SFX/smal-crit.mp3"
                "效果顯著"
                return
            if d20 >=1:
                call RhAtkTseCam
                $ atk = d4 + Rh.attack - mc.defence
                if atk < 0:
                    $ atk = 0
                $ mc.hp -= atk
                call StateDisplay
                play sound "SFX/meteor-smash.mp3"
                "成效普通"
                return
            if d20 == 1:
                play sound "SFX/movie_1_C2K5NH0.mp3"
                "未命中"
                return

        if winwin_bright == True:
            if d20 == 20:
                call RhAtkTseCam
                $ atk = d4 + Rh.attack - mc.defence
                if atk < 0:
                    $ atk = 0
                $ mc.hp -= atk
                call StateDisplay
                play sound "SFX/meteor-smash.mp3"
                "成效普通"
                return
            if d20 <= 19:
                play sound "SFX/movie_1_C2K5NH0.mp3"
                "未命中"
                return   

    if selected_player == 2:
        "右手對[ww]使用正面突襲"
        if winwin_bright == False:

            if d20 >= 19:
                call RhAtkWwCam
                $ atk = d4 + d6 + Rh.attack - winwin.defence
                if atk < 0:
                    $ atk = 0
                $ winwin.hp -= atk
                call StateDisplay
                play sound "SFX/smal-crit.mp3"
                "效果顯著"
                return
            if d20 >=1:
                call RhAtkWwCam
                $ atk = d4 + Rh.attack - winwin.defence
                if atk < 0:
                    $ atk = 0
                $ winwin.hp -= atk
                play sound "SFX/meteor-smash.mp3"
                call StateDisplay
                "成效普通"
                return
            if d20 == 1:
                play sound "SFX/movie_1_C2K5NH0.mp3"
                "未命中"
                return

        if winwin_bright == True:
            if d20 == 20:
                call RhAtkWwCam
                $ atk = d4 + Rh.attack - winwin.defence
                if atk < 0:
                    $ atk = 0
                $ winwin.hp -= atk
                call StateDisplay
                play sound "SFX/meteor-smash.mp3"
                "成效普通"
                return
            if d20 <= 19:
                play sound "SFX/movie_1_C2K5NH0.mp3"
                "未命中"
            return
    
    return

label Lh_attack:
    
    call StateDisplay
    play sound "SFX/111-pokemon-recovery.mp3"
    "左手對校長使用了回復"
    $ principal.hp += 5
    if principal.hp > principal.max_hp:
        $ principal.hp = principal.max_hp
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
    
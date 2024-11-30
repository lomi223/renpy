screen player_state:
    grid 2 2:
        spacing 20
        if mc.hp > 0:
            frame:
                xoffset 20
                yoffset 10
                hbox:
                    spacing 20
                    vbox:
                        text "%s" % mc.name
                        text "HP"
                        text "TP"
                        text "def"
                        text "atk"
                    
                    vbox:
                        text ""
                        text "%d / %d" % (mc.hp , mc.max_hp)
                        text "%d / %d" % (mc.thoughts , mc.max_thoughts)
                        text "%d" % mc.defence
                        text "%d" % mc.attack
        else:
            text ""
        if winwin.hp > 0:
            frame:
                xoffset 20
                yoffset 10
                hbox:
                    spacing 20
                    vbox:
                        text "%s" % winwin.name
                        text "HP"
                        text "TP"
                        text "def"
                        text "atk"
                    
                    vbox:
                        text ""
                        text "%d / %d" % (winwin.hp , winwin.max_hp)
                        text "%d / %d" % (winwin.thoughts , winwin.max_thoughts)
                        text "%d" % winwin.defence
                        text "%d" % winwin.attack
        else:
            text ""
        if mc.hp > 0:
            grid mc_effectamount 1 :
                xanchor 0.0
                xoffset 20
                spacing 5
                for i in mc_effects:
                    imagebutton:
                        at zoomedin
                        idle "EffectIcon/%s idle.png" % i
        else:
            text ""
        if winwin.hp > 0:
            grid ww_effectamount 1 :
                xanchor 0.0
                xoffset 20
                spacing 5
                for i in ww_effects:
                    imagebutton:
                        at zoomedin
                        idle "EffectIcon/%s idle.png" % i
        else:
            text ""

screen enemy_state:
    grid 2 2:
        xalign 1.0
        spacing 20
        
        if Rh.hp > 0:
            frame:
                xoffset -20
                yoffset 10
                hbox:
                    spacing 20
                    vbox:
                        text "%s" % Rh.name
                        text "HP"
                        text "TP"
                        text "def"
                        text "atk"
                    
                    vbox:
                        text ""
                        text "%d / %d" % (Rh.hp , Rh.max_hp)
                        text "%d / %d" % (Rh.thoughts , Rh.max_thoughts)
                        text "%d" % Rh.defence
                        text "%d" % Rh.attack
        elif Lh.hp > 0:
            frame:
                xoffset -20
                yoffset 10
                hbox:
                    spacing 20
                    vbox:
                        text "%s" % Lh.name
                        text "HP"
                        text "TP"
                        text "def"
                        text "atk"
                    
                    vbox:
                        text ""
                        text "%d / %d" % (Lh.hp , Lh.max_hp)
                        text "%d / %d" % (Lh.thoughts , Lh.max_thoughts)
                        text "%d" % Lh.defence
                        text "%d" % Lh.attack
        else:
            text ""
        if principal.hp > 0:
            frame:
                xoffset -20
                yoffset 10
                hbox:
                    spacing 20
                    vbox:
                        text "%s" % principal.name
                        text "HP"
                        text "TP"
                        text "def"
                        text "atk"
                    
                    vbox:
                        text ""
                        text "%d / %d" % (principal.hp , principal.max_hp)
                        text "%d / %d" % (principal.thoughts , principal.max_thoughts)
                        text "%d" % principal.defence
                        text "%d" % principal.attack
        else:
            text ""
        if Rh.hp > 0:
            grid Rh_effectamount 1 :
                xanchor 0.0
                xoffset -20
                spacing 5
                for i in Rh_effects:
                    imagebutton:
                        at zoomedin
                        idle "EffectIcon/%s idle.png" % i
        elif Lh.hp > 0:
            grid Rh_effectamount 1 :
                xanchor 0.0
                xoffset -20
                spacing 5
                for i in Rh_effects:
                    imagebutton:
                        at zoomedin
                        idle "EffectIcon/%s idle.png" % i
        else:
            text ""
        if principal.hp > 0:
            grid boss_effectamount 1 :
                xanchor 0.0
                xoffset -20
                spacing 5
                for i in boss_effects:
                    imagebutton:
                        at zoomedin
                        idle "EffectIcon/%s idle.png" % i
        else:
            text ""

screen player_state:
    hbox:
        spacing 20
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


screen boss_state:
    hbox:
        xalign 1.0
        spacing 20
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

screen player_state:
    hbox:
        spacing 20
        frame:
            xoffset 20
            yoffset 10
            hbox:
                spacing 20
                vbox:
                    text "hp"
                    text "mp"
                    text "def"
                    text "atk"
                
                vbox:
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
                    text "hp"
                    text "mp"
                    text "def"
                    text "atk"
                
                vbox:
                    text "%d / %d" % (winwin.hp , winwin.max_hp)
                    text "%d / %d" % (winwin.thoughts , winwin.max_thoughts)
                    text "%d" % winwin.defence
                    text "%d" % winwin.attack

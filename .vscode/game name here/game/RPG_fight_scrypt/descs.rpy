screen sk1_desc:
    frame:
        xpadding 100
        ypadding 50
        xalign 0.5
        yalign 1.0
        yoffset -10
        xoffset 20
        text "找個藉口，對選定目標造成一定傷害（消耗：1TP）"

screen sk2_desc:
    frame:
        xpadding 100
        ypadding 50
        xalign 0.5
        yalign 1.0
        yoffset -10
        xoffset 20
        text "給我方全體加油，提升攻擊力（消耗：2TP）\n（持續3回合）（CD：5回合）"

screen sk3_desc:
    frame:
        xpadding 100
        ypadding 50
        xalign 0.5
        yalign 1.0
        yoffset -10
        xoffset 20
        text "給我方選定目標一個呼呼，回復HP並提升防禦（消耗：3TP）\n（只在當前回合奏效）"

screen food_desc:
    frame:
        xpadding 100
        ypadding 50
        xalign 0.5
        yalign 1.0
        yoffset -10
        xoffset 20
        text "吃一口外賣，為我方選定目標回復所有TP\n（當前剩餘： %d）" % food

screen wwsk1_desc:
    frame:
        xpadding 100
        ypadding 50
        xalign 0.5
        yalign 1.0
        yoffset -10
        xoffset 20
        text "跟選定目標講道理，有機會對選定目標造成大量傷害"

screen wwsk2_desc:
    frame:
        xpadding 100
        ypadding 50
        xalign 0.5
        yalign 1.0
        yoffset -10
        xoffset 20
        text "站在[player]前面，為[player]抵擋傷害\n（只在當前回合生效）"

screen wwsk3_desc:
    frame:
        xpadding 100
        ypadding 50
        xalign 0.5
        yalign 1.0
        yoffset -10
        xoffset 20
        text "[ww]開始發光，閃瞎對手的同時受到灼燒傷害\n（持續3回合）（CD：4回合）"

screen wwsk4_desc:
    frame:
        xpadding 100
        ypadding 50
        xalign 0.5
        yalign 1.0
        yoffset -10
        xoffset 20
        text "對對方全體進行嘴砲，有可能降防或激怒對方（消耗：2TP）\n（持續3回合）（CD：4回合）"

screen efdesc:
    default Showing = ""
    frame:
        xpadding 100
        ypadding 50
        xalign 0.5
        yalign 1.0
        yoffset -10
        xoffset 20
        if Showing == "a":
            text "ATK+2"
        if Showing == "h":
            text "DEF+2"
        if Showing == "bl":
            text "致盲：命中率下降"
        if Showing == "b":
            text "灼燒：每回合HP-1"
        if Showing == "q":
            text "禁言：本回合無法行動"
        if Showing == "rd":
            text "DEF-2"
        if Showing == "nd":
            text "破防：DEF歸0"
        if Showing == "wi":
            text "每回合HP-3"
        if Showing == "t":
            text "我來扛：必定受到敵方選定"
        if Showing == "we":
            text "ATK-2"
        if Showing == "rt":
            text "每回合TP-3"

screen rest:
    frame:
        xpadding 100
        ypadding 50
        xalign 0.5
        yalign 1.0
        yoffset -10
        xoffset 20
        text "休息一回合，回復1TP"
screen mc_attackchoice:
    frame:
        xoffset 40
        yoffset -30
        xpadding 50
        xalign 0.0
        yalign 1.0
        vbox:
            textbutton "abi" action [ToggleScreen("mc_attackchoice"),ToggleScreen("mc_abi")]
            textbutton "props" action [ToggleScreen("mc_attackchoice"),ToggleScreen("mc_props")]
            textbutton "rest" action [ToggleScreen("mc_attackchoice"),Jump("rest")]

screen mc_abi:
    frame:
        xoffset 40
        yoffset -30
        xpadding 50
        xalign 0.0
        yalign 1.0
        vbox:
            textbutton "找藉口 - 1 靈感":
                if mc.thoughts >= 1:
                    action [ToggleScreen("mc_abi"),Jump("excuse")]
                else:
                    action [Call("low_mp")]
            textbutton "加油 - 2 靈感":
                if mc_atkbufftimmer < 0 and mc.thoughts >= 2:
                    action [ToggleScreen("mc_abi"),Jump("atk_buff")]
                elif mc_atkbufftimmer > 0:
                    action [Notify("技能冷卻中")]
                elif mc.thoughts < 2:
                    action [Notify("mp不足")]
            textbutton "沒事的 - 3 靈感":
                if mc_defbufftimmer <= 0 and mc.thoughts >= 3:
                    action [SetVariable("jump_label","healthsheild"),ToggleScreen("mc_abi"),ToggleScreen("mc_ChooseCharater")]
                elif mc_atkbufftimmer > 0:
                    action [Notify("技能冷卻中")]
                elif mc.thoughts < 3:
                    action [Notify("mp不足")]
            textbutton "返回" action [ToggleScreen("mc_abi"),ToggleScreen("mc_attackchoice")]
            
screen mc_props:
    frame: 
        xoffset 40
        yoffset -30
        xpadding 50
        xalign 0.0
        yalign 1.0
        vbox:
            if food > 0:
                textbutton "吃外賣":
                    action [SetVariable("jump_label","eat"),ToggleScreen("mc_props"),ToggleScreen("mc_ChooseCharater")]
            textbutton "返回" action [ToggleScreen("mc_props"),ToggleScreen("mc_attackchoice")]

screen mc_ChooseCharater:
    frame:
        xoffset 40
        yoffset -30
        xpadding 50
        xalign 0.0
        yalign 1.0
        vbox:
            if mc.hp > 0:
                textbutton "[player]":
                    if jump_label == "eat":
                        action [SetVariable("chosen_player",player),ToggleScreen("mc_ChooseCharater"),Jump("eat")]
                    if jump_label == "healthsheild":
                        action [SetVariable("chosen_player",player),ToggleScreen("mc_ChooseCharater"),Jump("healthsheild")]
            if winwin.hp > 0:
                textbutton "[ww]":
                    if jump_label == "eat":
                        action [SetVariable("chosen_player",ww),ToggleScreen("mc_ChooseCharater"),Jump("eat")]
                    if jump_label == "healthsheild":
                        action [SetVariable("chosen_player",ww),ToggleScreen("mc_ChooseCharater"),Jump("healthsheild")]
            textbutton "返回" action [ToggleScreen("mc_ChooseCharater"),ToggleScreen("mc_attackchoice")]

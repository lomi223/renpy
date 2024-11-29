style mytextbutton:
    color "#ffffff"
    hover_color "#cde15c"
style blockedbutton:
    color "#777777"


screen mc_attackchoice:
    frame:
        xoffset 40
        yoffset -30
        xpadding 50
        xalign 0.0
        yalign 1.0
        vbox:
            textbutton "技能":
                text_style "mytextbutton"
                action [ToggleScreen("mc_attackchoice"),ToggleScreen("mc_abi")]
            textbutton "道具":
                text_style "mytextbutton"
                action [ToggleScreen("mc_attackchoice"),ToggleScreen("mc_props")]
            textbutton "休息":
                text_style "mytextbutton"
                action [ToggleScreen("mc_attackchoice"),Jump("mcrest")]

screen mc_abi:
    frame:
        xoffset 40
        yoffset -30
        xpadding 50
        xalign 0.0
        yalign 1.0
        vbox:
            textbutton "找藉口 - 1 靈感":
                hovered Show("sk1_desc")
                unhovered Hide("sk1_desc")
                if mc.thoughts >= 1:
                    text_style "mytextbutton"
                    action [SetVariable("jump_label","excuse"),SetVariable("prvscreen","mc_attackchoice"),ToggleScreen("mc_abi"),Hide("sk1_desc"),ToggleScreen("choosetarget")]
                else:
                    text_style "blockedbutton"
                    action [Notify("mp不足")]
            textbutton "加油 - 2 靈感":
                hovered Show("sk2_desc")
                unhovered Hide("sk2_desc")
                if mc_attackbuffcd < 0 and mc.thoughts >= 2:
                    text_style "mytextbutton"
                    action [ToggleScreen("mc_abi"),Hide("sk2_desc"),Jump("atk_buff")]
                elif mc_attackbuffcd > 0:
                    text_style "blockedbutton"
                    action [Notify("技能冷卻中")]
                elif mc.thoughts < 2:
                    text_style "blockedbutton"
                    action [Notify("mp不足")]
            textbutton "沒事的 - 3 靈感":
                text_style "mytextbutton"
                hovered Show("sk3_desc")
                unhovered Hide("sk3_desc")
                if mc_defbufftimmer < 0 and mc.thoughts >= 3:
                    text_style "mytextbutton"
                    action [SetVariable("jump_label","healthsheild"),Hide("sk3_desc"),ToggleScreen("mc_abi"),ToggleScreen("mc_ChooseCharater")]
                elif mc_atkbufftimmer > 0:
                    text_style "blockedbutton"
                    action [Notify("技能冷卻中")]
                elif mc.thoughts < 3:
                    text_style "blockedbutton"
                    action [Notify("mp不足")]
            textbutton "返回":
                text_style "mytextbutton"
                action [ToggleScreen("mc_abi"),ToggleScreen("mc_attackchoice")]
            
screen mc_props:
    frame: 
        xoffset 40
        yoffset -30
        xpadding 50
        xalign 0.0
        yalign 1.0
        vbox:
            if food > 0:
                textbutton "吃外賣 %d" % food:
                    text_style "mytextbutton"
                    hovered Show("food_desc")
                    unhovered Hide("food_desc")
                    action [SetVariable("jump_label","eat"),Hide("food_desc"),ToggleScreen("mc_props"),ToggleScreen("mc_ChooseCharater")]
            textbutton "返回":
                text_style "mytextbutton"
                action [ToggleScreen("mc_props"),ToggleScreen("mc_attackchoice")]

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
                    text_style "mytextbutton"
                    action [SetVariable("chosen_player",player),ToggleScreen("mc_ChooseCharater"),Jump(jump_label)]
            if winwin.hp > 0:
                textbutton "[ww]":
                    text_style "mytextbutton"
                    action [SetVariable("chosen_player",ww),ToggleScreen("mc_ChooseCharater"),Jump(jump_label)]

            textbutton "返回":
                text_style "mytextbutton"
                action [ToggleScreen("mc_ChooseCharater"),ToggleScreen("mc_attackchoice")]

screen choosetarget:
    frame:
        xoffset 40
        yoffset -30
        xpadding 50
        xalign 0.0
        yalign 1.0
        vbox:
            if principal.hp > 0:
                textbutton "校長":
                    text_style "mytextbutton"
                    action [SetVariable("target",principal),ToggleScreen("choosetarget"),Jump(jump_label)]
            if Rh.hp > 0:
                textbutton "右手":
                    text_style "mytextbutton"
                    action [SetVariable("target",Rh),ToggleScreen("choosetarget"),Jump(jump_label)]
            if Lh.hp > 0:
                textbutton "左手":
                    text_style "mytextbutton"
                    action [SetVariable("target",Lh),ToggleScreen("choosetarget"),Jump(jump_label)]
            textbutton "返回":
                text_style "mytextbutton"
                action [ToggleScreen("choosetarget"),ToggleScreen(prvscreen)]



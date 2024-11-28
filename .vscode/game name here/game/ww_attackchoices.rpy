screen ww_attackchoice:
    frame:
        xoffset 40
        yoffset -30
        xpadding 50
        xalign 0.0
        yalign 1.0
        vbox:
            textbutton "技能":
                text_style "mytextbutton"
                action [ToggleScreen("ww_attackchoice"),ToggleScreen("ww_abi")]
            textbutton "道具":
                text_style "mytextbutton"
                action [ToggleScreen("ww_attackchoice"),ToggleScreen("ww_props")]
            textbutton "休息":
                text_style "mytextbutton"
                action [ToggleScreen("ww_attackchoice"),Jump("wwrest")]

screen ww_abi:
    frame:
        xoffset 40
        yoffset -30
        xpadding 50
        xalign 0.0
        yalign 1.0
        vbox:
            textbutton "以理服人":
                text_style "mytextbutton"
                hovered Show("wwsk1_desc")
                unhovered Hide("wwsk1_desc")
                action [SetVariable("jump_label","wwab1"),SetVariable("prvscreen","ww_attackchoice"),Hide("wwsk1_desc"),ToggleScreen("ww_abi"),ToggleScreen("choosetarget")]
            textbutton "我來扛":
                text_style "mytextbutton"
                hovered Show("wwsk2_desc")
                unhovered Hide("wwsk2_desc")
                action [ToggleScreen("ww_abi"),Hide("wwsk2_desc"),Jump("wwab2")]
            textbutton "陽光開朗大男孩":
                hovered Show("wwsk3_desc")
                unhovered Hide("wwsk3_desc")
                if winwin_brightcd < 0:
                    text_style "mytextbutton"
                    action [ToggleScreen("ww_abi"),Hide("wwsk3_desc"),Jump("wwab3")]
                elif winwin_brightcd > 0:
                    text_style "blockedbutton"
                    action [Notify("技能冷卻中")]
            textbutton "嘴砲 - 2 靈感":
                hovered Show("wwsk4_desc")
                unhovered Hide("wwsk4_desc")
                if winwin_debuffcd < 0 and winwin.thoughts >= 2:
                    text_style "mytextbutton"
                    action [ToggleScreen("ww_abi"),Hide("wwsk4_desc"),Jump("wwab4")]
                elif winwin_debuffcd > 0:
                    text_style "blockedbutton"
                    action [Notify("技能冷卻中")]
                elif winwin.thoughts < 2:
                    text_style "blockedbutton"
                    action [Notify("mp不足")]
            textbutton "返回":
                text_style "mytextbutton"
                action [ToggleScreen("ww_abi"),ToggleScreen("ww_attackchoice")]

screen ww_props:
    frame:
        xoffset 40
        yoffset -30
        xpadding 50
        xalign 0.0
        yalign 1.0
        vbox:
            textbutton "返回":
                text_style "mytextbutton"
                action [ToggleScreen("ww_props"),ToggleScreen("ww_attackchoice")]


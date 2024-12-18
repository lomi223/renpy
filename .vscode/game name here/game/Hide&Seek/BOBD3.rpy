label BOBD3:
    play music "snowdin-town.mp3"
    scene black with dissolve
    centered "你來到了教室"
    scene classroom with dissolve

    show a norm with dissolve
    a "早安阿[player]"
    a "你要不要跟我一起去圖書館？"
    player "我......{nw}"
    show a norm:
        linear 0.3 xalign 0.65
    show s angered:
        xalign 0.0
        yalign 1.0
        linear 0.3 xalign 0.35
    s "你在說甚麼呢？"
    s "[player]已經跟我約好要一起玩了"
    show s norm
    s "對吧，[player]"
    player "......我{nw}"
    show w norm:
        zoom 0.5
        xalign 1.0 
        yalign 1.0
        linear 0.3 xalign 0.75
    show a norm:
        linear 0.3 xalign 0.5
    show s norm:
        linear 0.3 xalign 0.25
    w "不對！"
    w "[player]已經跟我約好要去愛買了"
    show bob norm:
        xalign 0.0
        yalign 1.0
        linear 0.5 xalign 0.05
    show w norm:
        linear 0.5 xalign 0.95
    show a norm:
        linear 0.5 xalign 0.65
    show s norm:
        linear 0.5 xalign 0.35
    b "哎呀！你們真是的"
    b "也不問問[player]的意見"
    b "那麼[player]你想跟誰一起玩呢？"
    jump ChooseWho
    return

label ChooseWho:
    stop sound
    hide static
    if (choose_a or choose_s or choose_w):
        player "該選誰好呢？"
        menu:
            "勝勝" if choose_w:
                stop music
                pause 1.0
                $ choose_w = False
                hide w
                show static
                play sound "SFX/ten-minutes-of-static.mp3"
                pause 1.0
                jump ChooseWho
            "碩碩" if choose_s:
                stop music
                pause 1.0
                $ choose_s = False
                hide s 
                show static
                play sound "SFX/ten-minutes-of-static.mp3"
                pause 1.0
                jump ChooseWho
            "Alex" if choose_a:
                stop music
                pause 1.0
                $ choose_a = False
                hide a
                show static
                play sound "SFX/ten-minutes-of-static.mp3"
                pause 1.0
                jump ChooseWho
            "BOB":
                jump bob_chosen
    else:
        play music "<from 0.1 to 3>SFX/undertale-sound-effect-chara-jumpscare.mp3"
        call screen dynamic_menu(20)
        stop music
        show static
        play sound "SFX/ten-minutes-of-static.mp3"
        pause 1.0
        jump bob_chosen
    return

label bob_chosen:
    stop sound
    hide static
    play music "snowdin-town.mp3"
    show bob norm:
        xalign 0.05
    show w norm:
        zoom 0.5
        yalign 1.0
        xalign 0.95
    show a norm:
        xalign 0.65
    show s norm:
        xalign 0.35

    b "我就知道你會選擇我[player]"
    b "我們走吧！"
    scene black with dissolve
    scene classroom with dissolve
    show b norm with dissolve
    b "該做甚麼呢？"
    menu:
        "來玩躲貓貓吧！":
            b "好啊！"
            b "我先躲，你要來找我喔！"
            scene black with dissolve
            centered "BOB花了點時間將自己藏好"
            jump bob_and_seak

screen dynamic_menu(num_choices):
    vbox:
        xalign 0.5     
        
        for i in range(1, num_choices + 1):
            textbutton "BOB":
                style_prefix "btns"
                action Return()

style btns_button:
    background "gui/button/choice_idle_background.png"
    hover_background "gui/button/choice_hover_background.png"
    xminimum 1150
    yminimum 50
    padding (10, 10, 10, 10)
    xalign 0.5
style btns_button_text:
    xalign 0.5
    yalign 0.5
    color "#b100008a"
label splashscreen:
    python:
        import os
        real_name = os.getlogin()
    if not persistent.agreed:
        scene starting_image
        "This game is not suitable for children who are easily disturbed."
        "Individuals suffering from anxiety or depression may not have a safe experience playing this game.For content warnings, please visit: https://www.youtube.com/watch?v=-HR421cejTM "
        "By playing Doki Doki Fixed, you agree that you are at least 13 years of age, and you consent to your exposure of highly disturbing content."
        menu:
            "I agree":
                $ persistent.agreed = True
    scene black 
    with Pause(0.5)
    show splash with dissolve:
        zoom 7.0
    with Pause(2)
    scene black with dissolve
    with Pause(1)
    return


label start: 
    stop music
    if persistent.bob:
        jump bob_and_me
    $ name = "澤澤"
    camera:
        perspective True
    play music "Start Menu.mp3" loop fadein 0.3 volume 1.5
    menu:
        "name":
            jump inputname
        "boss":
            jump boss_fight
        "bob":
            jump bob_and_seak
        "day4":
            jump day4
        "WWD3":
            jump WWDay3_morning
        "test":
            jump test
#label cg:
#    show black with dissolve
#    menu:
#        "show CG_a":
#            scene CG_a_red with fade
#            scene CG_a_blue with fade
#            scene CG_a_yellow with fade
#            scene CG_a_green with fade
#            scene CG_a_orange with fade
#            scene CG_a_indigo with fade
#            ""
#            jump cg
#        "show CG_b":
#            scene CG_b_red with fade
#            scene CG_b_blue with fade
#            scene CG_b_yellow with fade
#            scene CG_b_green with fade
#            scene CG_b_orange with fade
#            scene CG_b_indigo with fade
#            ""
#            jump cg
#        "show CG_c":
#            scene CG_c_red with fade
#            scene CG_c_blue with fade
#            scene CG_c_yellow with fade
#            scene CG_c_green with fade
#            scene CG_c_orange with fade
#            scene CG_c_indigo with fade
#            ""
#            jump cg
#        "nah":
#            jump inputname

    
label inputname:

    scene black with fade
    $ name = renpy.input("請在此輸入你的名字",length = 32)
    $ name = name.strip()
    if not name:
        $ name = "澤澤" 
    "[name]是你的名字嗎?"
    
menu:
    "Yes":
        jump say_my_name
    "No":
        jump inputname
        
label say_my_name:
    player "我的名字是[name]。"
    stop music fadeout 0.5
    jump act1
    
    return

label test:
    show b glitched
    ""
    return
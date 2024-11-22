label splashscreen:
    scene black 
    with Pause(1)
    show splash with dissolve 
    with Pause(2)
    scene black with dissolve
    with Pause(1)
    return


label start: 
    play music "11-just-monika.mp3" loop fadein 0.5 volume 0.3

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

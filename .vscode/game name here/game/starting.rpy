label splashscreen:
    scene black 
    with Pause(1)
    show splash with dissolve 
    with Pause(2)
    scene black with dissolve
    with Pause(1)
    return


label start:

label cg:
    menu:
        "show CG_a":
            scene CG_a_red with fade
            scene CG_a_blue with fade
            scene CG_a_yellow with fade
            scene CG_a_green with fade
            scene CG_a_orange with fade
            scene CG_a_indigo with fade
            ""
            jump cg
        "show CG_b":
            scene CG_b_red with fade
            scene CG_b_blue with fade
            scene CG_b_yellow with fade
            scene CG_b_green with fade
            scene CG_b_orange with fade
            scene CG_b_indigo with fade
            ""
            jump cg
        "show CG_c":
            scene CG_c_red with fade
            scene CG_c_blue with fade
            scene CG_c_yellow with fade
            scene CG_c_green with fade
            scene CG_c_orange with fade
            scene CG_c_indigo with fade
            ""
            jump cg
        "nah":
            jump inputname

    
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
"""
    # 顯示背景。 預設情況下，它使用佔位符，但您可以
    # 將檔案（名為 "bg room.png" 或 "bg room.jpg"）新增至
    # images 目錄來顯示它。
    scene bg room
    with fade
    play music "audio/11-just-monika.mp3" fadein 0.1 volume 0.3
    # 這顯示了一個角色精靈。 使用了佔位符，但您可以
    # 透過將名為 "eileen happy.png" 的檔案
    # 新增至 images 目錄來取代它。

    show eileen happy
    with dissolve
    
    # 這些顯示對話行。

    e "感謝您遊玩DDGC。"

    e "您將在此體驗您未曾有過的校園戀愛生活。"
"""

label say_my_name:
    player "我的名字是[name]。"
    jump act1
    
    return

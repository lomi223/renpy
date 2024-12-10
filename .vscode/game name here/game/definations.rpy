
define t = Character("[tt]", image = "t")
define w = Character("[ww]", image = "w")
define a = Character("[aa]", image = "a")
define s = Character("[ss]", image = "s")
define b = Character("[bb]", image = "b")
define npc_black = Character("皮膚黝黑的學生", image = "npc_black")
define npc_tall = Character("很高的學生", image = "npc_tall")
define npc_glasses = Character("戴著眼鏡的學生", image = "npc_glasses")
define player = Character("[name]")
define pr = Character("校長", image = "principal")

default tt = "？？？"
default ww = "？？？"
default aa = "？？？"
default ss = "？？？"
default bb = "BOB"

default persistent.testflag = 0
default persistent.bob = False

image splash = "temp_splash_img.png" 
image street_scene = "scene/road_scene.jpg"
image classroom :
    "scene/classroom.webp"
    zoom 2.0
image bedroom:
    "scene/bedroom.jpg"
    xzoom 3
    yzoom 2.5
image bathroom = "scene/bathroom.jpg"
image outside = "scene/school_outside.jpg"
image bedroom_night = "scene/bedroom_night.jpg"
image radio = "scene/radio.jpg"
image boss_scene = "scene/boss_scene.png"
image bossroom_floor = "scene/floor.jpg"
image static:
    "scene/static.jpg"
    zoom 3.5

image CG_a_red = "CGs/a_red.png"
image CG_a_blue = "CGs/a_blue.png"
image CG_a_yellow = "CGs/a_yellow.png"
image CG_a_green = "CGs/a_green.png"
image CG_a_orange = "CGs/a_orange.png"
image CG_a_indigo = "CGs/a_indigo.png"
 
image CG_b_red = "CGs/b_red.png"
image CG_b_blue = "CGs/b_blue.png"
image CG_b_yellow = "CGs/b_yellow.png"
image CG_b_green = "CGs/b_green.png"
image CG_b_orange = "CGs/b_orange.png"
image CG_b_indigo = "CGs/b_indigo.png"

image CG_c_red = "CGs/c_red.png"
image CG_c_blue = "CGs/c_blue.png"
image CG_c_yellow = "CGs/c_yellow.png"
image CG_c_green = "CGs/c_green.png"
image CG_c_orange = "CGs/c_orange.png"
image CG_c_indigo = "CGs/c_indigo.png"

default played_count = 0
default street_flag = 0
default wall_flag = 0
default a_notreacted = 1
default w_notreacted = 1
default s_notreacted = 1
default b_canreact = 0
default w_love = 0
default s_love = 0
default a_love = 0
default b_love = 0
default repeat = 0
default screen_changed = 0
default jump_label = ""
default chosen_player = ""
default target = ""
default prvscreen = ""
default mc_effects = []
default ww_effects = []
default boss_effects = []
default Rh_effects = []
default Lh_effects = []
default caught = False
default bob = False

default choose_w = True
default choose_a = True
default choose_s = True

screen radio_button:
    imagebutton:
        idle "radio_idle.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.498
        ypos 0.556
        at zoomedin
        action Jump("not_here")

init python:
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
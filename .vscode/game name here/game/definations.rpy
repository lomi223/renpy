
define t = Character("[tt]", image = "t")
define w = Character("[ww]", image = "w")
define a = Character("[aa]", image = "a")
define s = Character("[ss]", image = "s")
define b = Character("[bb]", image = "b")
define player = Character("[name]")

default tt = "？？？"
default ww = "？？？"
default aa = "？？？"
default ss = "？？？"
default bb = "？？？"

default persistent.testflag = 0

image splash = "temp_splash_img.png" 
image street_scene = "scene/road_scene.jpg"
image classroom :
    "scene/classroom.webp"
    zoom 2.0
image bedroom = "scene/bedroom.jpg"
image outside = "scene/school_outside.jpg"

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
default w_notrecated = 1
default s_notreacted = 1
default w_love = 0
default s_love = 0
default a_love = 0
default b_love = 0
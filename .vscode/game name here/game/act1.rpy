image street_scene = "road_scene.jpg"
image classroom = "classroom.webp"

label act1:
#    first scene start here\
    scene black with dissolve
    "八月的尾聲即將到來，即將邁入秋色的風似乎更加喧囂了。青澀的少年渴望抓住夏天的尾巴、為青春開啟美好的篇章。" with fade
    scene street_scene with dissolve:
        zoom 3
    show w with dissolve:
        zoom 0.6
        yalign 1.5
        xalign 0.5
    w "{size=*2}嘿!哥們{/size}"
    w "上學不揪"
    menu:
        "嗨勝勝":
            player "一起走阿"
            jump classroom
        "約嗎？":
            w "好啊"
            jump end1

label classroom:
    scene classroom with dissolve:
        zoom 2
    ""
    return
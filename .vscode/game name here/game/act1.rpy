label act1:
    play music "bird-chirping-sound-effect.mp3" loop fadein 0.3 volume 0.3
    scene black with dissolve
    centered "八月的尾聲即將到來，即將邁入秋色的風似乎更加喧囂了。青澀的少年渴望抓住夏天的尾巴、為青春開啟美好的篇章。" with fade
    
    scene bedroom with dissolve:
        xzoom 3
        yzoom 2.5
    player "今天天氣真不錯！"
label do_what:
    player "接下來要幹嘛呢？"
    menu:
        "去上學" if played_count < 3:
            if played_count == 0:
                stop music
                play music "birds-flying-away.mp3" noloop
                jump w_on_street
            else:
                stop music
                play music "birds-flying-away.mp3" noloop
                jump s_wall

        "玩會兒遊戲" if played_count < 3:
            scene black with dissolve
            $ played_count += 1
            scene bedroom with dissolve:
                xzoom 3
                yzoom 2.5
            player "刺激"
            if played_count < 3:
                jump do_what
            else:
                stop music
                jump playing_ending
            
label w_on_street:
    scene street_scene with Fade(0.5,1.0,0.5):
        zoom 3
    show w norm with dissolve:
        zoom 0.6
        yalign 1.5
        xalign 0.5
    w "{size=*2}嘿!哥們{/size}"
    w  "上學不揪"

    menu:
        "嗨勝勝":
            player "一起走阿"
            jump classroom


label s_wall:
    scene black with dissolve
    "你飛快來到了學校"
    "但你還是遲到了"

    show outside with dissolve:
        xsize 1.1
        ysize 1.1

    player "糟了！"
    player "現在進去肯定會被抓"
    show s norm with dissolve
    
    s "你也遲到啦？"
    player "碩碩！"
    "碩碩是你的青梅竹馬"
    "你們從小便經常玩在一起"
    s "我來助你"
    scene black with dissolve
    centered "碩碩表演了一番身法後翻到了牆上，順便也將你拉了上去"

label classroom:
    scene classroom with dissolve:
        zoom 2
    ""
    return
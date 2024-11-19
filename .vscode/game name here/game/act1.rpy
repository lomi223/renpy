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
                $ street_flag = 1
                jump a_on_street
            else:
                stop music
                play music "birds-flying-away.mp3" noloop
                $ wall_flag = 1
                jump w_wall

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
            
label a_on_street:
    scene black with dissolve
    centered "行走於繁華的街道中，[player]見到了......"
    scene street_scene with dissolve:
        zoom 3
    show a norm with dissolve:
        zoom 0.6
        yalign 1.5
        xalign 0.5
    pause 1.0
    hide a norm with dissolve
    player "啊......啊"
    player "很美~~~~阿"
    player "他媽的"
    player "好美......阿阿"
    "女孩的秀髮於風中飄盪著"
    "挑逗著[player]的內心"
    jump classroom

label w_wall:
    scene black with dissolve
    "你飛快來到了學校"
    "但你還是遲到了"

    show outside with dissolve:
        xsize 1.1
        ysize 1.1

    player "糟了！"
    player "現在進去肯定會被抓"
    show w norm with dissolve
    
    w "你也遲到啦？"
    player "勝勝！？"
    w "我來助你"
    scene black with dissolve
    centered "勝勝表演了一番身法後翻到了牆上，順便也將你拉了上去"

label classroom:
    scene classroom with Fade(0.5,1.0,0.5)
    if street_flag:
        show s norm with dissolve 
        "來到教室，你發現碩碩已經座在位子上"
        player "早啊！碩碩"
        player "你也在這間學校啊！"
        "發現你的到來，碩碩靦腆的低下了頭"
        show s shy with dissolve
        s "早......早阿"
        hide s
        scene black with dissolve
        centered "正當你和碩碩聊得正歡時"
        scene classroom with dissolve
        show a norm with dissolve:
            xpos 0.0
            linear 2.0 xpos 1.0
        pause 1.0
        hide a norm with dissolve
        pause 0.5
        player "是早上那個女孩！"
        player "他也在這裡"







    return


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
    "少女的秀髮於風中飄盪著"
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
    player "你是！？"
    w "我來助你"
    scene black with dissolve
    centered "對方表演了一番身法後翻到了牆上，向你伸出了手"
    $ ww = "勝勝"
    w "你好！我叫勝勝"
    centered "你們以全速衝往了教室"
label classroom:
    scene classroom with Fade(0.5,1.0,0.5)
    play music "snowdin-town.mp3" loop volume 0.5
    if street_flag:
        show s norm with dissolve 
        "來到教室，你發現你的青梅碩碩已經座在位子上"
        player "早啊！碩碩"
        player "你也在這間學校啊！"
        "發現你的到來，碩碩靦腆的低下了頭"
        $ ss = "碩碩"
        show s shy with dissolve
        s "早......早阿"
        hide s
        scene black with dissolve

        centered "正當你和碩碩聊得正歡時"
        scene classroom with dissolve
        play sound "SFX/walking_6QdYC8X.mp3"
        show a norm with dissolve:
            xpos 0.0
            linear 4.0 xpos 1.0
        pause 4.0
        hide a norm with dissolve
        pause 0.5
        player "是早上那個女孩！"
        player "他也在這裡"

        play sound "SFX/door-slam.mp3" noloop volume 0.5
        pause 1.0
        show w norm with dissolve:
            zoom 0.6
            yalign 1.5
            xalign 0.5
        w "剛好趕上"
        "突如其來的聲響嚇了你一跳"
        w "早啊！哥們"
        show w norm:
            xpos 0.5
            linear 0.25 xpos 1.5
        pause 0.5
        hide w
        player "剛剛那是啥？"
    elif wall_flag:
        play sound "SFX/door-slam.mp3" noloop volume 0.5
        player "趕上了"
    
    scene black with dissolve
    centered "隨著時間的推進，教室逐漸充滿了人們"


label choose_react:
    scene classroom with dissolve
    player "該找誰聊聊呢？"
    menu:
        "街上遇到的少女" if street_flag & a_notreacted:
            jump choose_a
        "做在一旁看書的少女" if wall_flag & a_notreacted:
            jump choose_a
        "我最可愛的青梅" if s_notreacted:
            jump choose_s
        "衝進來的那個人" if street_flag & w_notrecated:
            jump choose_w
        "幫了你的勝勝" if wall_flag & w_notrecated:
            jump choose_w

label choose_a:
    ""
    $ a_notreacted = 0
    jump choose_react
label choose_s:
    ""
    $ s_notreacted = 0
    jump choose_react
label choose_w:
    ""
    $ w_notrecated = 0
    jump choose_react
    return
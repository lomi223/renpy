label act1:
    play music "bird-chirping-sound-effect.mp3" loop fadein 0.3 volume 0.3
    scene black with dissolve
    centered "八月的尾聲即將到來，即將邁入秋色的風似乎更加喧囂了。青澀的少年渴望抓住夏天的尾巴、為青春開啟美好的篇章。" with fade
    
    scene bedroom with dissolve
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
            scene bedroom with dissolve
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
    window auto hide
    camera:
        subpixel True 
        parallel:
            pos (-150, 170) 
            linear 1.00 pos (-120, -120) 
            linear 0.60 pos (150, -70) 
            linear 0.80 pos (15, 100) 
        parallel:
            zpos -1100.0 
            linear 1.00 zpos -1100.0 
            linear 0.60 zpos -1100.0 
            linear 0.80 zpos -1100.0 
            linear 0.80 zpos -300.0 
    show a norm:
        zoom 0.2 
        xalign 0.5
        yalign 1.0
    with Pause(3.30)
    camera:
        pos (0, 0) zpos 0.0
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
    show w norm with dissolve:
        yalign 1.5
        xalign 0.5
    
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
        show s norm with dissolve:
            zoom 0.25
            yalign 1.5
            xalign 0.5
        "來到教室，你發現你的青梅碩碩已經座在位子上"
        player "早啊！碩碩"
        player "你也在這間學校啊！"
        "發現你的到來，碩碩靦腆的低下了頭"
        $ ss = "碩碩"
        show s shy with dissolve:
            zoom 0.25
            yalign 1.5
            xalign 0.5
        s "早......早阿[player]"
        hide s
        scene black with dissolve

        centered "正當你和碩碩聊得正歡時"
        scene classroom with dissolve
        play sound "SFX/walking_6QdYC8X.mp3"
        show a noticed with dissolve:
            subpixel True 
            matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
            zoom 0.28
            xpos 0.0
            parallel:
                linear 4.0 xpos 1.0
            parallel:
                linear 0.5 ypos -30
                pause 0.5
                linear 0.5 ypos 0
                pause 0.5
                linear 0.5 ypos -30
                pause 0.5
                linear 0.5 ypos 0
                pause 0.5
        pause 4.0
        hide a with dissolve
        pause 0.5
        player "是早上那個女孩！"
        player "他也在這裡"

        play sound "SFX/door-slam.mp3" noloop volume 0.5
        pause 1.0
        show w norm with dissolve:
            zoom 0.9
            yalign 1.5
            xalign 0.5
        w "剛好趕上"
        "突如其來的聲響嚇了你一跳"
        w "早啊！哥們"
        show w norm:
            linear 0.25 xpos 1.5
        pause 0.5
        hide w
        player "剛剛那是啥？"

    elif wall_flag:
        play sound "SFX/door-slam.mp3" noloop volume 0.5
        player "趕上了"
        s "哇！"
        "突如其來的聲響嚇到了一旁的同學"
        show s norm with dissolve:
            zoom 0.25
            yalign 1.5
            xalign 0.5
        player "碩碩！"
        player "沒想到會在這裡遇到妳"
        "碩碩，你的青梅，你們從小便是看著對方長大"
        "發現你的到來，碩碩靦腆的低下了頭"
        $ ss = "碩碩"
        show s shy with dissolve:
            zoom 0.25
            yalign 1.5
            xalign 0.5
        s "早......早阿[player]"
        scene black with dissolve
        centered "環視整間教室，[player]見到了......"
        scene classroom with dissolve
        show a reading with dissolve:
            zoom 0.25
            yalign 1.5
            xalign 0.5
        pause 0.5
        show a noticed with dissolve:
            zoom 0.25
            yalign 1.5
            xalign 0.5
        pause 0.5
        show a happy with dissolve:
            zoom 0.25
            yalign 1.5
            xalign 0.5
        pause 0.5
        hide a 
        player "啊......啊"
        player "很美~~~~阿"
        player "他媽的"
        player "好美......阿阿"
        "少女的微笑不斷勾引著[player]"
        "令[player]目不轉睛"



    scene black with dissolve
    centered "隨著時間的推進，教室逐漸充滿了人們"

label choose_react:
    scene classroom with Fade(0.5,1.0,0.5)
    player "該找誰聊聊呢？"
    
    menu:
        "街上遇到的少女" if street_flag & a_notreacted:
            jump choose_a
        "坐在一旁看書的少女" if wall_flag & a_notreacted:
            jump choose_a
        "躲在角落的青梅" if s_notreacted:
            jump choose_s
        "衝進來的那個人" if street_flag & w_notreacted:
            jump choose_w
        "幫了你的勝勝" if wall_flag & w_notreacted:
            jump choose_w
        "？？？" if b_canreact:
            jump choose_b
        "還是算了":
            jump night
            
label choose_a:
    scene black with dissolve
    "你選擇靠近那位少女"
    scene classroom with dissolve
    show a reading with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
    pause 0.5
    show a noticed with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
    menu:
        "嘿！同學，你好嗎":
            a "阿，那個......你好"
            $ a_love += 1

        "我愛你！！！":
            show a shocked
            a "蛤？"
            hide a with dissolve
            "少女害怕地跑開了"
            "你不小心從他桌上的書知道了他名叫Alex"
            "不小心的"
            $ aa = "Alex"
            $ a_love -= 1
            $ a_notreacted = 0
            jump choose_react

    menu:
        "聊聊戀愛話題":
            "從對話中，你了解到他名叫Alex"
            $ aa = "Alex"
            player "你有喜歡的人嗎？"
            a "抱歉，我目前沒有戀愛想法"
            $ a_love -= 1
            python:
                if (s_notreacted == 0 and w_notreacted == 1 and played_count == 2):
                    b_canreact = 1 

        "聊聊他看的書":
            player "你手上那本是最新一集的《鮑伯與你》嗎？"
            a "你也知道這本書？"
            player "是阿，我很喜歡"
            a "是喔"
            a "話說，你叫甚麼名字"
            player "我叫[player]"
            a "[player]啊......"
            show a happy with dissolve
            "少女的目光回到了書上，露出了迷人的微笑"
            a "很高興認識你，我叫Alex"
            $ aa = "Alex"
            $ a_tellingname = 1
            player "（他真的好可愛）"
            $ a_love += 1

    $ a_notreacted = 0
    jump choose_react

label choose_s:
    scene black with dissolve
    "你找到了碩碩"
    scene classroom with dissolve
    show s shy with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
    player "剛剛的聲音嚇到你了？"
    s "（微微點頭）"
    menu:
        "（摸摸頭）":
            player "沒事有我在"
            show s happy:
                zoom 0.25
                yalign 1.5
                xalign 0.5
            "碩碩低著的頭慢慢抬了起來，緊繃的情緒似乎比較緩和了"
            player "（好像摸太久了，該停下來了）"
            "當[player]準備將手收回時，碩碩突然輕輕握住了[player]的手"
            player "！？"
            player "（......好像貓咪）"
            player "還……要再摸一下嗎？"
            "碩碩撇開的側臉頓時滿臉通紅，他趕緊將[player]的手放開、再次逃離了現場"
            player "（......好可愛）"
            $ s_love += 1

        "笑死":
            show s sad:
                zoom 0.25
                yalign 1.5
                xalign 0.5
            "碩碩傷心的低下了頭，怎樣都不願理你"
            player "（好像生氣了）"
            $ s_love -= 1
            
    $ s_notreacted = 0
    jump choose_react

label choose_w:
    scene black with dissolve
    if street_flag:
        "你接近了衝進來的那個人"
    if wall_flag:
        "你接近了勝勝"
    scene classroom with dissolve
    show w norm with dissolve:
            zoom 0.9
            yalign 1.5
            xalign 0.5
    menu:
        "（熱情地打招呼）":
            if wall_flag:  
                player "嘿哥們！剛才真是謝了！"
                w "早安哥們！客氣什麼，小事一樁！"
                player "我是[player]，很高興認識你！"
                w "我之後會加入學校的足球隊，有機會記得來看看啊！"
                player "必須的"
            
            elif street_flag:
                player "早安哥們！你的動作也太快了！"
                w "被你發現了，我是有練過的！我是勝勝，你叫什麼名字？"
                $ ww = "勝勝"
                player "我是[player]很高興認識你！話說，你的動作好快，你有在運動嗎？"
                w "我喜歡踢足球！你對足球有興趣嗎？"
                player "沒有試過，但感覺很有趣！"
                w "沒關係，有機會我可以教你！"
                w "我之後會加入學校的足球隊，有機會記得來看看啊！"
                player "必須的"

            $ w_love += 1

        "（普通地打招呼）":
            player "你好啊"
            if wall_flag:
                w "喔嗨哥們，你是剛才的那個......"
                player "我是[player]，請多指教"
                player "你的動作好快，你有在運動嗎？"
                w "我喜歡踢足球！"
            elif street_flag:
                w "早啊哥們！"
                player "我是[player]，請問你是？"
                w "我是勝勝！我喜歡踢足球！"
            w "我之後會加入學校的足球隊，有機會記得來看看啊！"
            player "沒問題"

    $ w_notreacted = 0
    $ b_canreact = 0
    jump choose_react

label choose_b:
    stop music
    scene black with dissolve

    centered "你接̷̖̟̝͉̭̝̦̘̥̙̦̗̺̣͕̐̚近̶̢̛̺̞̦̺̣́̿͗̊́͂͑̊̾͘̚͝了̷̨̨̢̝̙̪̙͖̦̤̙͓͖̣̓̏̋͂̓̍̓ͅ.̵̳̏́̾.̷̘̟̠̤̇̔̊̀͑̎͋̚ͅ.̶̤̠̽̽̓̿̾̉̊.̵̛͍̞̜̭̩̫̯̩͌͌̑͛̋̈́ͅ"


    scene classroom with dissolve
    show bob norm with dissolve:
        zoom 0.3
        yalign 1.5
        xalign 0.5
        ypos 1.6
    label b_c:
        if repeat < 5:
            menu:
                "？":
                    $ repeat += 1
                    jump b_c
        else:
            hide bob
            show w norm:
                zoom 2.5
                xalign 0.5
                yalign 0.0
            pause 2.0
            play music "snowdin-town.mp3" loop volume 0.5
            show w norm:
                zoom 0.95
                yalign 1.5
                xalign 0.5
            
            w "你在跟誰說話啊哥們？"
            player "沒......沒事"
            $ b_love += 1
            $ b_canreact = 0
            jump choose_react

label night:
    stop music
    scene black with dissolve
    centered "第一天的課程忙碌地度過了，時間飛逝、太陽悄悄地溜向西邊，黃昏時分很快就到來了。"
    player "時間差不多了，回家吧。"
    
    show bedroom:
        subpixel True 
        matrixcolor TintMatrix("#18213b")*InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.5)*HueMatrix(0.0) 
    play music "night.mp3"
    $ ww = "勝勝"
    $ ss = "碩碩"
    $ aa = "Alex"
    "[player]將書包扔到了一旁，以「大」字形的姿勢向後躺到了床上"
    player "今天見到了好多人啊！"
    show s norm with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
    player "可愛又靦腆的[ss]"
    show s norm:
        linear 0.3 xalign 0.2
    show w norm with dissolve:
        zoom 0.95
        yalign 1.5
        xalign 0.5
    player "帥氣又熱情的[ww]"
    show w norm:
        linear 0.3 xalign 0.8
    show a norm with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
    player "還有[aa]......"
    "想這裡[player]不禁嚥了嚥口水"
    player "他真的好美啊......"
    scene black with Fade(1.0,0.0,0.0)
    "不知怎地，眼皮越來越沉重，回想著今天發生的一切，[player]就這麼進入了夢鄉"
    if b_love == 1:
        player "喔對還有那個人......"
        player "他究竟是誰？"
        jump dream
    jump act2

return
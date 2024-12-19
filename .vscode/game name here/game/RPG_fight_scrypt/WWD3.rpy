label WWDay3_morning :
    play music "bird-chirping-sound-effect.mp3" loop fadein 0.3 volume 0.3
    scene bedroom with Fade(0.5,1.0,0.5)
    "經歷了與勝勝的練習，你掙扎著痠痛的雙腿起床"
    "吃著早餐，你的手機傳來了一些簡訊"
    "1則未讀訊息"
    w "（最近天氣好熱喔，今天要不要翻出去吃點冰？）"
    player "..."
    player "感覺上高中就是要翻過幾次牆呢"
    scene black with dissolve
    jump WW_icefeast

label WW_icefeast:
    scene Wall with dissolve
    "走到牆邊，勝勝在向你招手" 
    show w norm with dissolve:
        zoom 0.9
        yalign 1.2
        xalign 0.5

    w "總算等到你了，幹什麼事情拖那麼久"
    menu:
        "剛剛有其他事，抱歉":
            w "爛，下次早點講啦"
        "肚子不太好，去炸了趟廁所":
            w "不知道為什麼有點反胃"
    w "總之，現在就出發吧"
    w "你力氣多大？手可以撐上去嗎？"
    player "感覺力氣不太夠..."
    w "不然我在下面撐著，你等一下用力點蹬上去"
    w "聽我數到3---"
    w "1"
    w "-"
    w "2"
    w "-"
    w "3"
    player "伊-"
    scene black with dissolve 
    player "啊--"
    player "哈啊--"
    player "嘶--"
    centered "經過一番掙扎，你成功抵達了牆外的世界"    
    show world_OutsideTheWall:
        subpixel True zoom 1.39 

    
    player "真令人著迷啊，牆外的世界"
    player "牆的另一端，是敵..."
    show w norm with moveinleft:
        zoom 0.9
        yalign 1.0
        xalign 0.2
    w "別廢話，動身去冰店吧！"
    scene black with dissolve
    
    
    scene icestore at center:
        xzoom 2.5
        yzoom 2
    play music "Dating Start!.mp3" loop volume 1.5

    show w norm_2 with dissolve:
        zoom 0.2
        yalign 1.5
        xalign 0
    w "這家很像份量還蠻大的，你不介意共吃一碗吧？"
    menu:
        "還真的蠻介意的？":
            w "真是不留情面..."
        "沒關係，我們就共吃一碗吧！":
            show w chill with dissolve:
                zoom 0.2
                yalign 1.5
                xalign 0
            w "那就這麼決定了！"
            $ shareice += 1
    show w norm_2
    w "那你有喜歡吃什麼口味嗎?"
    menu:
        "這個看起來不太起眼的黑糖剉冰":
            show w chill with dissolve:
                zoom 0.2
                yalign 1.5
                xalign 0
            w "看起來不錯，我也喜歡爆炒黑糖"
        "這個季節限定的醬油蒸蛋口味雪花冰":
            show w shy with dissolve:
                zoom 0.2
                yalign 1.5
                xalign 0
            w "雖然是季節限定，但這東西還真倒胃口..."
    scene black with dissolve
    scene dining_area at center:
        xzoom 3.6
        yzoom 3
    "點完餐後，你們走到了旁邊的座位區"
    "店內的空間雖小，卻很熱鬧"
    "周圍似乎擠滿了也是翻牆出來的人"
    "延續昨天的話題，你在跟勝勝爭論"
    show w norm_2 with dissolve:
        zoom 0.2
        yalign 1.5
        xalign 0.5
    "--"
    "女僕到底要不要帶著貓耳？"
    "聽著有點莫名其妙，但是你們正相當認真地辯駁這個問題"
    w "我就說了，貓耳戴在女僕的身上根本是對貓咪的褻瀆!"
    player "才不是呢，不覺得多了那副貓耳，讓人有種無法抗拒的魅力嗎？"
    show w mad with dissolve:
        zoom 0.2
        yalign 1.5
        xalign 0.5
    w "那[player]你是說，我如果戴上了貓耳，也會讓你招架不住囉？"
    player "..."
    w "..."
    "意識到勝勝也許不是在開玩笑，你陷入了短暫的沈默"
    player "..."
    player "呃..."
    menu:
        "才不是呢，貓耳只有套在女僕上才能發揮他的魅力！":
            w "哼，那就是你不懂的欣賞了"
        "其實那副耳朵也蠻適合你的":
            w "..."
            show w shy with dissolve:
                zoom 0.2
                yalign 1.5
                xalign 0.5
            w "這..."
            w "謝謝你對我的認可？"
            w "..."
            show w chill with dissolve:
                zoom 0.2
                yalign 1.5
                xalign 0.5
            w "有機會會考慮的"
    "隨著你們的激辯，冰也送上來了"
    if(shareice == 1):
        call shareice_version
    else:
        call normalice_version
    "吃完挫冰之後，你們外帶了一份豆花回去"
    "冰很美味，翻牆出來的經驗也很新奇"
    "你好奇今天還會發生什麼有趣的事"
    w "那我們走原路回去囉？"
    scene black with dissolve
    scene Wall with dissolve
    "第二次的翻牆，你顯得駕輕就熟"
    show w norm_2 with dissolve:
        zoom 0.2
        yalign 1.5
        xalign 0.5
    w "走吧，還要回去趕-"
    pr "你們在那邊做什麼！"
    pr "給我去校長室報到"
    scene FogWall with Fade(1,1,1)
    stop music
    play music "barrier.mp3"
    show w norm with dissolve:
        zoom 0.9
        xalign 0.5
        yalign 1.0
    w "哥們，這看起來十分不妙"
    w "你準備好了嗎？"
    menu:
        "走吧":
            $ quick_menu = False
            scene black with Fade(1,1,1)
            pass
    jump boss_fight

label shareice_version:
    show w norm_2 with dissolve:
        zoom 0.2
        yalign 1.5
        xalign 0.5
    w "跟你說了吧，他的量真的很大"
    menu:
        "這點量對我來說才不算什麼":
            w "這麼自信，你等等就不要吃不下"
        "希望等一下不會吃不完...":
            w "吃不完還可以打包！不用擔心"
            player "打包啥...糖水嗎？"
    "勝勝挖起了一匙冰"
    "望向了你"
    show w shy with dissolve:
        zoom 0.2
        yalign 1.5
        xalign 0.5
    "他看起來有什麼話要說"
    w "呃..."
    w "[player]"
    hide w
    show w mad with moveinbottom
    pause (1.0)
    w "啊--"
    "..."
    player "（含）"
    w "好吃嗎"
    "看起來是第一次餵別人吃冰，勝勝的動作在此時看起來有些僵硬"
    menu:
        "好吃":
            show w chill with dissolve:
                zoom 0.2
                yalign 1.5
                xalign 0.5
            w "就說吧，我推的店準好吃"
        "讓你喂，變得更好吃了":
            show w chill with dissolve:
                zoom 0.2
                yalign 1.5
                xalign 0.5
            w "那，要不要再吃一口？"
            player "不用...剛那口就快把我嚇死了"
    return

label normalice_version:
    "冰上來了，你們很正常的吃著你們自己點的冰"
    "冰是挺好吃的"
    "但你總覺得少了什麼"
    return

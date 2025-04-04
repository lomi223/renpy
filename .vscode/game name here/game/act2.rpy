label act2:
    play music "bird-chirping-sound-effect.mp3" loop fadein 0.3 volume 0.3
    if b_love == 1:
        jump bob_morning
    jump morning

label morning:
    scene bedroom with Fade(0.5,1.0,0.5)
    player "看來今天也是美好的一天呢！"
    scene classroom with Fade(0.5,1.0,0.5)
    play music "snowdin-town.mp3" loop volume 0.5
    play sound "SFX/door-slam.mp3" noloop volume 0.3
    "[player]來到了教室"
    show s norm with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
    player "碩碩，早安"
    s "！"
    "碩碩突然抬起頭來"
    "看到是你，似乎鬆了一口氣"
    show s happy with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
    s "早……早安"
    hide s norm with dissolve
    show w norm at comein(0.5,0.1):
        yalign 1.5
        zoom 0.9
    w "嘿哥們！早啊！"
    player "勝勝！早啊"
    w "我等等有比賽，等等記得來看我！"
    "經勝勝提醒，你想起來今天上午似乎是校園認識活動"
    "學生們可以到處參觀、走訪校園"
    player "必須的"
    show w at goout(0.1)
    "勝勝飛快地離開了教室"
    hide w norm
    "此時，那位美女恰巧進來了教室"
    play sound "SFX/door-slam.mp3" noloop volume 0.3
    show a norm with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
    "空氣中彷彿多了一點莓果的香氣，使你整個人都清爽了起來"
    if a_tellingname:
        player "啊，Alex，早安"
        a "早啊，[player]"
    hide a norm with dissolve
    player "離活動開始還有一段時間，稍微睡一下好了……"
    
    scene classroom with Fade(0.5,1.0,0.5)
    play music "bird-chirping-sound-effect.mp3" loop fadein 0.3 volume 0.3
    "你睡了一覺，精神似乎變好了"
    "醒來後，教室裡的人已經寥寥無幾"
    player "我也去逛逛學校好了。"

label choose_scene:
    play music "snowdin-town.mp3" loop volume 0.5
    scene classroom with dissolve
    if day2_count == 2:
        "時間很晚了，充實的一天也這麼結束了。"
        jump day2_night
    player "接下來我該去哪呢？"
    menu:
        "去球場看看" if sportfield_reacted == 0:
            jump w_soccer
        "去圖書室看看" if library_reacted == 0:
            jump a_reading
        "隨處晃晃" if go_around_reacted == 0:
            jump s_cat

label w_soccer:
    play music "summer_storm.mp3" loop volume 0.5
    scene sport_field with Fade(0.5,1.0,0.5):
        zoom 2.70
    "你慢慢靠近球場，人開始多了起來"
    "許多新生聚集到了此處，觀看著高年級的學生們揮灑汗水"
    "不遠處的足球場旁更是擠滿了人"
    player "足球？我記得勝勝好像有比賽的樣子，過去看看吧。"
    player "不好意思，借我過一下"
    "你使盡全力，才稍微擠進那群學生中"
    show w norm with dissolve:
        zoom 0.9
        yalign 1.5
        xalign 0.5
    show w norm with dissolve:
        zoom 0.9
        yalign 1.5
        xalign 0.5
        linear 1 xalign 0.2
    show w norm with dissolve:
        zoom 0.9
        yalign 1.5
        xalign 0.5
        linear 1 xalign 0.85
    "仔細一看，勝勝正快速地在球場上穿梭"
    play sound "SFX/cheering.mp3" noloop volume 0.3
    player "對面選手的有穿學校球衣，應該都是高年級吧？"
    "儘管對手是高年級，勝勝仍不落下風"
    "他敏捷的動作令所有人為之驚嘆，精準的傳球驚詫了周邊的所有人"
    "很快，勝勝便找到了機會，一發射門——"
    "如此刺激，使你險些忘記了呼吸"
    show w norm with dissolve:
        zoom 0.9
        rotate 0
        parallel:
            linear 0.5 yalign 1.5
        parallel:
            linear 0.5 xalign 0.5
        parallel:
            linear 1 rotate 360
    play sound "SFX/ball_kick.mp3" noloop volume 0.8
    play sound "SFX/cheering_2.mp3" noloop volume 1
    "完美的倒鉤！全場立刻爆發出歡呼聲"
    player "勝勝！太帥了！"
    "勝勝聽見你的聲音，眼神立即與你對上"
    "他露出了燦爛的笑容，你懷疑，那光芒能夠與太陽比肩"
    "比賽在歡聲中落幕，勝勝所帶領的隊伍毫無疑問拿下了勝利"
    "人群漸漸散開，勝勝在此時找到了你"
    w "[player]！你覺得我剛剛那一球怎麼樣！"
    menu:
        "帥麻了，可惜不能再站近一點。":
            w "讚啦，就知道你會喜歡！"
            w "以後隨時都可以來找我，有機會也教你踢球！"
            $ w_love += 1
        "還不賴。":
            w "謝啦。"
            w "以後有機會也來踢球吧。"
    show w chill with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
        ypos 1.75        
    "勝勝換上了日常服裝，你們在操場上閒聊著"
    show w norm_2 with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
        ypos 1.75
    "你們之間的話題不斷，大部分是有關運動的"
    "還有肌肉、女僕跟電動"
    "談話間，勝勝突然拉著你往旁邊一步"
    show w norm_2 with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
        ypos 1.75
        linear 0.5 xalign -0.5
    "飛身向前、為你擋住了天外飛來的排球"
    play sound "SFX/ball_kick.mp3" noloop volume 0.3
    show strong_guy with dissolve:
        zoom 3
        yalign 1.5
        xalign 0.5
        ypos 1.85
        xpos 1.15
        linear 0.5 xalign 0.8  

    npc_black "對不起！沒注意力道"
    w "沒事，我們都沒有受傷"
    "勝勝回頭望向你，似乎在等待著你說些什麼"
    menu:
        "謝謝勝勝！嚇死我了！":
            "勝勝的臉微微泛紅，你們之間僵住了一小會兒"
            show w shy with dissolve:
                zoom 0.25
                yalign 1.5
                xalign 0.5
                ypos 1.75
                xpos 0.2
            w "沒……沒事就好"
            $ w_love += 1
        "我去，這球有夠危險。":
            show w mad with dissolve:
                zoom 0.25
                yalign 1.5
                xalign 0.5
                ypos 1.75
                xpos 0.2
            w "……沒事就好！"
    hide strong_guy with dissolve
    show w norm_2 with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
        ypos 1.75
    "你們一起參觀了許多運動社團"
    show tall_guy with dissolve:
        yalign 1.5
        xalign 0.5
        ypos 2036
        xpos 0.8
    npc_tall "歡迎加入籃球隊喔！"
    show weak_guy with dissolve:
        zoom 2.8
        yalign 1.5
        xalign 0.5
        ypos 1.75
        xpos 0.2
    npc_weak "不介意的話，可以來桌球部看看喔……"
    "學生們的吆喝聲此起彼落"
    "勝勝似乎很喜歡這種熱鬧的氣氛"
    "你的嘴角也不自覺上揚了些"
    hide tall_guy with dissolve
    hide weak_guy with dissolve
    "你們漫步在運動場上，有時被勝勝拉走、去看看一些有趣的攤子"
    "有時只是單純聊著天"
    scene soccer_field with Fade(0.5,1.0,0.5):
        zoom 1.5
    show w norm_2 with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
        ypos 1.55
    "你們最後坐在了足球場旁的板凳上，這時，勝勝不知從哪裡搞來了一顆足球"
    show soccer with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
        ypos 0.41
        xpos 937
    "他將球頂在頭上，秀著一些你看不懂的技巧與招式"
    hide soccer
    show w norm_2 with dissolve:
        zoom 0.25
        rotate 0
        parallel:
            linear 0.5 yalign 1.5
        parallel:
            linear 0.5 ypos 1.75
        parallel:
            linear 0.5 xalign 0.5
        parallel:
            linear 1 rotate 360
    show soccer with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
        ypos 0.78
        xpos 955
        linear 0.3 xpos 2071
    show w norm_2 with dissolve:
        rotate 0
        zoom 0.25
        yalign 1.5
        xalign 0.5
        ypos 1.75
        linear 0.2 xpos 0.85
    show soccer with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
        ypos 0.78
        xpos 2071
        linear 0.3 xpos -116
    show w norm_2 with dissolve:
        rotate 270
        zoom 0.25
        yalign 1.5
        xalign 0.5
        xpos 0.75
        ypos 2.00
        linear 0.1 ypos 1.35
    show soccer with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
        ypos 0.78
        xpos -116
        linear 0.3 xpos 2071
    show w norm_2 with dissolve:
        rotate 180
        zoom 0.25
        yalign 1.5
        xalign 0.5
        xpos 0.9
        ypos 1.3
        linear 0.2 xpos 0.1
    show soccer with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
        ypos 0.78
        xpos 2071
        linear 0.3 xpos -116
    show w norm_2 with dissolve:
        rotate 90
        zoom 0.25
        yalign 1.5
        xalign 0.5
        xpos 0.1
        ypos 1.33
        linear 0.1 ypos 2.0
    show soccer with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
        ypos 0.78
        xpos -116
        linear 0.3 xpos 2071
    show w norm_2 with dissolve:
        zoom 0.25
        rotate 0
        parallel:
            linear 0.5 yalign 1.5
        parallel:
            linear 0.5 ypos 1.75
        parallel:
            linear 0.5 xalign 0.5
        parallel:
            linear 1 rotate 360
    show soccer with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
        parallel:
            linear 0.5 ypos 0.48
        parallel:
            linear 0.5 xpos 937
        parallel:
            linear 1 rotate 360
    "看起來有些滑稽，但你知道，這些動作絕不是簡簡單單能辦到的"
    w "[player]還有一些時間，你要來體驗一下足球嗎？"
    play music "flower_dance.mp3" loop volume 0.5
    menu:
        "打！肯定打！":
            w "這就對了！"
            "勝勝將你一把拉起，興高采烈地跟你介紹起了簡單的動作與腳法"
            "你有些不適應，但勝勝耐心地在一旁指導你"
            hide soccer with dissolve
            "過了一段時間，你也開始能夠做出基本的踢、傳球了"
            "你與勝勝在炎熱的太陽下踢著球"
            "彷彿忽視了旁人"
            "世界好像只剩下你們兩人"
            scene black with dissolve
            centered "經費不足，所以沒有cg"
            scene bench with dissolve:
                zoom 2.5
            "不知過了多久，你們兩個都累壞了"
            "你坐在板凳上喘著氣，此時勝勝向你遞來了飲料"
            show w norm_2 with dissolve:
                zoom 0.4
                yalign 1.5
                xalign 0.5
                ypos 2.25
            w "我喝過了，你用倒的吧"
            player "沒事，我不介意"
            "你們兩人坐在球場旁，就著麼看著場上的運動員們"
            "勝勝的肌膚輕貼著你，你沒有開口說話"
            "你們保持著曖昧的距離，就這麼持續著好一陣子"
            w "時間差不多了，我得去找球隊朋友吃飯！"
            "勝勝撇過頭去，你卻能清楚地看見他泛紅的臉頰"
            show w shy with dissolve:
                zoom 0.4
                yalign 1.5
                xalign 0.5
                ypos 2.25
            player "嗯！路上小心，掰掰！"
            $ w_love += 1
            $ day2_count += 1
            $ sportfield_reacted = 1
            jump choose_scene
        "先不要……":
            show w mad with dissolve:
                zoom 0.4
                yalign 1.5
                xalign 0.5
                ypos 2.25
            w "……好吧，以後有機會也是可以。"
            player "嗯。"
            "你們之間的氣氛變得有些尷尬"
            w "我該去跟球隊的朋友吃飯了，晚點見。"
            "勝勝很快跑遠了"
            $ day2_count += 1
            $ sportfield_reacted = 1
            jump choose_scene

label a_reading:
    play music "Holiday.mp3" loop volume 0.5
    scene stair with dissolve:
        zoom 2.55   
        ypos -0.21    
    "你來到了另一棟教學大樓"
    "這裡大部分是社團教室、老師辦公室"
    "也許是新生歡迎活動的緣故，這裡的人非常少"
    "一陣風吹過，微風挾帶著花瓣迎面而來"
    "帶來一股清新的香氣，這讓你想到了Alex"
    scene hallway with dissolve
    "這時，你注意到了一間門打開的教室"
    "上頭的牌子寫著「圖書室」"
    "你好奇地往裡頭走去"
    scene library with dissolve:
        zoom 2.55  
        ypos -0.21
    "進入了一個由書香與文藝氣息充斥的空間，你的心情似乎寧靜了下來"
    "又一股風吹過，你向前一看，那柔順的秀髮飄逸著、熟悉的莓果香氣再次出現"
    scene library_2 with dissolve:
        zoom 2.8
        ypos -522
    show a reading with dissolve:
        zoom 0.33
        xpos 486
    "是Alex，他端正地坐在窗戶旁的那木桌旁"
    "他的裙襬微微被風吹地搖動，你被他的美貌驚詫到了"
    "他正專注地看著手上的書，似乎沒注意到你的到來"
    player "（我現在該幹嘛？）"
    menu:
        "先靜靜地等著，不要打斷他" :
            "你就這麼靜靜地看著，你在這裡觀察到了他不同於平時的表情"
            show a happy with dissolve:
                zoom 0.33
                xpos 486
                ypos -216
            "他時而抿起嘴、似乎感到憤懣"
            show a noticed with dissolve:
                zoom 0.33
                xpos 486
                ypos -225
            "又時而露出淺淺地微笑"
            "過了一陣子，他總算暫時停下手邊的動作"
            "他終於注意到了你，一瞬間，他露出了驚訝的表情"
            show a shocked with dissolve:
                zoom 0.33
                xpos 486
                ypos -225 
            a "啊？"
            show a norm with dissolve:
                zoom 0.33
                xpos 423
                ypos -216
            if a_tellingname:
                a "[player]？你怎麼在這裡……不，你不會一直站在那邊看我吧！！"
            else:
                player "啊，我是[player]，如果嚇到你了我很抱歉。"
                a "你……不會一直站在那邊看我吧！！"
            player "我想說不要打擾到你……"
            "聽到你這麼說，Alex的表情僵了一下"
            a "噗哧"
            show a noticed with dissolve:
                zoom 0.33
                xpos 486
                ypos -225
            player "！？"
            a "哈……哈哈哈！"
            "Alex突然笑了起來，他美麗動人的笑容讓你的心跳加速"
            a "你也太可愛了吧！直接叫我不就好了嗎？"
            "你羞紅了臉，有些說不出話來"
            show a norm with dissolve:
                zoom 0.33
                xpos 423
                ypos -216
            a "不過這邊的劇情的確很精彩，謝謝你啦！"
            if a_tellingname == 0:
                a "你真有趣！叫我Alex就可以了！"
            a "你找我有什麼事嗎？"
            $ a_love += 1
        "直接開口打招呼":
            if a_tellingname:
                player "Alex？"
                "Alex被突然的聲音嚇了一跳"
                a "[player]？你怎麼會在這裡？"
                player "到處晃晃，就到這裡來了。"
                a "這樣啊……"
            else: 
                player "同學？"
                "Alex被突然的聲音嚇了一跳"
                player "啊，不好意思，我還沒自我介紹。"
                player "我是[player]，請多多指教！"
                show a noticed with dissolve:
                    zoom 0.33
                    xpos 486
                    ypos -225
                "Alex深吸了一口氣，臉上綻開了燦爛的微笑。"
                a "你真有趣！叫我Alex就可以了！"
                show a norm with dissolve:
                    zoom 0.33
                    xpos 423
                    ypos -216
                a "話說，你找我有什麼事嗎？"
    player "那本書……是？"
    show a reading with dissolve:
        zoom 0.33
        xpos 486
        ypos -27
    a "是《喃喃戀愛奇譚》喔，我很喜歡這本書的作者。"
    a "他的作品還有《大綱紅閃耀的鸚鵡》、《鮑勃！！！》"
    a "我特別喜歡後者的其中一篇小說，叫做〈捲乙己〉"
    a "裡面的寓意與巧思很令人驚嘆呢！"
    a "啊啊，記得念《鮑勃！！！》書名的時候要用喊的喔，這是讀者們的共識呢！"
    "Alex滔滔不絕地說著，你努力記住了其中的細節"
    show a norm with dissolve:
        zoom 0.33
        xpos 423
        ypos -216
    "在一陣資訊轟炸後，Alex停了下來，看著你的眼睛"
    "他似乎在等著你說些什麼"
    menu:
        "努力將你想到的東西全部講出來":
            player "哦哦！鸚鵡那個故事我好像知道！"
            player "我很喜歡主角群奮力抵抗敵人砲火的那段劇情"
            player "雖然沒有完整看過《鮑勃！！！》，但〈捲乙己〉的故事很有名！"
            "在唸出《鮑勃！！！》的時候，你努力地用接近吶喊的方式喊出"
            "Alex摀住了嘴巴，但藏不住他眼中的笑意"
            show a noticed with dissolve:
                    zoom 0.33
                    xpos 486
                    ypos -225
            a "你該不會都偷偷把我的話記起來了吧？"
            player "這個……不能算偷！讀書人的事，能算偷麼？"
            "Alex終於掩蓋不住笑容，輕聲地笑了起來"
            show a happy with dissolve:
                zoom 0.33
                xpos 486
                ypos -216
            $ a_love += 1
        "誠實告訴Alex你啥都沒聽懂":
            player "抱歉，其實我沒有全部聽懂"
            a "嗯嗯，沒關係。"
    show a norm with dissolve:
        zoom 0.33
        xpos 423
        ypos -216
    "你們之間的火熱氣氛漸漸趨緩，兩人都沒有要開口的意思，而此時…… "
    a "那個，[player]，你要不要來看看這本書，我覺得你可能會喜歡。"
    play music "AIR_poem_of_birds.mp3" loop volume 0.5
    "Alex坐回木桌，輕輕向你招手。"
    "潔白的窗簾被風吹得輕輕晃動，陽光灑在Alex的臉龐上"
    "「那是天使吧？」你在心中這麼呼喊著"
    "而「天使」正在等待你的答覆"
    menu:
        "坐到Alex的旁邊":
            show a reading with dissolve:
                zoom 0.47
                xpos 279
                ypos -135
            "你戰戰兢兢地坐到了Alex旁邊的位置，他身上的梅果氣味更加明顯了"
            "圖書室很安靜，安靜到你能清楚地聽見Alex的呼吸"
            "心跳聲正在加速，希望Alex不會聽見"
            a "那……我要開始翻頁囉。"
            player "好。"
            "翻頁聲迴繞在圖書室中，書放置在你們兩人之間，你們一人一邊、扶著書的兩側"
            "這個角度讓你能夠清楚地看見Alex白皙的手"
            a "看好了嗎？我要翻頁囉？"
            "Alex的聲音打斷了你的恍神"
            player "啊，再一下下……"
            a "好。"
            "你意識到不能這樣發呆了，開始加速閱讀《喃喃戀愛奇譚》"
            "這本書是關於一個封閉自己內心多年的男孩的故事"
            "他對班上的一位女孩子心生情愫，卻因為同學的嘲弄與玩笑而隱藏起來"
            "當他終於鼓起勇氣、對女孩表達了自己的愛意"
            "卻換來性騷擾警告與社會性死亡"
            "最終被孤立、發誓再也不會喜歡上女生"
            player "（？？？這三小劇情）"
            "此時，一旁隱隱約約傳來啜泣聲，你撇眼一看，Alex的眼淚悄然從臉頰滑落"
            show cry with dissolve:
                zoom 0.14
                ypos 0.33
                xpos 0.48
            "他的肩膀輕輕依靠著你，他自己卻沒有自覺"
            "你仔細一看，Alex竟靠在你的肩膀上睡著了"
            "你決定不多說什麼，就這麼靜靜地待在他身邊"    
            "這時，你的眼皮也開始沉重了起來……"
            scene library_2 with Fade(0.5,1.0,0.5):
                zoom 2.8
                ypos -522
            show a reading with dissolve:
                zoom 0.47
                xpos 279
                ypos -135
            "過了一段時間，你終於醒了過來"
            "Alex仍然坐在那邊，翻動著書頁"
            "你的肩膀上卻多出了一件外套"
            player "香香的……"
            show a happy with dissolve:
                zoom 0.75
                xpos -198
                ypos -738
            a "[player]！你醒了啊！"
            "醒來後迎接你的是Alex美麗動人的微笑"
            a "時間不早囉，也差不多該離開了"
            player "喔喔，好，那就在這邊道別吧"
            a "掰掰，明天見。"
            player "掰掰……"   
            $ a_love += 1
            $ day2_count += 1
            $ library_reacted = 1
            jump choose_scene

        "坐到Alex的對面":
            show a reading with dissolve:
                zoom 0.27
                xpos 522
                ypos 18
            a "啊，那就……"
            "Alex把書轉了一邊，你們一人一邊、扶著書的兩側"
            "圖書室很安靜，安靜到你能清楚地聽見Alex的呼吸"
            "心跳聲正在加速，希望Alex不會聽見"
            "你們兩人度過了一段尷尬的時光"
            a "時間不早囉，也差不多該離開了"
            player "喔喔，好，那就在這邊道別吧"
            a "掰掰，明天見。"
            player "掰掰……"  
            $ day2_count += 1 
            $ library_reacted =1
            jump choose_scene

label s_cat:
    play music "Hotel.mp3" loop volume 0.5
    scene hallway with dissolve
    "你遊蕩在走廊上，漫無目的地在校園中走著"  
    "時而經過社團教室，悠揚的樂音傳入你的耳中" 
    "就這麼繞著繞著，你來到了校園的某個角落"
    scene corner with dissolve:
        zoom 2.4
    "此時，一聲突兀的貓叫聲驚動了你" 
    "緊接著那個貓叫聲、是另一聲比較輕柔的貓叫"
    "你開始感到有些好奇了，你開始四處尋找貓咪的蹤跡"
    "來到了舊校舍後的涼亭附近，你看見了……"
    show s norm with dissolve:
        zoom 0.25 
        xpos 252 
        ypos 72
    show cat with dissolve:
        zoom 1.72
        xpos 0.53 
        ypos 0.61
    play sound "SFX/cat_meow.mp3" noloop volume 0.3
    "碩碩與一隻黑貓正在互相喵喵叫著"
    "碩碩似乎還沒注意到你"
    "應該要怎麼辦？"
    menu:
        "就這麼看著碩碩":
            "碩碩背對著你，他嬌小的身軀蹲在了涼亭欄杆旁邊、與貓咪激烈對話著"
            s "喵喵喵？喵喵！"
            "可不知怎地，貓咪的眼神竟飄到了你身上"
            "碩碩向後一看"
            hide cat
            show s sad with dissolve:
                zoom 0.25 
                xpos 603 
                ypos 72
            "你們兩人之間只剩下了沉默"
            s "嗚……嗚嗚……"
            "碩碩失落地看著地面、在地上劃著圈圈，似乎馬上眼淚就要滴下來了"
            player "別……別哭啊！我覺得很可愛，所以完全沒有問題！！"
            "聽到這話，碩碩似乎多了一些精神"
            show s happy with dissolve:
                zoom 0.25 
                xpos 603 
                ypos 72
        "跟著一起喵喵叫":
            "碩碩背對著你，他嬌小的身軀蹲在了涼亭欄杆旁邊、與貓咪激烈對話著"
            play sound "SFX/cat_meow.mp3" noloop volume 0.3
            player "喵……喵？"
            "真是一隻蒼老的貓咪"
            "碩碩向後一看"
            hide cat
            show s sad with dissolve:
                zoom 0.25 
                xpos 603 
                ypos 72
            "你們兩人之間只剩下了沉默"
            s "嗚……嗚嗚……"
            "碩碩失落地看著地面、在地上劃著圈圈，似乎馬上眼淚就要滴下來了"
            player "別……別哭啊！我覺得很可愛，所以完全沒有問題！！"
            show s happy with dissolve:
                zoom 0.25 
                xpos 603 
                ypos 72
            "聽到這話，碩碩似乎多了一些精神"
            $ s_love += 1
    s "這……這隻貓咪很可愛，你要不要也來跟牠說說話？"
    player "貓咪嗎？我看看……"
    "此時，你發現原本待在欄杆上的貓咪突然消失了"
    s "！？"
    "碩碩無法掩蓋內心的慌張，似乎又要像剛才那樣自閉了"
    show s sad with dissolve:
                zoom 0.25 
                xpos 603 
                ypos 72
    player "不緊張，小問題！我們一起去找牠！"
    s "（點點頭）"
    scene sport_field with Fade(0.5,1.0,0.5):
        zoom 2.70
    "你們先來到了操場，越靠近運動場，人漸漸多了起來"
    play sound "SFX/crowd_noise.mp3" noloop volume 0.5
    show tall_guy with dissolve:
        yalign 1.5
        xalign 0.5
        ypos 2036
        xpos 0.8
    show weak_guy with dissolve:
        zoom 2.8
        yalign 1.5
        xalign 0.5
        ypos 1.75
        xpos 0.2 
    show s norm with dissolve:
        zoom 0.25 
        xpos 567 
        ypos 72
    player "那貓咪很親近人，有可能會來這裡嗎？"
    player "果然還是得去找一下！"
    menu:
        "緊緊抓住碩碩的手，往人群裡走": 
            show s norm with dissolve:
                zoom 0.4 
                xpos 324 
                ypos -198
            hide tall_guy with dissolve 
            hide weak_guy with dissolve
            "你握住了碩碩的手腕、帶著他在操場周圍尋找貓咪的蹤跡。"
            player "這裡人好多，我們往這邊走！"
            "人群的推擠並沒有將你們分開，反倒是碩碩反過來緊緊牽住了你的手"
            show s shy with dissolve:
                zoom 0.4 
                xpos 324 
                ypos -198
            s "……"
            player "!!!"
            "你們兩人一言不發，就這麼一起走著"
            $ s_love += 1
        "讓碩碩拉住衣角，往人群裡走": 
            show s norm with dissolve:
                zoom 0.4 
                xpos 324 
                ypos -198
            hide tall_guy with dissolve 
            hide weak_guy with dissolve
            "碩碩默默跟在你的身旁，不發一語"
    "過了好一陣子，你們愣是沒有看見任何貓咪的蹤跡。"
    "碩碩低下了頭，似乎在消沉著。"
    show s sad with dissolve:
                zoom 0.4 
                xpos 324 
                ypos -198
    player "……沒事的！我們去其他地方看看！"
    scene hallway with dissolve
    show s norm with dissolve:
        zoom 0.26
        xpos 558 
        ypos 72
    stop sound
    play music "Memory.mp3" loop volume 0.5
    "你們遊蕩在校園的各處，陽光灑落走廊，時空彷彿凝結在此刻"
    "遠方的人聲被你們的腳步聲所覆蓋，只得隱隱地傳到教學樓來"
    "你們之間的距離十分曖昧，你稍微瞄了碩碩一眼。"
    show s shy with dissolve:
        zoom 0.26
        xpos 558 
        ypos 72
    "他露出了羞赧的表情，不管幾次，那模樣總能吸引住你的目光"
    "明明像隻令人想要守護的小貓咪。"
    "從你跟他相處多年的時光來看，你卻明白碩碩纖細而堅強的心靈。"
    show s happy with dissolve:
        zoom 0.26
        xpos 558 
        ypos 72
    "他的話語與鼓勵總能一次次讓你振作起來。"
    "此時，你注意到碩碩的臉頰似乎變得更紅了。"
    player "（被發現在偷看他了）"
    hide s with dissolve
    "你尷尬地撇開了臉頰，卻又想著再偷偷瞄一眼"
    player "（再……再一眼就好！）"
    "衝了！"
    show s happy with dissolve:
        zoom 0.26
        xpos 558 
        ypos 72
    "結果是，令人尷尬的四目相對"
    show s shy with dissolve:
        zoom 0.26
        xpos 558 
        ypos 72
    "你們兩人同時把臉撇開，這大概也是你們多年的默契吧。"
    "過了一段時間，你們再次回到了最初的那個角落"
    scene corner with dissolve:
        zoom 2.4
    "碩碩坐到了涼亭的石椅上，似乎是難過地低下了頭"
    show s sad with dissolve:
                zoom 0.25 
                xpos 603 
                ypos 72
    player "（我應該要怎麼辦？）"
    menu:
        "安慰他":
            player "……碩碩，沒事的，我們才來到這裡沒多久"
            player "搞不好還有很多見到貓咪的機會，對吧？"
            s "嗚，我……"
            player "不然我們去加入流浪動物社？這樣就可以看到很多可愛小動物了！"
            "碩碩聽到這句話，眼睛馬上亮了起來。"
            show s happy with dissolve:
                zoom 0.25 
                xpos 603 
                ypos 72
            s "我其實……只是想要跟你創造多一點回憶而已……"
            "喔Damn，心臟暴擊"
            player "原來是這樣！那就更沒問題了！"
            show s sad with dissolve:
                zoom 0.25 
                xpos 603 
                ypos 72
            s "那時候你去了別的國中，我真的好害怕……"
            s "我怕我再也見不到你了……"
            "一陣風吹過，你們兩人再次四目相會，可這次，你們卻直直注視著彼此"
            show s happy with dissolve:
                zoom 0.25 
                xpos 603 
                ypos 72
            player "見到你，我真的很高興，碩碩。"
            "你們就這麼看著彼此的雙眼，持續了好一陣子。"
            "此時"
            play sound "SFX/cat_meow.mp3" noloop volume 0.3 
            "喵——喵嗚"
            show s shy with dissolve:
                zoom 0.25 
                xpos 252 
                ypos 72
            show cat with dissolve:
                zoom 1.72
                xpos 0.53 
                ypos 0.61
            
            s "！？"
            player"！出現了！"
            "貓咪再次出現在你們眼前，就在離你一隻手臂不到的距離"
            s "趁……趁現在！"
            player "哦！"
            "你輕輕撫摸了牠的頭，毛毛的，軟軟的，果然很好摸"
            show s happy with dissolve:
                zoom 0.25 
                xpos 603 
                ypos 72
            "你與碩碩相視一笑，度過了一段悠閒的時光"
            "你們相談了許久"
            "回憶起許多之前的事情"
            "此刻你感到無比安心"            
            $ s_love += 1
            player "啊！時間不早了，我得走了！"
            s "嗯，掰掰。"
            $ day2_count += 1
            $ go_around_reacted = 1
            jump choose_scene


        "就這麼看著":
            "你不知道該說些甚麼，就這麼看著碩碩"
            "此時"
            play sound "SFX/cat_meow.mp3" noloop volume 0.3
            "喵——喵嗚"
            s "！？"
            show s shy with dissolve:
                zoom 0.25 
                xpos 252 
                ypos 72
            show cat with dissolve:
                zoom 1.72
                xpos 0.53 
                ypos 0.61
            
            player"！出現了！"
            "貓咪再次出現在你們眼前，就在離你一隻手臂不到的距離"
            s "趁……趁現在！"
            player "哦！"
            "你輕輕撫摸了牠的頭，毛毛的，軟軟的，果然很好摸"
            show s happy with dissolve:
                zoom 0.25 
                xpos 603 
                ypos 72
            "你與碩碩相視一笑，度過了一段悠閒的時光"
            "你與碩碩相視一笑，度過了一段悠閒的時光"
            "你們相談了許久"
            "回憶起許多之前的事情"
            "此刻你感到無比安心" 
            player "啊！時間不早了，我得走了！"
            s "嗯，掰掰。"
            $ day2_count += 1
            $ go_around_reacted = 1
            jump choose_scene

    return

label day2_night:
    scene bedroom with dissolve:
        subpixel True 
        matrixcolor TintMatrix("#18213b")*InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.5)*HueMatrix(0.0) 
    play music "night.mp3"
    "一天又這麼過去了，好累啊"
    scene black with Fade(0.5,1.0,0.5)
    return

label bob_morning:
    scene bedroom
    player "看來今天也是美好的一天呢！"
    scene classroom with Fade(0.5,1.0,0.5)
    play music "snowdin-town.mp3" loop volume 0.5
    "[player]來到了教室"
    show s norm with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
    "碩碩突然抬起頭來"
    "看到是你，似乎鬆了一口氣"
    show s happy with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
    s "早……早安"
    hide s norm with dissolve
    show w norm at comein(0.5,0.1):
        yalign 1.5
        zoom 0.9
    w "嘿哥們！早啊！"
    player "勝勝！早啊"
    w "我等等有比賽，等等記得來看我！"
    "經勝勝提醒，你想起來今天上午似乎是校園認識活動"
    "學生們可以到處參觀、走訪校園"
    player "必須的"
    show w at goout(0.1)
    "勝勝飛快地離開了教室"
    hide w norm
    "此時，那位美女恰巧進來了教室"
    play sound "SFX/door-slam.mp3" noloop volume 0.3
    show a norm with dissolve:
        zoom 0.25
        yalign 1.5
        xalign 0.5
    "空氣中彷彿多了一點莓果的香氣，使你整個人都清爽了起來"
    if a_tellingname:
        player "啊，Alex，早安"
        a "早啊，[player]"
    hide a norm with dissolve

    play sound "SFX/felicia_character_page1_jp.mp3"
    show bob norm with dissolve:
        xalign 0.5
        yalign 1.0
        zoom 0.3
    b "早上好啊！[player]"
    player "早上好，[bb]"
    player "?"
    "不知怎麼的{nw=0.1}"
    "不知怎麼的{fast} 你雖然對[bb]感到陌生"
    "腦海中卻有許多你們相處的回憶"
    b "怎麼了嗎？"
    b "你看上去有點疲憊呢"
    b "做惡夢了？"
    player "......"
    b "過來一點"
    show bob norm:
            yalign 0.5
            linear 1.0 zoom 1.0
    "[bb]一把把你摟進環中"
    "隔著他的衣服{nw}"
    "隔著他的衣服{fast} 你似乎能聽見他的心跳"
    show bob norm:
        linear 1.0 zoom 0.5
    b "好點了嗎？"
    player "嗯"
    show bob happy
    b "沒事就好"
    hide bob 
    scene classroom with Fade(0.5,0.0,0.5)
    
    player "離活動開始還有一段時間，稍微睡一下好了……"
    
    scene classroom with Fade(0.5,1.0,0.5)
    "你睡了一覺，精神似乎變好了"
    "醒來後，教室裡只剩[bb]和你"
    show bob norm:
        zoom 0.3
    b "醒來啦？"
    show bob happy
    b "你看上去清爽多了"
    b "過來吧！"
    scene black with dissolve
    "[bb]將你抱在懷中 溫柔的撫摸著你的頭"
    b "把全部都交給我就好"
    "[bb]溫柔的話語令你感到十分安全"
    "......"
    player "對了！今天還有活動呢！"
    jump choose_scene

    return
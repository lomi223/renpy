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
    "[player]來到了教室"
    player "碩碩，早安"
    s "！"
    "碩碩突然抬起頭來"
    "看到是你，似乎鬆了一口氣"
    s "早……早安"
    w "嘿哥們！早啊！"
    player "勝勝！早啊"
    w "我等等有比賽，等等記得來看我！"
    "經勝勝提醒，你想起來今天上午似乎是校園認識活動"
    "學生們可以到處參觀、走訪校園"
    player "必須的"
    "勝勝飛快地離開了教室"
    "此時，Alex恰巧進來了教室"
    "空氣中彷彿多了一點莓果的香氣，使你整個人都清爽了起來"
    player "啊，Alex，早安"
    a "早啊，[player]"
    player "離活動開始還有一段時間，稍微睡一下好了……"
    "你睡了一覺，精神似乎變好了"
    "醒來後，教室裡的人已經寥寥無幾"
    player "我也去逛逛學校好了。"
    player "我該去哪呢？"
    menu:
        "去球場看看":
            jump w_soccer
        "去圖書室看看":
            jump a_reading
        "隨處晃晃":
            jump s_cat

label w_soccer:
    "你慢慢靠近球場，人開始多了起來"
    "許多新生聚集到了此處，觀看著高年級的學生們揮灑汗水"
    "不遠處的足球場旁更是擠滿了人"
    player "足球？我記得勝勝好像有比賽的樣子，過去看看吧。"
    "你使盡全力，才稍微擠進那群學生中"
    "仔細一看，勝勝正快速地在球場上穿梭"
    player "對面選手的有穿學校球衣，應該都是高年級吧？"
    "儘管對手是高年級，勝勝仍不落下風"
    "他敏捷的動作令所有人為之驚嘆，精準的傳球驚詫了周邊的所有人"
    "很快，勝勝便找到了機會，一發射門——"
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
    "你們之間的話題不斷，大部分是有關運動的"
    "還有肌肉、女僕跟電動"
    "談話間，勝勝突然拉著你往旁邊一步"
    "飛身向前、為你擋住了天外飛來的排球"
    皮膚黝黑的學生 "對不起！沒注意力道"
    w "沒事，我們都沒有受傷"
    "勝勝回頭望向你，似乎在等待著你說些什麼"
    menu:
        "謝謝勝勝！嚇死我了！":
            "勝勝的臉微微泛紅，你們之間僵住了一小會兒"
            w "沒……沒事就好"
            $ w_love += 1
        "我去，這球有夠危險。":
            w "……沒事就好！"
    "你們一起參觀了許多運動社團"
    很高的學生 "歡迎加入籃球隊喔！"
    戴著眼鏡的學生 "不介意的話，可以來桌球部看看喔……"
    "學生們的吆喝聲此起彼落"
    "勝勝似乎很喜歡這種熱鬧的氣氛"
    "你的嘴角也不自覺上揚了些"
    "你們漫步在運動場上，有時被勝勝拉走、去看看一些有趣的攤子"
    "有時只是單純聊著天"
    "你們最後坐在了足球場旁的板凳上，這時，勝勝不知從哪裡搞來了一顆足球"
    "他將球頂在頭上，秀著一些你看不懂的技巧與招式"
    "看起來有些滑稽，但你知道，這些動作絕不是簡簡單單能辦到的"
    w "[player]還有一些時間，你要來體驗一下足球嗎？"
    menu:
        "打！肯定打！":
            w "這就對了！"
            "勝勝將你一把拉起，興高采烈地跟你介紹起了簡單的動作與腳法"
            "你有些不適應，但勝勝耐心地在一旁指導你"
            "過了一段時間，你也開始能夠做出基本的踢、傳球了"
            "你與勝勝在炎熱的太陽下踢著球"
            "彷彿忽視了旁人"
            "世界好像只剩下你們兩人"
            "不知過了多久，你們兩個都累壞了"
            "你坐在板凳上喘著氣，此時勝勝向你遞來了飲料"
            w "我喝過了，你用倒的吧"
            player "沒事，我不介意"
            "你們兩人坐在球場旁，就著麼看著場上的運動員們"
            "勝勝的肌膚輕貼著你，你沒有開口說話"
            "就著麼持續著好一陣子"
            w "時間差不多了，我得去找球隊朋友吃飯！"
            player "嗯！路上小心，掰掰！"
        "先不要……":
            ""

label a_reading:
    

label s_cat:
        
    return

label bob_morning:
    scene bedroom
    "看來今天也是美好的一天呢！"
    
    return

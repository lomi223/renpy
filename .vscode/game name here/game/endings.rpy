label end1:
    scene black with dissolve
    "那天你和勝勝度過了一個美妙的夜晚"
    "你們兩個都很滿意"
    centered "獲得成就：基情" with Dissolve(2.0)
    return

label playing_ending:
    scene black with dissolve
    "你玩了一整天的遊戲"
    "從早上到了晚上"
    "你決定睡覺了"
    "但是你發現被子有點短"
    "於是不斷的調整被子"
    "可不管怎麼調整"
    "被子總是短一截"
    "你終於明白"
    "玩了一整天"
    "你這被子也就這樣了"
    centered "獲得成就：一被子" with Dissolve(2.0)
    return

label single:
    scene black with dissolve
    "不是，哥們"
    "機會都給你了還不把握？"
    centered "獲得成就：活該單身" with Dissolve(2.0)
    return

label w_love:
    scene black with dissolve
    centered "約定的日子到來了，你帶著忐忑的心來到了勝勝的家附近"
    scene street_scene with dissolve:
        zoom 3
    player "今天要跟勝勝去逛街，算是第一次正式約會吧？"
    player "好緊張"
    "已經到達約定的時間了，你發現勝勝還沒有出來"
    "你又等了一陣子"
    "他的家門並沒有關"
    player "那個，打擾囉......"
    scene enterance with dissolve:
        zoom 2.65
        ypos -0.24
    stop music
    "安靜地可怕，你不禁吞了吞口水"
    player "看起來在房間裡面？"
    "你這麼想著，推開了那扇緊閉的門"
    scene bedroom with dissolve
    player "勝勝，你在......"
    play music "call of the witch.mp3" loop volume 1.5
    show w norm:
        yalign 1.5
        xalign 0.5
        ypos 0.95
    player "......"
    player "這是......什麼"
    player "為什麼" 
    player "為甚麼阿阿啊啊"
    show w norm with dissolve:
        yalign 1.5
        xalign 0.5
        ypos 0.95
        linear 1 ypos 1.09
    show w norm with dissolve:
        yalign 1.5
        xalign 0.5
        ypos 1.09
        linear 1 ypos 0.95
    player "?"
    show w norm with dissolve:
        yalign 1.5
        xalign 0.5
        ypos 0.95
        linear 1 ypos 1.09
    show w norm with dissolve:
        yalign 1.5
        xalign 0.5
        ypos 1.09
        linear 1 ypos 0.95
    "你又往內站了一步，看見了被門框擋住的地方"
    show w norm with dissolve:
        yalign 1.5
        xalign 0.5
        ypos 1.28
        linear 1 ypos 1.18
    show w norm with dissolve:
        yalign 1.5
        xalign 0.5
        ypos 1.18
        linear 1 ypos 1.28  
    play music "original-unfiltered-audio--1-hour-perfect-loop-high-quality--still-alive.mp3" loop volume 1
    player "為什麼......在做引體向上啊!"
    w "！喔澤澤你來了，討厭，人家還沒換衣服"
    w "快出去！"
    player "喔喔喔對不起......"
    scene street_scene with dissolve:
        zoom 3
    play music "flower_dance.mp3" loop volume 2
    show w norm_2 with dissolve:
        zoom 0.25
        xpos 585
        ypos 72
    "勝勝一換好衣服，便興奮地跑出了家門，你加快腳步跟上"
    "在你快要追到他時"
    "勝勝向你伸出了手"
    w "今後，也請多多指教啦？"
    "你忍不住露出了微笑、加快腳步"
    "牽起了勝勝的手"
    scene black with dissolve
    "勝勝結局"
    return
label a_love:
    scene black with dissolve
    centered "你來到了約定的地點，Alex正在天臺等著你"
    scene top_floor with dissolve:
        zoom 2.65
        ypos -0.24
    show a norm with dissolve:
        zoom 0.25
        xpos 567
        ypos 81
    "他的髮絲被風吹得飄逸"
    "他的手輕輕抬起、將一縷頭髮撩到耳後"
    a "你來了。"
    player "是的，我做好準備了。"
    show a happy with dissolve:
        zoom 0.25
        xpos 567
        ypos 81
    "你此刻心情複雜，不敢相信這種事情會發生在自己身上"
    "也許他下一秒會脖子折斷成九十度向你衝來"
    "但是並沒有，你確信了這並不是惡夢"
    "你與Alex談了很多，也了解了他的許多過去"
    "與Alex的對話是如此令人舒服"
    "你們或許認識不久"
    "但你相信愛情能夠帶著你們走向未來"
    
    scene black with dissolve
    "Alex結局"
    return

label s_love:
    scene black with dissolve
    centered "約定的日子到來了，你帶著忐忑的心來到了碩碩的家門前"
    scene street_scene with dissolve:
        zoom 3
    player "碩碩到底想給我看甚麼？"
    player "好緊張"
    "你又等了一陣子"
    "他的家門並沒有關"
    player "那個，打擾囉......"
    scene enterance with dissolve:
        zoom 2.65
        ypos -0.24
    stop music
    "安靜地可怕，你不禁吞了吞口水"
    player "看起來在房間裡面？"
    "你這麼想著，推開了那扇緊閉的門"
    scene bedroom with dissolve
    "房間內並沒有人"
    "正當你準備轉身出門時，卻發現碩碩站在門口"
    show s norm with dissolve:
        zoom 0.25
        xpos 567
        ypos 81
    play music "call of the witch.mp3" loop volume 1.5
    "他手中握著一把菜刀"
    "並反握著對準自己的肚子"
    player "碩碩，你幹嘛......"
    scene black with dissolve
    "你受到太大的驚嚇，閉上了自己的眼睛"
    play sound "SFX/stab.mp3" noloop volume 3
    "直到你聽見了刀子插入某種東西的聲音"
    "攪 呀 攪"
    "你開始啜泣，眼淚不停滑落"
    "終於睜開了眼睛"
    scene bedroom with dissolve
    show s norm with dissolve:
        zoom 0.25
        xpos 567
        ypos 81
    play music "original-unfiltered-audio--1-hour-perfect-loop-high-quality--still-alive.mp3" loop volume 1
    "發現碩碩站在你的身後，將刀子插向了後方桌上的蛋糕"
    player "......碩碩，你應該知道刀子不是這樣握的吧？"
    show s happy with dissolve:
        zoom 0.25
        xpos 567
        ypos 81
    s "......[player]生日快樂！"
    player "......今天根本不是我的生日啊？應該是下個月才對"
    s "......啊？"
    show s sad with dissolve:
        zoom 0.25
        xpos 567
        ypos 81
    player "......你也太糊塗了吧！"
    player "不過這樣也很可愛就是了"
    show s happy with dissolve:
        zoom 0.25
        xpos 567
        ypos 81
    s "......嘻嘻"
    play music "Memory.mp3" loop volume 0.5
    "你們吃著蛋糕、一起聊著天"
    "彷彿回到了你們以前相處的日子"
    "而你們知道，這種日子將會持續下去"
    s "[player]......謝謝你"
    player "嗯，今後也請多多指教囉？"
    scene black with dissolve
    "碩碩結局"
    return
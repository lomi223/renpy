label day4:
    play music "bird-chirping-sound-effect.mp3" loop fadein 0.3 volume 0.3
    scene bedroom with Fade(0.5,1.0,1.5)
    w "（炫耀的貼圖）：哥們，你一定不相信，那個（號稱）冰山美人的家政老師竟然給我把到了"
    w "老師同意我使用家政教室了，你不是想追到alex嗎？要不趁這個機會烤個手工餅乾？"
    "經歷了充實的幾天，你的疲勞感不減反增"
    "也認識了一些朋友"
    player "這包餅乾的去處..."
    player "不知道將會去哪？"
    "睡眼惺忪的你聳了聳肩，答應了勝勝的邀約"
    scene black with dissolve
    centered "回完訊息後，你再度陷入了沈睡" 
    player "我還不想做決定啦..."
    scene bedroom with Fade(0.5,1.0,1.5)
    "再度醒來，你感覺有哪裡不對勁"
    player "完了！睡過頭了！"
    scene black with dissolve
    scene street at center:
        xzoom 2.6
        yzoom 2.4
    "有別於三天前的陌生，你逐漸熟悉了上學的路線"
    "微風掠過，你很享受這種感覺"
    scene black with Fade(1.5,1.0,0.5)
    play music "Dating Start!.mp3" loop volume 1.5
    scene cookieclass at center:
        xzoom 3.2
        yzoom 2.6
    "走進家政教室，勝勝一邊向你揮手，一邊露出不滿的表情"
    show w mad at left with moveinleft:
        zoom 0.2
    w "這次怎麼也遲到了？"
    player "睡過頭了，抱歉..."
    show w norm_2 with dissolve:
        zoom 0.2
        yalign 1.5
        xalign 0.5
    w "沒事，趕快上工吧！"
    show w norm with dissolve:
        zoom 0.9
        yalign 1.0
        xalign 0.7
    "勝勝露出了一個「你肯定不知道我有多牛」的表情"
    w "雖然看起來不太像，但我在烘焙這塊可是很在行的"
    player "等等看你做怎麼樣就知道囉？"
    show w chill with dissolve:
        zoom 0.2
        yalign 1.5
        xalign 0.5
    w "包在我身上!"
    w "你有什麼喜歡的口味嗎？"
    menu:
        "巧克力":
            show w norm_2 :
                zoom 0.2
                yalign 1.5
                xalign 0.5
            w "我的話喜歡伯爵奶茶口味，我們就做這兩個口味吧"
        "伯爵奶茶":
            show w norm_2 with dissolve:
                zoom 0.2
                yalign 1.5
                xalign 0.5
            w "我的話喜歡巧克力口味，我們就做這兩個口味吧"
            w "你先來決定要放什麼配料吧？"
            hide w
    scene black with Fade(1.0,1.0,1.0)
    call cookie
    scene cookieclass at center:
        xzoom 3.2
        yzoom 2.6
    play music "Dating Start!.mp3" loop volume 1.5
    "軟化奶油並加入糖粉攪拌，你的工作有點過於容易"    
    "處理完手邊的工作，你望向勝勝"
    show w sided with dissolve:
        zoom 0.5
        yalign 1.0
        xalign 0
    "拌著餅乾要用的麵糊，他的衣服因汗溼而緊貼著他的肌膚，結實的線條若隱若現"
    menu:
        "有意無意地靠近勝勝，眼神時而飄到他身上。":
            window auto hide
            camera:
                subpixel True xzoom 1.0 
                zoom 1.0 
                linear 0.10 zoom 1.21 
            with Pause(0.5)
            camera:
                zoom 1.21 
            window auto show
            "你的視線在勝勝身上遊走，肆無忌憚地將他的肌肉線條盡收眼底。"
            show w norm_2 with dissolve:
                zoom 0.2
                yalign 1.0
                xalign 0
            camera:
                linear 0.10 zoom 1 
            with Pause(1.0)
            camera:
                zoom 1
            "但當勝勝轉過頭時，澤澤卻又像毫不在乎一般。"
            player "鋼盆我拿走囉。"
            "你輕靠在勝勝身上、伸手拿走了另一側的鋼盆。"
            show w shy with dissolve:
                zoom 0.2
                yalign 1.5
                xalign 0
            "勝勝沒有開口說話，但臉頰多了一抹紅潤。"
        "男人只會影響我做餅乾的速度。":
            "你原地lock in，開啟聖人模式，如入無人之境，手速有如阿扁每秒抖6.6次。" with hpunch
            "你的速度快到讓勝勝嚇了一跳。"with vpunch
            show w chill with dissolve:
                zoom 0.2
                yalign 1.5
                xalign 0
            w "哥們在裝弱啊，牛啊。"
            "你的速度快到讓餅乾也嚇了一跳"
            "餅乾成品量-20"
            show w mad with dissolve:
                zoom 0.2
                yalign 1.5
                xalign 0 

            w "哥們我們等一下有得清了..."
        "忍不住了，直接往他身上貼。":
            "不管三七二十一，你向勝勝使出了鐵山靠。"
            player "真香。"
            show w shy with dissolve:
                zoom 0.2
                yalign 1.5
                xalign 0 
            w "討厭，人家身上很多汗啦。"
            "勝勝雙手叉腰，嘴巴嘟了起來。"
            "你露出了得意的表情，像是拿逗貓棒在逗貓一般"
    scene black with Fade(1,0.5,1)
    stop music fadeout 1.0
    scene sunset_road at center:
        xzoom 2.6
        yzoom 2.4
    "做完餅乾，你跟勝勝走出了家政教室"
    player "很扯 竟然已經快要天黑了"
    show w mad at right with moveinbottom:
        zoom 0.2
    w "畢竟你睡到下午四點..."
    player "對不起..."
    show w norm_2 with dissolve:
            zoom 0.3
            yalign 2
            xalign 0.5
    w "沒...沒關係啦 哼"
    w "(捶)"  
    w "但沒想到你做的也不賴嘛"
    player "哈哈...多虧有你幫忙"
    w "明天就拿去給喜歡的人吧？"
    player "..."
    w "?"
    show w chill with dissolve:
        zoom 0.3
        yalign 2
        xalign 0.5
    w "你在煩惱要給誰嗎？"
    player "(點頭)" 
    w "原來如此"
    show w shy with dissolve:
        zoom 0.3
        yalign 2
        xalign 0.5
    w "要...要給我的話，也不是不行啦"
    w "..."
    w "當...當我沒說！明天見！"
    hide w with Fade(0.3,0,0.3)
    "雖然沒有說出口，你很開心可以遇見這樣的朋友"
    "朋友?"
    "..."
    "你自己也不太確定"
    player "煩惱事情還真多"
    "夕陽將街道染上了一片金黃"
    "跌宕起伏的暑輔也將步入尾聲"
    "握著手中微溫的餅乾"
    "你思考著這包餅乾的去處"
    "是靦腆的碩碩?"
    "熱情而無所畏懼的勝勝?"
    "熱愛文學的Alex?"
    "還是B̟̲̜͖̙̲̫̖̰͍̱̜̦͔̤̱̮̰͕̖̞̩̰̂̄̓͌̌̀̆̄̆̉̍̉͊͌̃̃̒͐̄͌̚ͅo͓̲̳̟͎̪̞̥̥̙̠͕̲̟̳̭̅̀̂̃̐́̂͆̌̿̇͌̑́͌̾͌̂̏ͅͅb͚̰̤̫̳̥̖͇̘͙̞͍̮͊͆͑̄̇̇̉̎̒͑̋͊̾̐̀̿̐̓̎̂̋͗̚?"
    scene black with dissolve
    centered "彷彿是在抗拒思考一般，你一到家便陷入了沈睡"

label cookie:
    default ingredients = []
    scene precookie at center:
        xzoom 2.2
        yzoom 2.2
    call screen make_cookie_UI
    if ingredients:
        play music "complete.mp3" volume 0.3 
        "你做出了一個有特色的餅乾"
    else:
        "你選擇不加任何配料，這是一塊普通的餅乾"
    scene black with Fade(0.5,0.5,0.5)
    return
screen make_cookie_UI:
    # 背景
    frame:
        align (1.0, 0.0)  # 置中
        xsize 600
        ysize 600
        background "#ffc4e5"
        vbox:
            spacing 10
            align (1.0, 0.5)
            
            # 標題
            text "選擇你想加入餅乾麵糊的配料：" size 30
            # 顯示可選擇的配料按鈕
            hbox:
                spacing 10
                add "images/chocolate.jpg" size (100, 100)
                textbutton "巧克力" action Function(add_ingredient, "巧克力","images/chocolate.jpg")
            hbox:
                spacing 10
                add "images/mom.png" size (100, 100)
                textbutton "你媽" action Function(add_ingredient, "你媽","images/mom.png")
            hbox:
                spacing 10
                add "images/Yajusanpai.jpg" size (100, 100)
                textbutton "野獸前輩" action Function(add_ingredient, "野獸前輩", "images/Yajusanpai.jpg")
            hbox:
                spacing 10
                add "images/sugar.jpg" size (100, 100)
                textbutton "糖霜" action Function(add_ingredient, "糖霜","images/sugar.jpg")
            if ingredients:
                text "已選擇的配料：" size 20
                text  " \n".join(ingredients)    
            # 完成按鈕
            textbutton "完成製作" action Return()
init python:
    def add_ingredient(name, image):
        if name not in renpy.store.ingredients:
            renpy.store.ingredients.append(name)

# Define styles
init:
    style ingredient_button:
        size 20
        background "#d4a373"
        hover_background "#f6c89f"
        insensitive_background "#aaaaaa"
        padding (10, 10)

    style done_button:
        size 24
        background "#9dc6a7"
        hover_background "#add4b5"
        insensitive_background "#aaaaaa"
        padding (15, 15)
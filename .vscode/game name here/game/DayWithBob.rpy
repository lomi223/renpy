label bob_and_me:
    python:
        import os
        real_name = os.getlogin()
    define rp = Character("[real_name]")
    scene black with dissolve
    centered "八月的尾聲即將到來，即將邁入秋色的風似乎更加喧囂了。青澀的少年渴望抓住夏天的尾巴、為青春開啟美好的篇章。" with fade
    
    scene bedroom with dissolve
    rp "今天天氣真不錯！"

    scene black with dissolve
    scene street_scene with dissolve:
        zoom 3
    rp "這裡還真安靜呢......"

    scene black with dissolve
    show outside with dissolve:
        xsize 1.1
        ysize 1.1
    rp "印象中似乎有誰在這裡"
    rp "不記得了......"

    scene black with dissolve
    scene classroom with dissolve
    rp "班上還真是冷清......"

    scene black with dissolve
    centered "你坐在你自己的座位上整理著你自己的物品直到......"
    scene classroom with dissolve 
    play sound "SFX/door_knock.mp3" noloop
    pause 1.0
    show bob norm with dissolve:
        zoom 0.25
    b "早安啊！[real_name]"
    rp "是你啊，bob{nw=0.3}"
    rp "是你啊，bob{fast}，其他人在......{nw}"
    b "哈哈！你忘了吧？"
    b "今天是只屬於我們倆的  一‧對‧一‧教‧學  喔！"
    rp "......"
    rp "好像是這樣沒錯"
    b "所以你現在先放輕鬆"
    b "閉上眼睛，讓我們開始第一堂課吧！"
    scene black with dissolve
    b "把一切都交給我就行了"
    
    return
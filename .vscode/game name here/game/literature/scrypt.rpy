label poem:
    scene notebook with dissolve
    $ points = 0
    jump show_words
    return

label show_words:
    if curr_words < 40:
        call screen words
    else:
        jump finished



default AlexWordList = {1 : "Alex", 2 : "Gaylex", 3 : "緊繃", 4 : "甲", 5 : "強人鎖男", 6 : "易安居士", 7 : "Alexyeh", 8 : "男同", 9 : "弄虛作甲", 10 : "超甲狂犀",
11 : "左右為男", 12 : "甲鬼甲怪", 13 : "網癮少年", 14 : "勉為騎男", 15 : "國文考卷", 16 : "甲子園", 17 : "男以理解", 18 : "甲擠定理", 19 : "同志", 20 : "甲動作",
21 : "甲裝", 22 : "不甲思索", 23 : "男上加男", 24 : "沒什麼", 25 : "倒廚餘", 26 : "值日生", 27 : "不甲思索", 28 : "甲設語氣", 29 : "男以理解", 30 : "甲新聞",
31 : "迎男而上", 32 : "Yori", 33 : "甲騙", 34 : "甲戲真做", 35 : "進退兩男", 36 : "甲鬼甲怪", 37 : "鬆繃", 38 : "甲尬八八", 39 : "甲面", 40 : "虛情甲意"
}

default RandomWordList1 = {1 : "風箏", 2 : "彩虹", 3 : "機器人", 4 : "瀑布", 5 : "鯨魚", 6 : "熱氣球", 7 : "指南針", 8 : "蜘蛛", 9 : "城堡", 10 : "望遠鏡",
11 : "冰川", 12 : "火山", 13 : "雷達", 14 : "星星", 15 : "天鵝", 16 : "烏龜", 17 : "氧氣", 18 : "磁鐵", 19 : "蝙蝠", 20 : "石榴",
21 : "算盤", 22 : "葡萄", 23 : "矛盾", 24 : "日食", 25 : "長頸鹿", 26 : "桑樹", 27 : "斑馬", 28 : "陀螺", 29 : "鯊魚", 30 : "跳繩",
31 : "銀河", 32 : "彈簧", 33 : "望遠鏡", 34 : "手套", 35 : "燈塔", 36 : "龍捲風", 37 : "蜜蜂", 38 : "箭靶", 39 : "鳳凰", 40 : "圓規"
}

default RandomWordList2 = {1 : "烏鴉", 2 : "珊瑚", 3 : "降落傘", 4 : "龜甲", 5 : "恆星", 6 : "仙人掌", 7 : "河流", 8 : "迷宮", 9 : "銅像", 10 : "黑洞",
11 : "烏龜殼", 12 : "繩索", 13 : "石碑", 14 : "流星雨", 15 : "眼鏡蛇", 16 : "月亮", 17 : "沙漠", 18 : "雪人", 19 : "木偶", 20 : "鳥巢",
21 : "滑板", 22 : "珍珠奶茶", 23 : "浮木", 24 : "紙鶴", 25 : "胡蘿蔔", 26 : "甲蟲", 27 : "彩燈", 28 : "風信子", 29 : "沙漏", 30 : "星雲",
31 : "毛筆", 32 : "畫框", 33 : "橋樑", 34 : "燈籠", 35 : "蟻群", 36 : "雨滴", 37 : "竹林", 38 : "烏雲", 39 : "冰山", 40 : "樹屋"
}

default RandomWordList3 = {1 : "風車", 2 : "橙子", 3 : "旋律", 4 : "浮橋", 5 : "松鼠", 6 : "探照燈", 7 : "花瓶", 8 : "流星", 9 : "狐狸", 10 : "地圖",
11 : "蝴蝶結", 12 : "貓頭鷹", 13 : "榴槤", 14 : "樹幹", 15 : "雲朵", 16 : "羽毛", 17 : "陽傘", 18 : "棋盤", 19 : "錦鯉", 20 : "杯子蛋糕",
21 : "海馬", 22 : "蜻蜓", 23 : "鯰魚", 24 : "棉花糖", 25 : "萬花筒", 26 : "烏托邦", 27 : "柿子", 28 : "氣球", 29 : "漁船", 30 : "鐵鎚",
31 : "壁虎", 32 : "岩漿", 33 : "箱子", 34 : "喇叭", 35 : "孔雀", 36 : "荷花", 37 : "茶壺", 38 : "鴿子", 39 : "雪花", 40 : "火柴"
}

default curr_words = 0

default points = 0

default pos = ["w","w","d","d","d","w","w","d","w","d","d","s","s","s","d","d","w","w","w","d","w","w","w","d","d","w","w","d","d","d","d","d","w","w","w","w","d","w","w","w"]


screen words:
    grid 1 2:
        xalign 0.5
        spacing 25
        yalign 0.52
        if pos[curr_words] ==  "w":
            hbox:
                spacing 150
                textbutton "%s" % AlexWordList[curr_words+1]:
                    text_style "AlexButt"
                    action [SetVariable("points", points + 1), SetVariable("curr_words", curr_words + 1), Jump("show_words")]
            
                textbutton "%s" % RandomWordList1[curr_words+1]:
                    text_style "AlexButt"
                    action [SetVariable("curr_words", curr_words + 1), Jump("show_words")]
            hbox:
                spacing 150
                textbutton "%s" % RandomWordList2[curr_words+1]:
                    text_style "AlexButt"
                    action [SetVariable("curr_words", curr_words + 1), Jump("show_words")]
            
                textbutton "%s" % RandomWordList3[curr_words+1]:
                    text_style "AlexButt"
                    action [SetVariable("curr_words", curr_words + 1), Jump("show_words")]
        
        if pos[curr_words] ==  "d":
            hbox:
                spacing 150
                textbutton "%s" % RandomWordList1[curr_words+1]:
                    text_style "AlexButt"
                    action [SetVariable("curr_words", curr_words + 1), Jump("show_words")]

                textbutton "%s" % AlexWordList[curr_words+1]:
                    text_style "AlexButt"
                    action [SetVariable("points", points + 1), SetVariable("curr_words", curr_words + 1), Jump("show_words")]
            hbox:
                spacing 150
                textbutton "%s" % RandomWordList2[curr_words+1]:
                    text_style "AlexButt"
                    action [SetVariable("curr_words", curr_words + 1), Jump("show_words")]
            
                textbutton "%s" % RandomWordList3[curr_words+1]:
                    text_style "AlexButt"
                    action [SetVariable("curr_words", curr_words + 1), Jump("show_words")]
        
        if pos[curr_words] ==  "s":
            hbox:
                spacing 150
                textbutton "%s" % RandomWordList1[curr_words+1]:
                    text_style "AlexButt"
                    action [SetVariable("curr_words", curr_words + 1), Jump("show_words")]
                    
                textbutton "%s" % RandomWordList3[curr_words+1]:
                    text_style "AlexButt"
                    action [SetVariable("curr_words", curr_words + 1), Jump("show_words")]
            hbox:
                spacing 150
                textbutton "%s" % RandomWordList2[curr_words+1]:
                    text_style "AlexButt"
                    action [SetVariable("curr_words", curr_words + 1), Jump("show_words")]

                textbutton "%s" % AlexWordList[curr_words+1]:
                        text_style "AlexButt"
                        action [SetVariable("points", points + 1), SetVariable("curr_words", curr_words + 1), Jump("show_words")]
                

style AlexButt:
    color "#000000ff"
    hover_color "#ecf455"
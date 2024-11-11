# 遊戲腳本位於此檔案。

# 聲明該遊戲使用的角色。 color 參數
# 為角色的名稱著色。

define e = Character("艾琳")
define t = Character("澤澤")
define w = Character("勝勝")
define a = Character("Alex")
define s = Character("碩碩")
define b = Character("BoB")
define player = Character("[name]")

# 遊戲從這裡開始。

label start:

    # 顯示背景。 預設情況下，它使用佔位符，但您可以
    # 將檔案（名為 "bg room.png" 或 "bg room.jpg"）新增至
    # images 目錄來顯示它。

    scene bg room
    with fade
    play music "audio/11-just-monika.mp3" fadein 0.1 volume 0.3
    # 這顯示了一個角色精靈。 使用了佔位符，但您可以
    # 透過將名為 "eileen happy.png" 的檔案
    # 新增至 images 目錄來取代它。

    show eileen happy
    with dissolve
    
    # 這些顯示對話行。

    e "感謝您遊玩DDGC。"

    e "您將在此體驗您未曾有過的校園戀愛生活。"

label inputname:
    $ name = renpy.input("請在此輸入你的名字",length = 32)
    $ name = name.strip()

    if not name:
        $ name = Alex 
    e "[name]是你的名字嗎?"
    
menu:
    "Yes":
        jump say_my_name
    "No":
        jump inputname

label say_my_name:
    player "我的名字是[name]。"
    # 遊戲結束。


    return

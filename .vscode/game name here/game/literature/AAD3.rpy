label AAD3:
    stop music
    scene black with dissolve
    centered "第三日的早晨 你在進教室前遇到了......"
    scene staircase with dissolve
    play music "snowdin-town.mp3"
    show a norm with dissolve:
        xalign 0.5
        yalign 0.5
        zoom 0.25
    a "早上好，[player]"
    player "早上好啊，[aa]......"
    player "（他真的好美阿......）"
    "[player]的心臟撲通撲通地跳著"
    show a noticed
    a "那個，你想和我去文學部看看嗎？"
    a "聽說他們今天有展覽"
    player "！？"
    a "要嗎？"
    menu:
        "去！":
            pass
        "必須得去！！！":
            pass
    show a happy
    a "那太好了，我們走吧"

    jump LiteratureClub

label LiteratureClub:
    scene classroom with Fade(0.5,0.1,0.5)
    player "這裡就是文學部嗎？"
    player "看起來跟我們的教室一模一樣"
    show monika 1 with dissolve:
        zoom 0.85
        xalign 0.5
        yalign 1.0
    monika "早上好呀！兩位客人{nw}"
    show monika 1d
    pause 0.5
    show monika 5
    monika "看來是兩位十分特別的客人呢！"
    monika "歡迎二位來到文學部"
    show monika 2
    monika "請問二位是來做甚麼的呢？"
    show monika 2:
        subpixel True
        linear 0.3 pos (0.65, 1.0)
    show a norm:
        subpixel True
        zoom 0.4
        pos (-0.65, -0.20) zpos -300 
        linear 0.3 pos (-0.05, -0.20) zpos -300 yrotate 18.0
    a "我們來體驗寫詩的"
    show monika 1
    monika "這樣啊"
    show monika 3
    monika "那這本單字書先給你們用"
    show monika 3j
    monika "我很期待你們的創作喔！"
    show monika 1
    monika "對了，[player]你過來一下"
    show a norm:
        subpixel True
        zoom 0.5
        linear 0.3 pos (-0.65, -0.25) zpos -300 yrotate 18.0
    show monika 1:
        subpixel True
        linear 0.3 pos (0.5, 1.0)
    monika "這個給你"
    $ renpy.notify("gift recieved")
    python:
        import os
        import platform

        system_name = platform.system()
        text = "左上為上，右上為右；\n左下為左，右下為下；\n四十步路，步步不回；\n終點就在前方。"
        
        if system_name == "Windows":
            folder_path = f"C:\\Users\\{real_name}\\Desktop\\GiftForYou;)"
        else:
            folder_path = f"/home/{real_name}/example_folder"

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_name = os.path.join(folder_path, "hint.txt")
        with open(file_name, "w") as file:
            file.write(text)

    player "？"
    monika "你說不定會用到"
    show monika 5
    monika "祝你好運，[real_name]{nw}"

    jump poem

label monikas:
    scene black with dissolve
    show monika 1
    ""
    show monika 2
    ""
    show monika 3
    ""
    show monika 4
    ""
    show monika 5
    ""
    show monika 1a
    ""
    show monika 1b
    ""
    show monika 1c
    ""
    show monika 1d
    ""
    show monika 1e
    ""
    show monika 1f
    ""
    show monika 1g
    ""
    show monika 1h
    ""
    show monika 1i
    ""
    show monika 1j
    ""
    show monika 1k
    ""
    show monika 1l
    ""
    show monika 1m
    ""
    show monika 1n
    ""
    show monika 1o
    ""
    show monika 1p
    ""
    show monika 1q
    ""
    show monika 1r
    ""
    show monika 2a
    ""
    show monika 2b
    ""
    show monika 2c
    ""
    show monika 2d
    ""
    show monika 2e
    ""
    show monika 2f
    ""
    show monika 2g
    ""
    show monika 2h
    ""
    show monika 2i
    ""
    show monika 2j
    ""
    show monika 2k
    ""
    show monika 2l
    ""
    show monika 2m
    ""
    show monika 2n
    ""
    show monika 2o
    ""
    show monika 2p
    ""
    show monika 2q
    ""
    show monika 2r
    ""
    show monika 3a
    ""
    show monika 3b
    ""
    show monika 3c
    ""
    show monika 3d
    ""
    show monika 3e
    ""
    show monika 3f
    ""
    show monika 3g
    ""
    show monika 3h
    ""
    show monika 3i
    ""
    show monika 3j
    ""
    show monika 3k
    ""
    show monika 3l
    ""
    show monika 3m
    ""
    show monika 3n
    ""
    show monika 3o
    ""
    show monika 3p
    ""
    show monika 3q
    ""
    show monika 3r
    ""
    show monika 4a
    ""
    show monika 4b
    ""
    show monika 4c
    ""
    show monika 4d
    ""
    show monika 4e
    ""
    show monika 4f
    ""
    show monika 4g
    ""
    show monika 4h
    ""
    show monika 4i
    ""
    show monika 4j
    ""
    show monika 4k
    ""
    show monika 4l
    ""
    show monika 4m
    ""
    show monika 4n
    ""
    show monika 4o
    ""
    show monika 4p
    ""
    show monika 4q
    ""
    show monika 4r
    ""
    show monika 5a
    ""
    show monika 5b
    ""
    return

label finished:
    "[points]"
    
    return
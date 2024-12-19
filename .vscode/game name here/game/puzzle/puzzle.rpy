label puzzle:
    $ block_SM = SpriteManager(update = blocks_update, event = blocks_events)
    $ block_sprites = []
    $ long_h_block = Image("puzzle/long-horizontal-block.png")
    $ long_v_block = Image("puzzle/long-vertical-block.png")
    $ short_h_block = Image("puzzle/short-horizontal-block.png")
    $ short_v_block = Image("puzzle/short-vertical-block.png")
    $ red_block = Image("puzzle/red-block.png")
    $ goal = Image("puzzle/goal-vertical.png")
    $ long_v_block_size = (151, 454)
    $ long_h_block_size = (454, 151)
    $ short_v_block_size = (151, 303)
    $ short_h_block_size = (303, 151)
    $ puzzle_frame_size = (938, 938)
    $ puzzle_frame_pos = (110,71)
    $ current_puzzle = 1
    $ chick_pos = [0,0]
    play music "original-unfiltered-audio--1-hour-perfect-loop-high-quality--still-alive.mp3" loop
    jump s_1
    return

label s_1:
    scene black
    $ quick_menu = False
    $ create_blocks()
    call screen unblock_puzzle

label solved_puzzle:
    $ quick_menu = True
    stop music fadeout 2.0
    
    s "好耶！解開了！"
    play sound "SFX/hit.mp3"
    centered "碩碩興奮地跳了一下 一個不注意接撞在你的臉上"
    player "哎呀！"
    #show CG SS TOP-DOWN FROM-BACK
    play music "instrumental-music.mp3" volume 0.3
    s "阿......抱...抱歉"
    s "[player]你還好嗎？"
    player "啊哈......沒事的"
    "碩碩一臉關心的注視著你直到冷靜下來後才發現你們彼此之間的距離是多麼接近"
    scene classroom with Fade(0.5,0.0,0.5)
    show s shy with dissolve
    stop music fadeout 2.0
    s "我......"
    hide s with fade
    play sound "SFX/footstepps-2.mp3"
    "碩碩害羞地跑開了"
    player "碩碩......"
    jump day4
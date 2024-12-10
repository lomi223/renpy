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

    jump s_1
    return

label s_1:
    scene black
    ""
    $ create_blocks()
    call screen unblock_puzzle

label solved_puzzle:
    "u solved it"
    return
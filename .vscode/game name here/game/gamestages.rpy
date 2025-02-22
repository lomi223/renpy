label stages:

    call act1

    if played_count == 3:
        stop music
        jump playing_ending
    if b_love == 1:
        player "喔對還有那個人......"
        player "他究竟是誰？"
        call dream
    
    call act2

    call D3

    call day4

    return
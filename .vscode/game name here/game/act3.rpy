label D3:
    if w_love <= 0 and s_love <= 0 and  a_love <= 0 and b_love <= 0:
        jump single
    elif b_love != 0:
        jump BOBD3
    else:
        if w_love > s_love and w_love > a_love:
            jump WWDay3_morning
        if s_love > a_love and s_love > w_love:
            jump SSD3
        if a_love > s_love and a_love > w_love:
            jump AAD3
        if w_love == s_love and w_love == a_love:
            call RandWho 
            if d3 == 1:
                jump WWDay3_morning
            if d3 == 2:
                jump SSD3
            if d3 == 1:
                jump AAD3
        if w_love == s_love:
            call RandWho
            if d2 == 1:
                jump WWDay3_morning
            if d2 == 2:
                jump SSD3
        if w_love == a_love:
            call RandWho
            if d2 == 1:
                jump WWDay3_morning
            if d2 == 2:
                jump AAD3
        if a_love == s_love:
            call RandWho
            if d2 == 1:
                jump SSD3
            if d2 == 2:
                jump AAD3

label RandWho:
    $ d2 = renpy.random.randint(1, 2)
    $ d3 = renpy.random.randint(1, 3)
    return
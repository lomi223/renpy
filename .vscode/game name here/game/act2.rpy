label act2:
    play music "bird-chirping-sound-effect.mp3" loop fadein 0.3 volume 0.3
    if b_love == 1:
        jump bob_morning
    jump morning

label morning:
    scene bedroom with Fade(0.5,1.0,0.5)
    "看來今天也是美好的一天呢！"
    scene classroom with Fade(0.5,1.0,0.5)
    play music "snowdin-town.mp3" loop volume 0.5

    
    
    return





label bob_morning:
    scene bedroom
    "看來今天也是美好的一天呢！"
    
    return

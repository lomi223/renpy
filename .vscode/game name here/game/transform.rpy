#show glitch effect
image b glitched:
    At("b norm",glitch)
    pause 0.2
    At("b norm",glitch)
    pause 0.1
    At("b norm",glitch)
    pause 0.1
    At("b norm",glitch)
    pause 0.3
    At("b norm")
    pause 0.5
    repeat
transform rotation:
    zoom 0.5
    xalign 0.5
    yalign 0.5
    rotate 0
    linear 10 rotate 360
    repeat
#show glitch effect
image b glitched:
    glitch("b norm")
    pause 0.2
    glitch("b norm", offset=60, randomkey=None)
    pause 0.3
    glitch("b norm")
    pause 0.2
    glitch("b norm", offset=60, randomkey=None)
    pause 0.2
    glitch("b norm")
    pause 0.1
    glitch("b norm", offset=60, randomkey=None)
    pause 0.1
    "b norm"
    pause 1.0
    repeat
transform rotation:
    zoom 0.5
    xalign 0.5
    yalign 0.5
    rotate 0
    linear 10 rotate 360
    repeat

init-2:
    transform zoomedin:
        zoom 1.5
    transform zoomedout:
        zoom 0.1
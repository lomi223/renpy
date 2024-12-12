#show glitch effect
image b glitched:
    glitch("bob norm")  
    pause 0.2
    glitch("bob norm", offset=60, randomkey=None)
    pause 0.3
    glitch("bob norm")
    pause 0.2
    glitch("bob norm", offset=60, randomkey=None)
    pause 0.2
    glitch("bob norm")
    pause 0.1
    glitch("bob norm", offset=60, randomkey=None)
    pause 0.1
    "bob norm"
    pause 1.0
    repeat

transform rotation:
    zoom 0.5
    xalign 0.5
    yalign 0.5
    rotate 0
    linear 10 rotate 360
    repeat

transform comein(x,time):
    xalign 0.0
    linear time xalign x

transform goout(time):
    linear time xalign 2.0

transform zoomedin:
    zoom 1.5
transform zoomedout:
    zoom 0.1


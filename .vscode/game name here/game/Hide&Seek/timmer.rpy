default g_time = 0

screen timerFame(max, endup):
    frame:
        xalign 0.5
        yalign 0.0
        hbox:
            timer 0.1 action If(g_time <= 0, false = SetVariable("g_time", g_time - 0.1), true = [Hide("timerFame"), SetVariable("g_time", 0), Jump("%s"%endup) ]) repeat True
            bar: #an animated bar top center screen
                value AnimatedValue(value=g_time, range=max, delay= 0.5)
                xalign 0.0
                yalign 0.0
                xmaximum 200
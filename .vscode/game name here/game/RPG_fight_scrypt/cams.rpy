#mc
label tseIdleCam:
    window auto hide
    camera:
        subpixel True 
        pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
        linear 0.50 pos (-280, -200) zpos -200.0 xrotate 7.0 yrotate 0.0 zrotate 5.0 
    with Pause(0.60) 
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label tseAtkPrCam:
    window auto hide
    camera:
        subpixel True 
        pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
        linear 0.30 pos (280, -200) zpos -300.0 xrotate 18.0 yrotate -9.0 zrotate -9.0 
    show tse atk:
        subpixel True 
        parallel:
            'tse idle'
            0.30
            'tse atk'
        parallel:
            pos (-0.25, 0.4) zpos -700.0 
            linear 0.10 pos (0.6, 0.4) zpos -500.0 
    show pr hurt:
        'pr idle'
        0.60
        'pr hurt'
    with Pause(0.70)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label tseAtkLhRhCam:
    window auto hide
    camera:
        subpixel True 
        linear 0.30 pos (280, 100) zpos -400.0 xrotate 9.0 yrotate -18.0 zrotate -18.0 
    show tse atk:
        subpixel True zpos -700.0 
        parallel:
            'tse idle'
            0.30
            'tse atk'
        parallel: 
            linear 0.30 pos (0.65, 0.6) 
    if Rh.hp > 0:
        show Rh hurt:
            'Rh idle'
            0.30
            'Rh hurt'
    if Lh.hp > 0:
        show Lh hurt:
            'Lh idle'
            0.30
            'Lh hurt'
    with Pause(0.40)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label tseCheerCam: 
    window auto hide
    camera:
        linear 0.30 xpos -1100 zpos -700.0 xrotate 9.0 yrotate -18.0 zrotate 0.0 
    show tse cheer:
        subpixel True 
        'tse idle'
        0.30
        'tse cheer'
    with Pause(0.90)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label tseChillCam: 
    window auto hide
    camera:
        linear 0.30 xpos -1100 zpos -700.0 xrotate 9.0 yrotate -18.0 zrotate 0.0 
    show tse chill:
        subpixel True 
        'tse idle'
        0.30
        'tse chill'
    with Pause(0.90)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label tseRetreat:
    show tse idle:
        subpixel True
        bop_out_time_warp 0.60 xpos -2000
    pause (0.70)
    hide tse
    return

#ww
label wwIdleCam:
    window auto hide
    camera:
        subpixel True 
        pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
        linear 0.50 pos (-280, 200) zpos -200.0 xrotate 7.0 yrotate 0.0 zrotate 5.0 
    with Pause(0.60) 
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label wwAtkPrCam:
    window auto hide
    camera:
        subpixel True 
        pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
        linear 0.30 pos (280, -200) zpos -300.0 xrotate 18.0 yrotate -9.0 zrotate -9.0 
    show ww atk:
        subpixel True 
        parallel:
            'ww idle'
            0.30
            'ww atk'
        parallel:
            pos (-0.2, 0.65) zpos -700.0 
            linear 0.10 pos (0.6, 0.4) zpos -500.0 
    show pr hurt:
        'pr idle'
        0.70
        'pr hurt'
    with Pause(0.70)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label wwAtkLhRhCam:
    window auto hide
    camera:
        subpixel True 
        linear 0.30 pos (280, 100) zpos -400.0 xrotate 9.0 yrotate -18.0 zrotate -18.0 
    show ww atk:
        subpixel True zpos -700.0 
        parallel:
            'ww idle'
            0.30
            'ww atk'
        parallel:
            linear 0.30 pos (0.65, 0.6) 
    with Pause(0.40)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label wwShineCam:
    window auto hide
    camera:
        subpixel True
        linear 0.30 xpos -1000 zpos -700.0 xrotate 9.0 yrotate -9.0 zrotate -18.0 
    show ww shine:
        subpixel True 
        'ww idle'
        0.30
        'ww shine'
    with Pause(0.90)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label wwDefCam:
    window auto hide
    camera:
        subpixel True
        linear 0.30 xpos -1000 zpos -700.0 xrotate 9.0 yrotate -9.0 zrotate -18.0 
    show ww def:
        subpixel True 
        'ww idle'
        0.30
        'ww def'
        linear 0.29 pos (-0.1, 0.5) 
    with Pause(0.90)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label wwGuoinnCam:
    window auto hide
    camera:
        subpixel True
        linear 0.30 xpos -1000 zpos -700.0 xrotate 9.0 yrotate -9.0 zrotate -18.0 
    show ww guoinn:
        subpixel True 
        'ww idle'
        0.30
        'ww guoinn' 
    with Pause(0.90)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label wwRetreat:
    show ww idle:
        subpixel True
        bop_out_time_warp 0.60 xpos -2000
    pause (0.70)
    hide ww
    return

#pr-tse
label prAtkTseCam:
    window auto hide
    camera:
        subpixel True 
        linear 0.30 pos (-350, -300) zpos -300.0 xrotate 18.0 yrotate 9.0 zrotate 0.0 
    show pr sing_atk:
        subpixel True 
        parallel:
            'pr idle'
            0.30
            'pr sing_atk'
        parallel:
            pos (0.9, 450) 
            linear 0.30 pos (-0.08, 400) 
    show tse hurt:
        'tse idle'
        0.30
        'tse hurt'
    with Pause(0.90)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label prBanTseCam:
    window auto hide
    camera:
        subpixel True 
        linear 0.30 pos (-350, -300) zpos -300.0 xrotate 18.0 yrotate 9.0 zrotate 0.0 
    show pr Ban:
        subpixel True 
        parallel:
            'pr idle'
            0.30
            'pr ban'
        parallel:
            pos (0.9, 450) 
            linear 0.30 pos (-0.08, 400) 
    with Pause(0.90)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return
#pr-ww
label prAtkWwCam:
    camera:
        subpixel True 
        linear 0.30 pos (-450, 350) zpos -300.0 xrotate -9.0 yrotate 0.0 zrotate -9.0
    if not winwin_taunt:
        show pr sing_atk:
            subpixel True
            parallel:
                'pr idle'
                0.30
                'pr sing_atk'
            parallel:
                pos (0.9, 450) 
                linear 0.30 pos (0.05, 600) zpos -400 
    elif winwin_taunt:
        show pr sing_atk:
            subpixel True
            parallel:
                'pr idle'
                0.30
                'pr sing_atk'
            parallel:
                pos (0.9, 450) 
                linear 0.30 pos (0.15, 450) zpos -400 
    show ww hurt:
        'ww idle'
        0.30
        'ww hurt'
    with Pause(0.90)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label prBanWwCam:
    camera:
        subpixel True 
        linear 0.30 pos (-450, 350) zpos -300.0 xrotate -9.0 yrotate 0.0 zrotate -9.0
    if not winwin_taunt:
        show pr ban:
            subpixel True
            parallel:
                'pr idle'
                0.30
                'pr ban'
            parallel:
                pos (0.9, 450) 
                linear 0.30 pos (0.05, 600) zpos -400 
    elif winwin_taunt:
        show pr ban:
            subpixel True
            parallel:
                'pr idle'
                0.30
                'pr ban'
            parallel:
                pos (0.9, 450) 
                linear 0.30 pos (0.15, 450) zpos -400 
    with Pause(0.90)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return
#pr-summon
label prSummonLhCam:
    window auto hide
    camera:
        subpixel True 
        pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
        linear 0.30 pos (100, 100) zpos -200.0 xrotate 4.0 yrotate -4.0 zrotate -2.0 
    show Lh idle:
        default
        subpixel True 
        parallel:
            xpos 3000 
            easein_back 0.80 xpos 1900 
        parallel:
            ypos 1300 zpos -700.0 
            linear 0.80 ypos 1300 zpos -700.0 
    with Pause(0.90)
    camera:
        linear 0.1 subpixel True pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label prSummonRhCam:
    window auto hide
    camera:
        subpixel True 
        pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
        linear 0.30 pos (100, 100) zpos -200.0 xrotate 4.0 yrotate -4.0 zrotate -2.0 
    show Rh idle:
        default
        subpixel True 
        parallel:
            xpos 3000 
            easein_back 0.80 xpos 1900 
        parallel:
            ypos 1300 zpos -700.0 
            linear 0.80 ypos 1300 zpos -700.0 
    with Pause(0.90)
    camera:
        linear 0.1 subpixel True pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return
#pr-others
label prMulAtkCam:
    
    window auto hide
    camera:
        subpixel True 
        linear 0.30 pos (-300, -50) zpos -700.0 xrotate 18.0 yrotate 12.0 zrotate 0.0 
    show pr multi_atk:
        subpixel True 
        parallel:
            'pr idle'
            0.30
            'pr multi_atk'
        parallel:
            xpos 0.9 zpos -700.0 
            linear 0.30 xpos 0.05 zpos -400.0 
    pause 0.3
    play sound "SFX/thunder-crack.mp3"
    if winwin.hp > 0:
        show ww hurt:
                'ww idle'
                0.30
                'ww hurt'
    if mc.hp > 0:
        show tse hurt:
            'tse idle'
            0.30
            'tse hurt'
    with Pause(1.75)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label prAngerCam:
    window auto hide
    camera:
        subpixel True 
        linear 0.30 xpos 1000 zpos -500.0 xrotate 12.0 yrotate 10.0 zrotate 9.0 
    show pr anger:
        subpixel True 
        'pr idle'
        0.30
        'pr anger'
    with Pause(0.40)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

#Rh
label RhAtkTseCam:
    window auto hide
    camera:
        subpixel True 
        linear 0.30 pos (-350, -300) zpos -300.0 xrotate 18.0 yrotate 9.0 zrotate 0.0 
    show Rh atk:
        subpixel True 
        parallel:
            'Rh idle'
            0.30
            'Rh atk'
        parallel:
            linear 0.30 pos (100, 1050) 
    show tse hurt:
        'tse idle'
        0.30
        'tse hurt'
    with Pause(0.90)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label RhAtkWwCam:
    camera:
        subpixel True 
        linear 0.30 pos (-450, 350) zpos -300.0 xrotate -9.0 yrotate 0.0 zrotate -9.0
    if not winwin_taunt:
        show Rh atk:
            subpixel True
            parallel:
                'Rh idle'
                0.30
                'Rh atk'
            parallel:
                linear 0.30 pos (200, 1325) zpos -700 
    elif winwin_taunt:
        show Rh atk:
            subpixel True
            parallel:
                'Rh idle'
                0.30
                'Rh atk'
            parallel: 
                linear 0.30 pos (400, 1150) zpos -700 
    show ww hurt:
        'ww idle'
        0.30
        'ww hurt'
    with Pause(0.90)
    camera:
        subpixel True
        easeout 15 pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label RhRetreat:
    window auto hide
    show Rh idle:
        subpixel True  
        bop_out_time_warp 0.60 xpos 3000 
    with Pause(0.70)
    hide Rh
    return

#Lh
label LhRetreat:
    window auto hide
    show Lh idle:
        subpixel True  
        bop_out_time_warp 0.60 xpos 3000 
    with Pause(0.70)
    hide Lh
    return

#resets
label ResetCam:
    camera:
        linear 0.1 subpixel True pos (0, 0) zpos 0.0 xrotate 0.0 yrotate 0.0 zrotate 0.0 
    return

label Relocate:
    stop sound
    if mc.hp > 0:
        show tse idle
    if winwin.hp > 0 and wwrelocate:
        show ww idle
    if mc.hp > 0:
        $ tseshown = True
        show tse idle:
            linear 0.1 pos (-0.25, 0.4) zpos -700.0 
    elif mc.hp <= 0 and tseshown:
        $ tseshown = False
        call tseRetreat
    if winwin.hp > 0:
        $ wwshown = True
        if wwrelocate:
            show ww idle:
                linear 0.1 pos (-0.2, 0.65) zpos -700.0 
    elif winwin.hp <= 0 and wwshown:
        $ wwshown = False
        call wwRetreat
    if principal.hp > 0:
        show pr idle:
            linear 0.1 subpixel True xpos 0.9 ypos 450 zpos -700.0 
    if Lh.hp > 0:
        $ Lhshown = True
        show Lh idle
    elif Lh.hp <= 0 and Lhshown:
        $ Lhshown = False
        call LhRetreat
    if Rh.hp > 0:
        $ Rhshown = True
        show Rh idle:
            linear 0.1 pos (1900, 1300) zpos -700.0
    elif Rh.hp <= 0 and Rhshown:
        $ Rhshown = False
        call RhRetreat
    return
    
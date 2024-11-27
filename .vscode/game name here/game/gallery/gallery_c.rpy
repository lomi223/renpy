screen gallery_c:
    tag menu
    add "CustomUI/bg_gallery.jpg"
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        use gallery_navigation
        grid 3 2:
            add g.make_button(name="c_red", unlocked=im.Scale("CGs/c_red.png",234,132), locked=im.Scale("locked.jpg",234,132))
            add g.make_button(name="c_blue", unlocked=im.Scale("CGs/c_blue.png",234,132), locked=im.Scale("locked.jpg",234,132))
            add g.make_button(name="c_yellow", unlocked=im.Scale("CGs/c_yellow.png",234,132), locked=im.Scale("locked.jpg",234,132))
            add g.make_button(name="c_green", unlocked=im.Scale("CGs/c_green.png",234,132), locked=im.Scale("locked.jpg",234,132))
            add g.make_button(name="c_orange", unlocked=im.Scale("CGs/c_orange.png",234,132), locked=im.Scale("locked.jpg",234,132))
            add g.make_button(name="c_indigo", unlocked=im.Scale("CGs/c_indigo.png",234,132), locked=im.Scale("locked.jpg",234,132))

            spacing 15
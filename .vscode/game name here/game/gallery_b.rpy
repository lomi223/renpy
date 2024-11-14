screen gallery_b:
    tag menu
    add "CustomUI/bg_gallery.jpg"
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        use gallery_navigation
        grid 3 2:
            add g.make_button(name="b_red", unlocked=im.Scale("CGs/b_red.png",234,132), locked=im.Scale("locked.jpg",234,132))
            add g.make_button(name="b_blue", unlocked=im.Scale("CGs/b_blue.png",234,132), locked=im.Scale("locked.jpg",234,132))
            add g.make_button(name="b_yellow", unlocked=im.Scale("CGs/b_yellow.png",234,132), locked=im.Scale("locked.jpg",234,132))
            add g.make_button(name="b_green", unlocked=im.Scale("CGs/b_green.png",234,132), locked=im.Scale("locked.jpg",234,132))
            add g.make_button(name="b_orange", unlocked=im.Scale("CGs/b_orange.png",234,132), locked=im.Scale("locked.jpg",234,132))
            add g.make_button(name="b_indigo", unlocked=im.Scale("CGs/b_indigo.png",234,132), locked=im.Scale("locked.jpg",234,132))

            spacing 15
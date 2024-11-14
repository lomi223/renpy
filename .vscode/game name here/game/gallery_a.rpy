screen gallery_a:
    tag menu
    add "CustomUI/bg_gallery.jpg"
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        use gallery_navigation
        grid 3 2:
            add g.make_button(name="a_red", unlocked=im.Scale("CGs/a_red.png",234,132), locked=im.Scale("locked.jpg",234,132))
            add g.make_button(name="a_blue", unlocked=im.Scale("CGs/a_blue.png",234,132), locked=im.Scale("locked.jpg",234,132))
            add g.make_button(name="a_yellow", unlocked=im.Scale("CGs/a_yellow.png",234,132), locked=im.Scale("locked.jpg",234,132))
            add g.make_button(name="a_green", unlocked=im.Scale("CGs/a_green.png",234,132), locked=im.Scale("locked.jpg",234,132))
            add g.make_button(name="a_orange", unlocked=im.Scale("CGs/a_orange.png",234,132), locked=im.Scale("locked.jpg",234,132))
            add g.make_button(name="a_indigo", unlocked=im.Scale("CGs/a_indigo.png",234,132), locked=im.Scale("locked.jpg",234,132))

            spacing 15
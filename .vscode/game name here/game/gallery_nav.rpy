screen gallery_navigation:
    vbox:
        style_prefix "gallery"
        spacing 20
        xoffset -100
        textbutton "Love Interest A" action ShowMenu("gallery_a")
        textbutton "Love Interest B" action ShowMenu("gallery_b")
        textbutton "Love Interest C" action ShowMenu("gallery_c")
        textbutton "Return":
            action Return()
            yoffset 200

style gallery_button_text:
    idle_color "#808080"
    hover_color "#E17BA2"
    selected_color "#AA1945"
    size 30
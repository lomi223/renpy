image arrow:
    "obj/arrow.png"
    zoom 0.1
image arrow right:
    "arrow"
image arrow left:
    "arrow"
    rotate 180
image arrow up:
    "arrow"
    rotate 270
image arrow down:
    "arrow"
    rotate 90
image closet:
    "obj/closet.png"
    zoom 0.224

screen arrow_right:
    if maze_layout[player_y][player_x + 1] != 1:
        imagebutton:
            xalign 1.0
            yalign 0.5
            idle "arrow right"
            action [Function(move_player, 1, 0),Jump("pos_check")]

screen arrow_left:
    if maze_layout[player_y][player_x - 1] != 1:
        imagebutton:
            yalign 0.5
            idle "arrow left"
            action [Function(move_player, -1, 0),Jump("pos_check")]

screen arrow_up:
    if maze_layout[player_y - 1][player_x] != 1:
        imagebutton:
            xalign 0.5
            idle "arrow up"
            action [Function(move_player, 0, -1),Jump("pos_check")]

screen arrow_down:
    if maze_layout[player_y + 1][player_x] != 1:
        imagebutton:
            xalign 0.5
            yalign 1.0
            idle "arrow down"
            action [Function(move_player, 0, 1),Jump("pos_check")]

screen closet:
    imagebutton:
        xpos 548
        ypos 275
        idle "closet"
        action [Jump("foundu")]
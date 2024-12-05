
init python:
    def can_move(x, y):
        if maze_layout[y][x] != 1:
            return True
        return False

    def move_player(dx, dy):
        global player_x, player_y
        new_x = player_x + dx
        new_y = player_y + dy
        if can_move(new_x, new_y):
            player_x = new_x
            player_y = new_y

screen maze_game():
    frame:
        xalign 1.0
        yalign 0.0
        background "#333"
        
        vbox:
            for y, row in enumerate(maze_layout):
                hbox:
                    for x, cell in enumerate(row):
                        if (x, y) == (player_x, player_y):
                            text "P" xalign 0.5 yalign 0.5 size 32 color "#0F0"
                        elif cell == 1:
                            text "#" xalign 0.5 yalign 0.5 size 32 color "#F00"
                        else:
                            text " . " xalign 0.5 yalign 0.5 size 32 color "#FFF"

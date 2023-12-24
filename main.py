from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)

    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(100, 100, 150, 150)

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw(150, 100, 200, 150)

    c1.draw_move(c2)

    c3 = Cell(win)
    c3.has_top_wall = False
    c3.has_right_wall = False
    c3.draw(150, 150, 200, 200)

    c2.draw_move(c3)

    c4 = Cell(win)
    c4.has_left_wall = False
    c4.draw(200, 150, 250, 200)

    c3.draw_move(c4)

    win.wait_for_close()

main()
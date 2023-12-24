from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)

    cell = Cell(win)
    cell.has_left_wall = False
    cell.draw(50, 50, 100, 100)

    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw(125, 125, 200, 200)

    cell = Cell(win)
    cell.has_top_wall = False
    cell.draw(320, 320, 420, 420)

    cell = Cell(win)
    cell.has_bottom_wall = False
    cell.draw(450, 450, 500, 500)

    win.wait_for_close()

main()
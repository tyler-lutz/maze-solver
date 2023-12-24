from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    line = Line(Point(50, 50), Point(100, 100))
    win.draw_line(line)
    win.wait_for_close()

main()
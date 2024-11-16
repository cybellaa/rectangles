import pgzrun

WIDTH = 500
HEIGHT = 500

def draw():
    screen.fill("grey")
    r=Rect((420,350),(80,150))
    screen.draw.filled_rect(r,"pink")
    c=Rect((0,0),(80,150))
    screen.draw.rect(c,"pink")



pgzrun.go()
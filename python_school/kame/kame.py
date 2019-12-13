from turtle import *

def draw_tuto_example():
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()

if __name__ == "__main__":
    print("Hello kame ")
    draw_tuto_example()

    

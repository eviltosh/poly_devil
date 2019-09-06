import turtle
def draw_poly():
    poly=turtle.Turtle()
    window=turtle.Screen()
    window.bgcolor("red")
    poly.pensize(10)
    poly.color("green")
    poly.speed(1)
    n=int(input("How many sides to your Polygon ? 5+"))
    size=int(input("How big 80-120?"))
    a=180- ((n-2)*180)/n
    for i in range(n):
        poly.forward(size)
        poly.right(a)

draw_poly()

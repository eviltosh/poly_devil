import turtle
mack=turtle.Turtle()
window=turtle.Screen()
window.bgcolor("red")
mack.color("green")
mack.pensize(3)
mack.speed(10)
def pentagram():
    for i in range(5):
        mack.forward(100)
        mack.right(144)

for i in range(5):
    pentagram()
    mack.penup()
    mack.forward(350)
    mack.right(144)
    mack.pendown()

window.mainloop()

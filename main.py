import time
import turtle

board = turtle.Screen()
board.bgcolor("black")
board.title("Catch me If You Can")
board.addshape("donatello.gif")
donatello = turtle.Turtle()
donatello.shape("donatello.gif")
timer = turtle.Turtle()
timer.color("white")
timer.hideturtle()

countdown = 15

for t in range(countdown, -1, -1):
    timer.clear()
    timer.write("Timer: %s" %t, False, "left", ("Arial", 40, "normal"))
    time.sleep(1)

turtle.mainloop()

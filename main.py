import turtle
import random

def setup_game():
    board = turtle.Screen()
    board.bgcolor("black")
    board.screensize(600, 600)
    board.title("Catch me If You Can")
    board.addshape("donatello.gif")

    donatello = turtle.Turtle()
    donatello.shape("donatello.gif")
    donatello.penup()

    timer = turtle.Turtle()
    timer.color("white")
    timer.penup()
    timer.hideturtle()
    timer.setposition(-100, 250)

    score = turtle.Turtle()
    score.color("yellow")
    score.penup()
    score.hideturtle()
    score.setposition(-100, 200)

    return board, donatello, timer, score

def move_target(target):
    target.hideturtle()
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    target.setposition(x, y)
    target.showturtle()

def update_timer(timer, time_left):
    timer.clear()
    timer.write("Time: %s" % time_left, False, "left", ("Arial", 40, "normal"))

def update_score(score, current_score):
    score.clear()
    score.write("Score: %s" % current_score, False, "left", ("Arial", 40, "normal"))

def check_click(x, y, target, score_turtle):
    if target.distance(x, y) < 20:
        score_turtle.current_score += 1
        update_score(score_turtle, score_turtle.current_score)
        move_target(target)

def game_loop(board, donatello, timer, score):
    def update():
        countdown = game_loop.countdown
        update_timer(timer, countdown)

        if countdown <= 0:
            end_game(score, score.current_score)
            return

        move_target(donatello)
        board.ontimer(update, 1000)

    score.current_score = 0
    game_loop.countdown = 15
    update_timer(timer, game_loop.countdown)
    move_target(donatello)
    board.ontimer(update, 1000)

    board.onclick(lambda x, y: check_click(x, y, donatello, score))

def end_game(score_turtle, final_score):
    score_turtle.clear()
    score_turtle.write("Game Over! Final Score: %s" % final_score, False, "center", ("Arial", 40, "normal"))

if __name__ == "__main__":
    board, donatello, timer, score = setup_game()
    game_loop(board, donatello, timer, score)
    turtle.mainloop()

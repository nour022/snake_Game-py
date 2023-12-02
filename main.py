from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)
starting_pos = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for i in starting_pos:
    snake = Turtle("square")
    snake.penup()
    snake.color("#fff")
    snake.goto(i)
    segments.append(snake)
screen.update()


def move_w():
    for s in segments:
        s.forward(10)


is_game_over = False
while not is_game_over:
    screen.update()
    time.sleep(0.5)
    for sn in range(len(segments) - 1, 0, -1):
        new_x = segments[sn - 1].xcor()
        new_y = segments[sn - 1].ycor()
        segments[sn].goto(new_x, new_y)
    segments[0].forward(10)
screen.exitonclick()

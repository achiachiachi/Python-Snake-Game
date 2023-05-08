import time
import turtle
import random
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("black")
board = turtle.Turtle()
board.hideturtle()
board.color("white")
board.penup()
board.sety(board.ycor() + 180)
board.forward(-50)
board.write("Score: 0", font=("Calibri", 20, "bold"))
snake = []
num = 0
score = 0
screen.tracer(0)
#snake setup
for i in range(3):
    square = turtle.Turtle()
    square.color("white")
    square.shape("square")
    square.penup()
    square.speed("fastest")
    square.shapesize(1)
    square.forward(num)
    snake.append(square)
    num += -20
screen.update()
def r():
    if snake[0].heading() == 0:
        print()
    elif snake[0].heading() == 90:
        snake[0].setheading(0)
    elif snake[0].heading() == 180:
        print()
    elif snake[0].heading() == 270:
        snake[0].setheading(0)
def l():
    if snake[0].heading() == 0:
        print()
    elif snake[0].heading() == 90:
        snake[0].setheading(180)
    elif snake[0].heading() == 180:
        print()
    elif snake[0].heading() == 270:
        snake[0].setheading(180)
def up():
    if snake[0].heading() == 0:
        snake[0].setheading(90)
    elif snake[0].heading() == 90:
        print()
    elif snake[0].heading() == 180:
        snake[0].setheading(90)
    elif snake[0].heading() == 270:
        print()
def down():
    if snake[0].heading() == 0:
        snake[0].setheading(270)
    elif snake[0].heading() == 90:
        print()
    elif snake[0].heading() == 180:
        snake[0].setheading(270)
    elif snake[0].heading() == 270:
        print()
def others():
    for i in range(len(snake), 1, -1):
        snake[i-1].setpos(snake[i -2].pos())
        screen.update()
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(0.5)
food.penup()

cc1 = random.randint(-9, 9) * 20
cc2 = random.randint(-9, 9) * 20
food.setpos(cc1,  cc2)

def lose():
    screen.clear()
    screen.bgcolor("black")
    jam = turtle.Turtle()
    jam.setpos(0, 0)
    jam.setheading(0)
    jam.penup()
    jam.forward(-200)
    jam.color("red")
    jam.write("You Lose", font=("Calibri", 80, "bold"))
    jam.hideturtle()
    screen.exitonclick()
def loser():
    if snake[0].xcor() > 250:
        lose()
    if snake[0].xcor() < -250:
        lose()
    if snake[0].xcor() > 250:
        lose()
    if snake[0].ycor() < -250:
        lose()
while True:
    loser()
    snake[0].forward(20)
    time.sleep(0.05)
    time.sleep(0.001)
    if snake[0].xcor().__round__() == float(cc1).__round__():
        if snake[0].ycor().__round__() == float(cc2).__round__():
            square = turtle.Turtle()
            square.color("white")
            square.shape("square")
            square.penup()
            square.speed("fastest")
            square.shapesize(1)
            square.forward(num)
            snake.append(square)
            cc1 = random.randint(-9, 9) * 20
            cc2 = random.randint(-9, 9) * 20
            food.goto(cc1, cc2)
            score += 100
            print(score)
            board.clear()
            board.write("Score: "+ str(score), font=("Calibri", 20, "bold"))
    others()
    #tail interaction
    for i in snake:
        if i.pos() == snake[0].pos():
            pass
        elif snake[0].distance(i) < 5:
            lose()
    screen.onkey(key="d", fun=r)
    screen.onkey(key="a", fun=l)
    screen.onkey(key="w", fun=up)
    screen.onkey(key="s", fun=down)
    screen.listen()



screen.mainloop()
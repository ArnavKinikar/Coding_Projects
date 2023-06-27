import turtle

wn = turtle.Screen()
wn.title("Ping Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Scores
scoreA = 0
scoreB = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = .2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0    Player B: 0", align="center", font=("Courier", 24, "bold"))

# Functions
def paddleAUp():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)


def paddleADown():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def paddleBUp():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddleBDown():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


# Keyboard Binding
wn.listen()
wn.onkeypress(paddleAUp, "w")
wn.onkeypress(paddleADown, "s")

wn.onkeypress(paddleBUp, "Up")
wn.onkeypress(paddleBDown, "Down")

# Main Game Loop
while True:
    wn.update()

    # To move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "bold"))

    # Paddle Collisions
    if (340 < ball.xcor() < 350) and (paddleB.ycor() + 40 > ball.ycor() > paddleB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (paddleA.ycor() + 40 > ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

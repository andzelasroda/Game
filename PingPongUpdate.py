import turtle

#functions
def racket_a_up():
    y = racket_a.ycor()
    y += 20
    racket_a.sety(y)

def racket_a_down():
    y = racket_a.ycor()
    y -= 20
    racket_a.sety(y)

def racket_b_up():
    y = racket_b.ycor()
    y += 20
    racket_b.sety(y)

def racket_b_down():
    y = racket_b.ycor()
    y -= 20
    racket_b.sety(y)


wn = turtle.Screen()
wn.title("PingPong Andzela")
wn.bgcolor("light blue")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# racket A
racket_a = turtle.Turtle()
racket_a.speed(0)
racket_a.shape("square")
racket_a.color("Dark blue")
racket_a.shapesize(stretch_wid=5,stretch_len=1)
racket_a.penup()
racket_a.goto(-350, 0)



# racket B
racket_b = turtle.Turtle()
racket_b.speed(0)
racket_b.shape("square")
racket_b.color("Dark blue")
racket_b.shapesize(stretch_wid=5,stretch_len=1)
racket_b.penup()
racket_b.goto(350, 0)


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("#36454f")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

# pen
pen= turtle.Turtle()
pen.speed(0)
pen.color("dim gray")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Gracz A: 0 Gracz B: 0", align="center",font=("Courier", 24, "bold"))



# up and down buttons
wn.listen()
wn.onkeypress(racket_a_up, "w")
wn.onkeypress(racket_a_down, "s")
wn.onkeypress(racket_b_up, "Up")
wn.onkeypress(racket_b_down, "Down")


# loop
while True:
    wn.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Gracz A: {} Gracz B: {}".format(score_a, score_b), align="center", font=("Rockwell", 24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Gracz A: {} Gracz B: {}".format(score_a, score_b), align="center", font=("Rockwell", 24, "bold"))


    if racket_a.ycor() < -300:
        racket_a.goto(-350,-300)

    if racket_a.ycor() > 300:
        racket_a.goto(-350,300)

    if racket_b.ycor() > 300:
        racket_b.goto(350,300)

    if racket_b.ycor() < -300:
        racket_b.goto(350,-300)


    # Racket and pingpong ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < racket_b.ycor() + 40 and ball.ycor() > racket_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < racket_a.ycor() + 40 and ball.ycor() > racket_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

    if (racket_a.xcor() > 300 and racket_a.xcor() < 350) and (ball.ycor() < racket_b.ycor() + 40 and ball.ycor() > racket_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() < -350) and (
        ball.ycor() < racket_a.ycor() + 40 and ball.ycor() > racket_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
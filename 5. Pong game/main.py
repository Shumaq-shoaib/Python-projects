from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from scoreboard import Score
import time

PADDLE1 = (-400, 0)
PADDLE2 = (400, 0)

# Set up the game screen
game_screen = Screen()
game_screen.setup(1000, 700)
game_screen.bgcolor("black")
game_screen.title("Pong")
game_screen.tracer(0)

# Create the paddles
paddle1 = Paddle(PADDLE1)
paddle2 = Paddle(PADDLE2)

# Create ball
ball = Ball()

# create score
score = Score()
# Add event listeners for paddle movement
game_screen.listen()
game_screen.onkey(paddle1.move_up, "Up")
game_screen.onkey(paddle1.move_down, "Down")


# Function to update the game
def update_game():
    game_screen.update()
    game_screen.onkey(paddle1.move_up, "Up")
    game_screen.onkey(paddle1.move_down, "Down")

    game_screen.onkey(paddle2.move_up, "w")
    game_screen.onkey(paddle2.move_down, "s")


# Start the game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    update_game()
    ball.move()

    # Bounce from ceil and floor
    if (ball.ycor() > 340) or (ball.ycor() < -340):
        ball.bounce_y()

    # bounce from paddle
    if (ball.distance(paddle2) < 50 and ball.xcor() > 375) or (ball.distance(paddle1) < 50 and ball.xcor() < -375):
        ball.bounce_x()
        ball.move_speed *= 0.9

    # right paddle misses
    if ball.xcor() > 410:
        ball.reset_postion()
        score.left_point()
        ball.reset_speed()

    # left paddle misses
    if ball.xcor() < -410:
        ball.reset_postion()
        score.right_point()
        ball.reset_speed()

# Exit the game screen
game_screen.exitonclick()

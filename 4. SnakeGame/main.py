from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import Score

score = Score()
food = Food()
sc = Screen()
snake = Snake()

sc.setup(width=600, height=600)
sc.title("SnakeGame")
sc.bgcolor("black")
sc.tracer(0)

sc.listen()
sc.onkeypress(snake.up, "Up")
sc.onkeypress(snake.left, "Left")
sc.onkeypress(snake.right, "Right")
sc.onkeypress(snake.down, "Down")

game_is_on = True
while game_is_on:
    sc.update()
    time.sleep(0.1)
    snake.move_snake()
    # detect collision with food
    if snake.head.distance(food) < 15:
        score.increase_score()
        food.refresh()
        snake.extend()
        print(score.pos())

    # detect collision with any block
    for segments in snake.objects[1:]:
        if snake.head.distance(segments) < 10:
            game_is_on = False
            score.game_over()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()
sc.exitonclick()

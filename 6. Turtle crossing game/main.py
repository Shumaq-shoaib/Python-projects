import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

turtle = Player()
screen = Screen()
car_manager = CarManager()
score = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

screen.onkeypress(turtle.go_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            score.game_over()
    if turtle.is_at_finish():
        turtle.go_to_start()
        car_manager.increase_speed()
        score.increase_level()
screen.exitonclick()
  
import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
car_manager=CarManager()
scoreboard = Scoreboard()





screen.listen()
screen.onkey(player.move_forward,'Up')


game_is_on = True



while game_is_on:

    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
#collision with car
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()

#turtle crosses the side
    if player.ycor()>280:
        scoreboard.update_score()
        player.next_round()
        car_manager.speed_up()

screen.exitonclick()




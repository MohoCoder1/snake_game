import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

game_is_on = True
screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Right", fun=snake.move_right)
screen.onkey(key="Left", fun=snake.move_left)

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_segment()
        scoreboard.add_score()

    if snake.head.xcor() > 245 or snake.head.xcor() < -245 or snake.head.ycor() > 245 or snake.head.ycor() < -245:
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()

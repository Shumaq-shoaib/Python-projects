from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.x = 20
        self.y = 0
        self.blocks = 3
        self.objects = []
        self.create_snake()
        self.head = self.objects[0]

    def create_snake(self):
        for _ in range(self.blocks):
            self.add_segment()

    def add_segment(self):
        tim = Turtle("square")
        tim.hideturtle()
        tim.speed("fastest")
        tim.color("white")
        # tim.penup()
        tim.goto(self.x, self.y)
        tim.speed(2)
        tim.showturtle()
        self.objects.append(tim)
        self.x -= 20

    def extend(self):
        self.add_segment()

    def move_snake(self):
        for seg_num in range(len(self.objects) - 1, 0, -1):
            new_x = self.objects[seg_num - 1].xcor()
            new_y = self.objects[seg_num - 1].ycor()
            self.objects[seg_num].goto(new_x, new_y)
        self.objects[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

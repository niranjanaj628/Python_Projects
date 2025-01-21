from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager():
    def __init__(self):
            self.cars=[]
            self.STARTING_MOVE_DISTANCE = 5
            self.MOVE_INCREMENT = 5
    def create_car(self):
        if random.randint(1,6)==2:
            car=Turtle()
            car.shape('square')
            car.shapesize(1,2)
            car.penup()
            car.speed(2)
            car.color(random.choice(COLORS))
            y=random.randint(-250,250)
            car.goto(290,y)
            self.cars.append(car)
        
    def move_car(self):
        for car in self.cars:
            car.backward(self.STARTING_MOVE_DISTANCE)
            
    def level_up(self):
        self.STARTING_MOVE_DISTANCE+=self.MOVE_INCREMENT
        self.move_car()
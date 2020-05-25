import turtle
import random


#people list will store all the people objects
people =[]
#launch window and set up GUI
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Simulator")
#initialize patient0
patient0 = turtle.Turtle()

#method will set up the amount of people objects specified by user
def setPeople(amount):
    for _ in range(amount):
        people.append(turtle.Turtle())
    for person in people:
        person.shape("circle")
        person.color("green")
        person.penup()
        person.speed(0)
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        person.goto(x,y)
        person.dy = 0
        person.dx = 2

#set up patient 0 and spwn in the window
def setPatientZero():
    patient0.shape("circle")
    patient0.color("red")
    patient0.penup()
    patient0.speed(0)
    x0 = random.randint(-290,290)
    y0 = random.randint(-290,290)
    patient0.goto(x0,y0)
    patient0.dy = 0
    patient0.dx = 2

#Amanda Maglaras
#amanda.maglaras1@marist.edu
#This project allows us to draw a traffic light using functions


from graphics import *

#This will name and set the size of the window
win = GraphWin("Traffic Light", 175, 175)
  

#This will draw the body of the traffic light
def draw_light_body(x, y, length, width):
    body=Rectangle(Point(x,y), Point (width, length))
    body.setOutline("black")
    body.setFill("white")
    body.draw(win)

#This will draw the lamps
def draw_lamp(color, x, y, radius):
    lamp=Circle(Point(x, y), radius)
    lamp.setOutline("black")
    lamp.setFill(color)
    lamp.draw(win)

#This will draw the entire traffic light 
def draw_traffic_light(x, y):
    draw_light_body(16, 16, 136, 64)
    draw_lamp("red", 40,36, 16)
    draw_lamp("yellow", 40, 76, 16)
    draw_lamp("green", 40, 116, 16)

#This will call the function
draw_traffic_light(16, 16)  

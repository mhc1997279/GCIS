"""
This code is used to do pixart and it will draw pixal based on your string and it will read a text file and make the art
"""
import turtle as turta
from turtle import Screen

PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20
DEFAULT_PEN_COLOR = 'black'
DEFAULT_PIXEL_COLOR = 'white'

def initialization(turta):
    '''Function which sets the speed, pencolor and the starting point of the turtle to start drawing'''
    turta.speed(0)
    turta.penup()
    turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * ROWS / 2) # initial coordinate of the turtle to begin drawing
    turta.setheading(0)
    turta.pendown()
    turta.pencolor(DEFAULT_PEN_COLOR)
    turta.fillcolor(DEFAULT_PIXEL_COLOR)

def get_color(x):
    '''Returns the color corresponding to a given code.'''
    if x==0:
        y="black"
    elif x==1:
        y="white"
    elif x==2:
        y="red"
    elif x==3:
        y="yellow"
    elif x==4:
        y="orange"
    elif x==5:
        y="green"
    elif x==6:
        y="yellowgreen"
    elif x==7:
        y="sienna"
    elif x==8:
        y="tan" 
    elif x==9:
        y="gray"
    elif x=="A":
        y="darkgray"
    else:
        y=None     
    return y

def draw_color_pixel(x,turta):
    '''Draws a single pixel of the specified color.'''
    turta.speed(0)
    turta.fillcolor(x)
    turta.begin_fill()
    i=0
    while i<4:
        turta.forward(30)
        turta.left(90)
        i+=1
    turta.end_fill()

def draw_pixel(x, turta):
    '''Draws a single pixel of a color based on its code.'''
    turta.speed(0)
    turta.fillcolor(get_color(x))
    turta.begin_fill()
    i=0
    while i<4:
        turta.forward(30)
        turta.left(90)
        i+=1
    turta.end_fill()


def draw_line_from_string(color_string, turta):
    '''Draws a line of pixels based on a string of color codes.'''
    row=len(color_string)
    j=0
    while j<row:
        for i in color_string:
            if i.isdigit():
                i= int(i)
            l=get_color(i)
            draw_color_pixel(l,turta)
            turta.forward(30)
            j+=1

def draw_shape_from_string(u,p,turta):
    '''It checks wether the row is odd or even or the else will check wether the string is correct'''
    while True:
        if u=="yes":
            row1 = "20202020202020202020"
            row2 = "02020202020202020202"
            if p%2==0:
                draw_line_from_string(row1, turta)
                break
            else:
                draw_line_from_string(row2, turta)
                break
        else:
            color_string = input("Enter string of colors (or press Enter to finish): ")
            if color_string=="":
                break
            for i in color_string:
                if i.isdigit():
                    color_value = int(i)
                else:
                    color_value = i
            if get_color(color_value) is None:
                print("Invalid color entered. Stopping the drawing process.")
                break
            draw_line_from_string(color_string, turta)
            break

def draw_grid(x,y,turta):
    '''Draws a grid of shapes using predefined patterns.'''
    i=0
    while i<20:
        turta.penup()
        turta.goto(x,y)
        turta.pendown()
        j="yes"
        draw_shape_from_string(j,i,turta)
        i+=1
        y=y-30

def draw_shape_from_file(x,y,turta):
    '''Draws shapes from a file containing color strings.'''
    f=open("C:\\Users\\MOHAMMED\\Downloads\\drawing02.txt","r")
    read=f.readlines()
    f.close()
    for i in read:
        color_string = i.strip()
        draw_line_from_string(color_string, turta)
        y=y-30
        turta.penup()
        turta.goto(x,y)
        turta.pendown()


def main():
    '''Main function to initialize the turtle and execute drawing functions.'''
    '''initialization(turta)
    get_color(5)
    get_color(2) 
    get_color("X") 
    draw_color_pixel("red", turta)
    draw_pixel(5, turta) '''
    draw_line_from_string ('01Z3421', turta) 
    turta.penup()
    turta.goto(-300,300)
    turta.pendown()
    draw_grid(-300,300,turta)
    turta.clear()
    turta.penup()
    turta.goto(-300,300)
    turta.pendown()
    draw_shape_from_file(-300,300,turta)

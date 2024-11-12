from pixart import *
import turtle as turta

def main():
    initialization(turta)
    get_color(5)
    get_color(2) 
    get_color("X") 
    draw_color_pixel("red", turta)
    draw_pixel(5, turta) 
    draw_line_from_string ('01A753421', turta) 
    turta.penup()
    turta.goto(-300,300)
    turta.pendown()
    draw_grid(-300,300,turta)
    turta.clear()
    turta.penup()
    turta.goto(-300,300)
    turta.pendown()
    draw_shape_from_file(-300,300,turta)

if __name__=="__main__":
    main()
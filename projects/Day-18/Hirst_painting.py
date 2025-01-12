#Hirst painting : Day -18
import turtle as t
import random 
# import colorgram

# extracting the most widely used colors out of a hister painting

# rgb_colors=[]
# colors=colorgram.extract('dot_painting.jpeg',15)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     rgb_colors.append((r,g,b))
    
# print(rgb_colors)

def dot_painting(color_list,size):
    '''Draws a dot painting based on a list of colors and size (give n in n x n)'''
    tommy.speed('fastest')
    tommy.penup()
    tommy.setheading(135)
    tommy.forward(250)
    tommy.setheading(0)
    tommy.speed('fastest')
    tommy.hideturtle()
    for i in range(size):
        for j in range(size):     
            tommy.dot(15,random.choice(color_list))
            tommy.penup()
            tommy.forward(40)
        
            if j==size-1:
                 tommy.right(90)
                 tommy.forward(40)
                 tommy.right(90)
                 tommy.forward(40*size)
                 tommy.right(180)
        
    
color_list=[(225, 215, 204), (213, 161, 100), (34, 111, 159), (230, 209, 216), (199, 136, 155), (124, 59, 88), (207, 222, 210), (151, 18, 46), (225, 201, 107), (122, 164, 193), (202, 81, 106), (42, 124, 92), (153, 159, 47), (170, 73, 48), (212, 84, 64)]
#creating the turtle instance
tommy=t.Turtle()
t.colormode(255)

dot_painting(color_list,10)

#creating a screen instance
screen=t.Screen()
screen.exitonclick()
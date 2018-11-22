import turtle
Password = ''' Please Enter Code to Access StringArt
ex. 3o4cc0'''
screen = turtle.getscreen()

t_program = screen.textinput('String Art Login', Password)
print(t_program)
if t_program == '3o3':
        Test = ''' Please Type the Background Color You Would Like.
(Black or White)'''
else:
    print("Incorrect Try Again")
screen = turtle.getscreen()
b_program = screen.textinput('Select a Background', Test)
print("You selected",b_program)
if b_program == 'Black':
    turtle.bgcolor("black")
        break
if b_program == 'White':
    break
else:
    print("Sorry, That is not a color that is available")
    exit

    
#------------------------------------------------------------- Starts Up Window




    #Opens Window
    loadWindow = turtle.Screen()
    turtle.colormode(255)

    turtle.speed(0)

#Make sure that you do 255/f's coefficient, otherwise you get an error
    #ex. 255/15 = 17  set f > 17: f = 17
    for i in range(23):
        turtle.circle(5*i)
        turtle.circle(-5*i)
        turtle.left(i)
        f=i
        if f > 15:
            f = 15
turtle.color(3*i,10*i,5*f)
        
exit




#---------------------------------------------------------------------
#color Library

'''
Green = (3*i,10*i,5*f)

Orange = (10*i,5*i,f)

Pink = (10*i,5*i,5*f)

Blue = (1*i,1*i,15*f)
'''
        
        



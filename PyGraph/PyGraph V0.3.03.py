import pygame
import math
import fractions

pygame.init()
    
# Window
SCREENSIZE = (600, 600)
TITLE = "PyGraph 0.3.03"
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 500 #250


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PURPLE = (150, 0, 150)

#Constants
POINTS = list()
''' format '''
vertex_points=[{'color':WHITE,
                'vertex':[0,0],
                'con_vertex':[300,300]}]
x_intercept_points=[{'color':WHITE,
                     'x_int':[0],
                     'con_x_int':[[300,300]]}]
vertex_points=[]
x_intercept_points=[]
''' function bools '''
VERTEX = False
X_INTERCEPTS = False


# Window
x_min = -20
x_max = 20
y_min = -20
y_max = 20

X_LEN = SCREENSIZE[0]
Y_LEN = SCREENSIZE[1]

dashesx,dashesy = x_max-x_min,y_max-y_min
dashes_x,dashes_y = [],[]

distancex = X_LEN//dashesx
distancey = Y_LEN//dashesy

for x in range(dashesx):
    dashes_x.append(x*(X_LEN//dashesx))
for y in range(dashesy):
    dashes_y.append(y*(Y_LEN//dashesy))




###-----Functions-----###

''' Variable Functions '''
def range_x(x):
    #range function
    if x < 0:
        range_len = (-x * 2) + 1
    else:
        range_len = (x * 2)+ 1
    return range_len
def sqrt(x):
    return x**(1/2)
def cbrt(x):
    return x**(1/3)
def quad(a,b,c):
    x1 = (-b + sqrt((b**2)-(4*a*c)))/2*a
    x2 = (-b - sqrt((b**2)-(4*a*c)))/2*a
    print('x = '+str(x1)+' or x = '+str(x2))
    return [x1,x2]
def standard_form(vertex):
    print("f(x) = a(x-("+\
          str(vertex[0])+\
          "))^2 + ("+\
          str(vertex[1])+\
          ")")
def leading_coefficient_test(coef=-4,exponent=3):
    if coef < 0:
        pass

def vertical_line(x):
    points=[]
    y=-200
    for i in range(400):
        points.append([x,y])
        y+=1
    return points
def fraction(num):
    return fractions.Fraction(num).limit_denominator()
def compound_interest(P,r,t,n=None):
    if n==None:
        A=P*(math.e**(r*t))
    else:
        A=P*(1+(r/n))**(n*t)
    return A

##def exponential(x, n, f=lambda x,n:x**n):
##	rangen = range_x(n)
##	print("x^n  |  xn")
##	for i in range(rangen):
##		print(str(x)+"^"+str(n), end='   ')
##		print(f(x,n))
##		n+=1
##    

''' Algebraic Functions '''
def graph_function(x=-200,
                   fx=lambda x:x+1,
                   bools=[],
                   range_len=4000,
                   x_interval=.1):
    points = []
    
    for p in range(range_len):
        bool_passed=[]
        for b in range(len(bools)):
            bool_passed.append(False)
        passed=False
        #multiple conditionals
        for b in bool_passed:
            b=False
        #no conditionals
        if len(bools) == 0:
            passed=True
        #conditionals
        
        if len(bools)>0:
            i_b = 0
            for b in bools:
                try:
                    if b(x):
                        passed=True
                        bool_passed[i_b] = True
                except ZeroDivisionError:
                    pass
                i_b += 1
            for b in bool_passed:
                if b==False:
                    passed=False
        if passed:
            try:
                y = fx(x)
                points.append([x,y])
            except ZeroDivisionError:
                pass
        x += x_interval
    return points



def exponential_function(x=-200,
                         n=-5,
                         fx=lambda x,n:x**n,
                         bools=[],
                         range_len=4000,
                         range_n=10,
                         x_interval=.1,
                         n_interval=1):
    points = []
    
    for p in range(range_n):
        bool_passed=[]
        for b in range(len(bools)):
            bool_passed.append(False)
        passed=False
        #multiple conditionals
        for b in bool_passed:
            b=False
        #no conditionals
        if len(bools) == 0:
            passed=True
        #conditionals
        if len(bools)>0:
            i_b = 0
            for b in bools:
                try:
                    if b(x):
                        passed=True
                        bool_passed[i_b] = True
                except ZeroDivisionError:
                    pass
                i_b += 1
            for b in bool_passed:
                if b==False:
                    passed=False
                    
        # fx function
        if passed:
            try:
                y = fx(x,n)
                points.append([n,y])
            except ZeroDivisionError:
                pass
        x += x_interval
        n += n_interval
    return points

#            base  exponent
def exponential(x, n, f=lambda x,n:x**n,rangen=None):
    if rangen==None:
        rangen = range_x(n)
    else:
        rangen = rangen
    points = []
    for i in range(rangen):
        fx = (f(x,n))
        points.append([n, fx])
        n+=1
            
    return points
        
''' Graphing Functions/Converting To Graph '''
def convert_points(points=[]):
    drawn_points = []
    i = 0
    for p in points:
        error=False
        #for errors, make the error number 0
        try:
            x=math.floor(p[0] * distancex)
            y=math.floor(p[1] * distancey)
        except TypeError:
            error=True
        if not error:
            drawn_points.append([300,300])
            drawn_points[i][0] += math.floor(p[0] * distancex)
            drawn_points[i][1] -= math.floor(p[1] * distancey)
            i += 1
    return drawn_points
def connect_lines(points=[],color=GREEN,line_width=5):
    if len(points) >= 2:
        for p in range(len(points)):
            if p >= len(points)-1:
                break
            else:
                start=points[p]
                end = points[p+1]
                pygame.draw.line(screen,color,start,end,line_width)

''' Input Functions '''
def var_input(points=[],
              color=RED,
              draw_vertex=False,
              vertex=[0,0],
              draw_intercepts=False,
              function=lambda x:x):
    con_vertex=convert_points([vertex])
    global POINTS
    f = convert_points(points)
    POINTS.append({'points':points,
                   'draw_points':f,
                   'color' :color,
                   'draw_vertex':draw_vertex,
                   'vertex':vertex,
                   'con_vertex':con_vertex[0],
                   'draw_intercepts':draw_intercepts,
                   'function':function})

''' Predefined Graphing Functions '''
def Parent_Functions():
    #constant
    var_input(graph_function(-20,lambda x:4), RED)
    #identity
    var_input(graph_function(-5,lambda x:x-3), BLUE)
    #squaring
    var_input(graph_function(-5,lambda x:x**2), GREEN)
    #cubing
    var_input(graph_function(-5,lambda x:x**3), WHITE)
    #square root
    var_input(graph_function(-5,lambda x:sqrt(x)), PURPLE)
    #reciproal
    var_input(graph_function(-5,lambda x:1/x), YELLOW)
    #absolute value
    var_input(graph_function(-20,lambda x:abs(x)), CYAN)
    
    #standard value is f(x) = a(x-h)^2 + k

def Square_Roots():
    var_input(graph_function(-200,lambda x:sqrt(x)), GREEN)
    var_input(graph_function(-200,lambda x:sqrt(-x)), BLUE)
    var_input(graph_function(-200,lambda x:-sqrt(x)), RED)
    var_input(graph_function(-200,lambda x:-sqrt(-x)), YELLOW)

def Cube_Roots():
    var_input(graph_function(-200,lambda x:cbrt(x)), GREEN)
    var_input(graph_function(-200,lambda x:cbrt(-x)), BLUE)
    var_input(graph_function(-200,lambda x:-cbrt(x)), RED)
    var_input(graph_function(-200,lambda x:-cbrt(-x)), YELLOW)


def x_intercepts(fx):
    #try to do another graph function but limited parameters
    points = graph_function(x=-50,fx=fx,bools=[],range_len=200,x_interval=.5)
    x_ints = []
    
    for p in points:
        #.5 works
        if p[1] < 0.5 and p[1] > -0.5:
            # Try point -= .1 10 times and opposite 10 times
            #if y = 0
            if fx(p[0])==0:
                x_ints.append(p[0])
##            new_points=graph_function(x=-1,fx=fx,bools=[],
##                                      range_len=100,
##                                      x_interval=.01)
##
##            for np in new_points:
##                if np[1] <=.1 and np[1] >= -.1:
##                    x_ints.append(np[0])
    return x_ints

def aos(x, color=GREEN):
    var_input(points=vertical_line(x),
              color=color)   

# Points         
POINTS = []

# Predefined Functions

##Parent_Functions()
##Square_Roots()
##Cube_Roots()
##aos(4,GREEN)

# User Defined Functions
''' standard graph function '''
##var_input(points= graph_function(-50,
##                                 fx=lambda x:6-(x**4),
##                                 bools=[],
##                                 range_len=200,
##                                 x_interval=.5),
##          color=GREEN)

''' exponential function '''
var_input(points=exponential(10,
                             -5,
                             lambda x,n:x**n,
                             rangen=None),
          color=GREEN)
var_input(points=exponential(10,
                             1,
                             lambda x,n:math.log(n,x),
                             rangen=5),
          color=RED)



''' Version Log/Notes '''
'''
0.1.01
    -built, basic functions, can run almost any
    equation in chapter 1
0.2.01
    #fix points with errors
        #complex numbers
        #divide by zero
    
    -more focused on chapter 2, updates may be based on
       chapter at this point
    #screen blit vertex
    

0.2.02
    -make multiple vertices
    #draw axis of symmetry?
    #draw x-intercepts
        Xuse the quad function to get x-intercepts
        #used new function

0.2.03
    -Polynomial Division and Synthetic Division
        -Use MODULUS Symbol to get remainder

0.2.04
    -Complex numbers
        -Numbers.Complex()
    -use complex number error
    -it works like a polynomial the same way that x does

0.2.06
    -Vertical and Horizontal Asymptotes

0.2.07
    -Nonlinear Inequalities

0.3.01
    -exponential functions and logarithms
    #change graph function to accept exponent variable
        #x=var, n=exponent. do x**n

0.3.02
    -logarithmic Functions
        -use math.log with fractions.Fraction
        -math.e
        -math.log(x[, base]) (natural)
        -math.log10(base)    (common)

0.3.03
    -Properties of Logarithms
    -simplification of logarithmic expressions

0.3.04
    -Exponential & Logarithmic Equations
    


        
        -----planned-----

Add click point function somewhere, or show a point.
more focused on specifics

Add screenblits for points
    point(x,y) blit(x+5,y-5)(bottom left corner)
        0.2.01: points for vertex
        0.2.02: points for x-intercepts

Do domain and range for inputs, but instead of infinity,
    do about -1000 to 1000, so that it wont break the
    computer
        (python math function may have infinity variable)

Do inputs for functions, save lambdas to temporary text.py
    file so that it could run it, perhaps use import
    text.py file to use the function

Rewrite functions as class objects
    do this for the bigger functions


'''
printed_overflow=False
# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True       
            
        

    # Game logic                
    # Drawing Functions
    screen.fill(BLACK)
    ''' Graph '''                    
    pygame.draw.line(screen, WHITE, [000, 300], [600, 300], 1)
    pygame.draw.line(screen, WHITE, [300, 000], [300, 600], 1)
    for x in dashes_x:
        start = [x, (-2+300)]
        end =   [x, ( 2+300)]
        pygame.draw.line(screen, WHITE, start, end)
    for y in dashes_y:
        start = [(-2+300), y]
        end =   [( 2+300), y]
        pygame.draw.line(screen, WHITE, start, end)

    ''' Points and Lines '''
    for obj in POINTS:
        try:
            for point in obj['draw_points']:
                pygame.draw.circle(screen, obj['color'], point, 2)
            connect_lines(obj['draw_points'], obj['color'],4)

            #creating vertex list/appending to vertex list
            if obj['draw_vertex']:
                vertex_points.append({'color':obj['color'],
                                      'vertex':obj['vertex'],
                                      'con_vertex':obj['con_vertex']})
            if obj['draw_intercepts']:
                x_ints = x_intercepts(obj['function'])
                xpoints = []
                for x in x_ints:
                    xpoints.append([x,0])
                
                
                x_intercept_points.append({'color':obj['color'],
                                           'x_int':x_ints,
                                           'con_x_int':convert_points(xpoints)})
                    
            
        except OverflowError:
            print('Overflow Error, please use smaller values')
            pass

    ''' Screen Blit '''
    font = pygame.font.Font(None,25)
    # Vertex
    if VERTEX:
        for vertex in vertex_points:
            text = font.render("("+\
                               str(vertex['vertex'][0])+","+\
                               str(vertex['vertex'][1])+")",
                               True,
                               vertex['color'])
            v_pos = vertex['con_vertex']
            screen.blit(text, [v_pos[0]+7,
                               v_pos[1]+7])

    # x-intercepts
    if X_INTERCEPTS:
        for function in x_intercept_points:
            texts = []
            text_poses = []
            for x in function['x_int']:
                text = font.render(str(x),
                                   True,
                                   function['color'])
                texts.append(text)
            text_poses = function['con_x_int']

            for i in range(len(texts)):
                x_pos = text_poses[i]
                screen.blit(texts[i],
                            [x_pos[0]+4,
                             x_pos[1]+7])
                
                                    
        
##    point = [300,300]
##    
##    font = pygame.font.Font(None, 20)
##    text = font.render("(0,0)", True, GREEN)
##    screen.blit(text, [point[0]+3,point[1]+3])
    

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)


# Close window on quit
pygame.quit()


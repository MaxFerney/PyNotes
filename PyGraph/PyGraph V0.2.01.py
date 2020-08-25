import pygame
import math

pygame.init()
    
# Window
SCREENSIZE = (600, 600)
TITLE = "PyGraph 0.2.01"
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

#dashesx = xmax-xmin
#dashesy = ymax-ymin

#Constants

# Window
x_min = -20
x_max = 20
y_min = -20
y_max = 20

X_LEN = SCREENSIZE[0]
Y_LEN = SCREENSIZE[1]
##dashes = 200
dashesx = x_max-x_min
dashesy = y_max-y_min
dashes_x = []
dashes_y = []
##distance = SCREENSIZE[0]//dashes
distancex = X_LEN//dashesx
distancey = Y_LEN//dashesy

##for i in range(dashes):
##    dashes_x.append(i*(X_LEN//dashes))
##    dashes_y.append(i*(Y_LEN//dashes))
for x in range(dashesx):
    dashes_x.append(x*(X_LEN//dashesx))
for y in range(dashesy):
    dashes_y.append(y*(Y_LEN//dashesy))



#Functions

##def abs_val(var):
##    if var < 0:
##        var = -1 * var
##    else:
##        var = var
##    return var

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
    print("f(x) = (x-("+\
          str(vertex[0])+\
          "))^2 + ("+\
          str(vertex[1])+\
          ")")
    


def graph_function(x=-200,
                   fx=lambda x:x+1,
                   bools=[],
                   range_len=4000,
                   x_interval=.1):
    points = []
    #range function
##    if x < 0:
##        range_len = (-x * 2) + 1
##    else:
##        range_len = (x * 2)+ 1
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
        
#drawing on graph
#----------{
def convert_points(points=[]):
    drawn_points = []
    i = 0
    for p in points:
        error=False
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
#}----------

POINTS = list()
vertex_points=[{'color':WHITE,
                'vertex':[0,0],
                'con_vertex':[300,300]}]
def var_input(points=[],color=RED,draw_vertex=False,vertex=[0,0]):
    con_vertex=convert_points([vertex])
    global POINTS
    f = convert_points(points)
    POINTS.append({'points':points,
                   'draw_points':f,
                   'color' :color,
                   'draw_vertex':draw_vertex,
                   'vertex':vertex,
                   'con_vertex':con_vertex[0]})

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
    
    #standard value is f(x) = (x-h)^2 + k

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

        
        

#Points
                
POINTS = []

# Predefined Functions

##Parent_Functions()
##Square_Roots()
##


var_input(points= graph_function(-200,
                                 fx=lambda x:x**3,
                                 bools=[],
                                 range_len=4000),
          color=GREEN,
          draw_vertex=False,
          vertex=[0,0])
var_input(points= graph_function(-200,
                                 fx=lambda x:x**4,
                                 bools=[],
                                 range_len=4000),
          color=RED,
          draw_vertex=False,
          vertex=[0,0])





##for o in POINTS:
##    for p in o['points']:
##        print(p)


'''
0.0.01
    -built, basic functions, can run almost any
    equation in chapter 1
0.0.02
    #fix points with errors
        #complex numbers
        #divide by zero
    -draw axis of symmetry?
    -more focused on chapter 2, updates may be based on
       chapter at this point
    #screen blit vertex
    -make multiple vertices

        -----planned-----

Add click point function somewhere, or show a point.
more focused on specifics

Add screenblits for points
    point(x,y) blit(x+5,y-5)(bottom left corner)
        0.0.02: points for vertex

Do domain and range for inputs, but instead of infinity,
    do about -1000 to 1000, so that it wont break the
    computer

Do inputs for functions, save lambdas to temporary text.py
    file so that it could run it, perhaps use import
    text.py file to use the function
'''
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
##            connect_lines(obj['draw_points'], obj['color'],2)
            if obj['draw_vertex']:
                vertex_points.append({'color':obj['color'],
                                      'vertex':obj['vertex'],
                                      'con_vertex':obj['con_vertex']})
                
            
        except OverflowError:
##            print('Overflow Error, please use smaller values')
            pass

    ''' Screen Blit '''
    font = pygame.font.Font(None,30)
    for vertex in vertex_points:
        text = font.render("("+\
                           str(vertex['vertex'][0])+","+\
                           str(vertex['vertex'][1])+")",
                           True,
                           vertex['color'])
        v_pos = vertex['con_vertex']
        screen.blit(text, [v_pos[0]+5,
                           v_pos[1]+5])
        
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


import pygame
import os
import time
import webbrowser

dots = [{'x': 0, 'y': 0, 'color': (255, 255, 255)}]
pygame.init()

"""

#file name input option?


webbrowser.open("filename")
    works perfectly.

#show list of files, then selecting a file opens it

Allow name of file, since this is PyPaint, link it
    the PyNotes Main Program.

separate the folder which each file is saved by
    the current date(first 5 or so characters)


cursor = pygame.cursors.compile(pygame.cursors.textmarker_strings)
pygame.mouse.set_cursor(*cursor)


compile(strings, black=’X’, white=’.’, xor=’o’)


thickarrow_strings = (               #sized 24x24
  "XX                      ",
  "XXX                     ",
  "XXXX                    ",
  "XX.XX                   ",
  "XX..XX                  ",
  "XX...XX                 ",
  "XX....XX                ",
  "XX.....XX               ",
  "XX......XX              ",
  "XX.......XX             ",
  "XX........XX            ",
  "XX........XXX           ",
  "XX......XXXXX           ",
  "XX.XXX..XX              ",
  "XXXX XX..XX             ",
  "XX   XX..XX             ",
  "     XX..XX             ",
  "      XX..XX            ",
  "      XX..XX            ",
  "       XXXX             ",
  "       XX               ",
  "                        ",
  "                        ",
  "                        ")




  
"""

def UFL(folder="Files\\Paint"):
    global files
    files = list()
    cwd = os.getcwd()
    path = os.path.join(cwd, folder)
    print("------------FILES------------")
    for c in os.walk(path).__next__()[2]:
        print(c)
        files.append(c)
        
##def load():
##    UFL()
##    global dots
##    dots = list()
##    print("Do you want to open a saved file(yes/no)?")
##    LOAD = input()
##    if LOAD == 'yes' or LOAD == 'y':
##        for f in files:
##            print(f)
##        file = input('filename: ')
##        FileName = 'Files/Paint'+file+'.txt'
##        with open(FileName, 'r') as f:
##            for line in f:
##                a = line[0:4]
##                b = line[4:9]        #line[-9:-3]
##                if len(a) == 2:
##                    a = '0'+a
##                if len(a) == 1:
##                    a = '00'+a
##                inta = int(a)
##                intb = int(b)
##                coords = [inta, intb]
##                #print(coords)
##                dots.append(coords)
##        f.close()
    
    
# Window
SIZE = (900, 600)
TITLE = "Paint"
screen = pygame.display.set_mode(SIZE)
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

current_color = RED


# Brush
radius = 5;
SIZE1 = 1
SIZE2 = 2
SIZE3 = 3
SIZE4 = 4
SIZE5 = 5
SIZE6 = 6
SIZE7 = 7
SIZE8 = 8
SIZE9 = 9
SIZE = 5

# Palete Location
RED_BOX = (10, 560, 30, 30)
GREEN_BOX = (50, 560, 30, 30)
BLUE_BOX = (90, 560, 30, 30)



oldx = 0
oldy = 0
# Game loop
done = False
saving = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                SIZE = SIZE1
            if event.key == pygame.K_2:
                SIZE = SIZE2
            if event.key == pygame.K_3:
                SIZE = SIZE3
            if event.key == pygame.K_4:
                SIZE = SIZE4
            if event.key == pygame.K_5:
                SIZE = SIZE5
            if event.key == pygame.K_6:
                SIZE = SIZE6
            if event.key == pygame.K_7:
                SIZE = SIZE7
            if event.key == pygame.K_8:
                SIZE = SIZE8
            if event.key == pygame.K_9:
                SIZE = SIZE9
            if event.key == pygame.K_0:
                screen.fill(BLACK)
            if event.key == pygame.K_s:
                if not saving:
                    saving = True
            if event.key == pygame.K_e:
                SIZE=SIZE9
                current_color=BLACK
                #make black color, as well as erase cursor
                
        

    # Game logic
    if saving:
        name = ''
        name = input('input filename: ')
        time_string = str(time.asctime()[4:7]+\
                          time.asctime()[8:10]+\
                          time.asctime()[11:13]+\
                          time.asctime()[14:16]+\
                          time.asctime()[17:19])
        pygame.image.save(screen,
                          "Files//PAINT//"+\
                          time_string+\
                          "_"+name+\
                          ".jpeg")
        saving = not saving
        print('-----SAVED IMAGE-----')
        print(time_string+"_"+name+".jpeg")
        print('---------------------')
        
    clicks = pygame.mouse.get_pressed()

    if clicks[0]:
        
        click_pos = pygame.mouse.get_pos()
        x = click_pos[0]
        y = click_pos[1]
        if oldx != x or oldy != y:
            dots.append({'x': x, 'y': y, 'color': current_color})
        oldx = x
        oldy = y
        
##        dots.append({'x': x, 'y': y, 'color': current_color})
##                print('click!', x, y)
        
        if RED_BOX[0] < x < RED_BOX[0] + RED_BOX[2] and \
           RED_BOX[1] < y < RED_BOX[1] + RED_BOX[3]:
            current_color = RED
##                    print('Red')
        elif GREEN_BOX[0] < x < GREEN_BOX[0] + GREEN_BOX[2] and \
             GREEN_BOX[1] < y < GREEN_BOX[1] + GREEN_BOX[3]:
            current_color = GREEN
##                    print('Green')
        elif BLUE_BOX[0] < x < BLUE_BOX[0] + BLUE_BOX[2] and \
             BLUE_BOX[1] < y < BLUE_BOX[1] + BLUE_BOX[3]:
            current_color = BLUE
##                    print('Blue')
        else:
##                    print('draw')
            pygame.draw.circle(screen, current_color, [x, y], SIZE)
            

    ''' draw palette '''
    pygame.draw.rect(screen, RED, RED_BOX)
    pygame.draw.rect(screen, WHITE, RED_BOX, 2)
    pygame.draw.rect(screen, GREEN, GREEN_BOX)
    pygame.draw.rect(screen, WHITE, GREEN_BOX, 2)
    pygame.draw.rect(screen, BLUE, BLUE_BOX)
    pygame.draw.rect(screen, WHITE, BLUE_BOX, 2)
                     
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)


# Close window on quit
pygame.quit()


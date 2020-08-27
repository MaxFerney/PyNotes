import pygame
import os
import time
import webbrowser


pygame.init()

"""

################################################
add a list of shortcuts to the screen on startup
################################################


#file name input option?


webbrowser.open("filename")
    works perfectly.

#show list of files, then selecting a pens it

Allow name of file, since this is PyPaint, link it
    the PyNotes Main Program.

separate the folder which each file is saved by
    the current date(first 5 or so characters)

ascii to paint
    use ascii art to draw pixel and color at specific point.

needs to do text box.. badly

cursor = pygame.cursors.compile(pygame.cursors.textmarker_strings)
pygame.mouse.set_cursor(*cursor)

eliminated dot at text when reclicking

#######
IDEA!!!
Instead of putting screen blits into a list, just do it once
IDEA!!!
#######

compile(strings, black=’ ’, white=’.’,  or=’o’)


thickarrow_strings = (               #sized 24 24
  "                        ",
  "                        ",
  "                        ",
  "  .                     ",
  "  ..                    ",
  "  ...                   ",
  "  ....                  ",
  "  .....                 ",
  "  ......                ",
  "  .......               ",
  "  ........              ",
  "  ........              ",
  "  ......                ",
  "  .   ..                ",
  "       ..               ",
  "       ..               ",
  "       ..               ",
  "        ..              ",
  "        ..              ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ")


Eraser_strings = (               #sized 32x32
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "              ....              ",
    "            ........            ",
    "          ...XXXXXX...          ",
    "        ...XXXXXXXXXX...        ",
    "       ..XXXXXXXXXXXXXX..       ",
    "      ..XXXXXXXXXXXXXXXX..      ",
    "     ..XXXXXXXXXXXXXXXXXX..     ",
    "     ..XXXXXXXXXXXXXXXXXX..     ",
    "    ..XXXXXXXXXXXXXXXXXXXX..    ",
    "    ..XXXXXXXXXXXXXXXXXXXX..    ",
    "    ..XXXXXXXXXXXXXXXXXXXX..    ",
    "    ..XXXXXXXXXXXXXXXXXXXX..    ",
    "    ..XXXXXXXXXXXXXXXXXXXX..    ",
    "    ..XXXXXXXXXXXXXXXXXXXX..    ",
    "     ..XXXXXXXXXXXXXXXXXX..     ",
    "     ..XXXXXXXXXXXXXXXXXX..     ",
    "      ..XXXXXXXXXXXXXXXX..      ",
    "       ..XXXXXXXXXXXXXX..       ",
    "        ...XXXXXXXXXX...        ",
    "          ...XXXXXX...          ",
    "            ........            ",
    "              ....              ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ")

  
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
##        FileName = 'Files/Paint'+file+'.t t'
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


Eraser_strings = (               #sized 32x32
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "            ........            ",
    "          ...XXXXXX...          ",
    "        ...XXXXXXXXXX...        ",
    "       ..XXXXXXXXXXXXXX..       ",
    "      ..XXXXXXXXXXXXXXXX..      ",
    "     ..XXXXXXXXXXXXXXXXXX..     ",
    "     ..XXXXXXXXXXXXXXXXXX..     ",
    "    ..XXXXXXXXXXXXXXXXXXXX..    ",
    "    ..XXXXXXXXXXXXXXXXXXXX..    ",
    "    ..XXXXXXXXXXXXXXXXXXXX..    ",
    "    ..XXXXXXXXXXXXXXXXXXXX..    ",
    "    ..XXXXXXXXXXXXXXXXXXXX..    ",
    "    ..XXXXXXXXXXXXXXXXXXXX..    ",
    "     ..XXXXXXXXXXXXXXXXXX..     ",
    "     ..XXXXXXXXXXXXXXXXXX..     ",
    "      ..XXXXXXXXXXXXXXXX..      ",
    "       ..XXXXXXXXXXXXXX..       ",
    "        ...XXXXXXXXXX...        ",
    "          ...XXXXXX...          ",
    "            ........            ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ")

# Cursor
original_cursor = pygame.mouse.get_cursor()
cursor = pygame.cursors.compile(Eraser_strings)
##cursor_vars = ((32,32),(16,16),*cursor)
pygame.mouse.set_cursor((32,32),(16,16),*cursor)




# Palete Location
RED_BOX  = (10, 560, 30, 30)
GREEN_BOX  = (50, 560, 30, 30)
BLUE_BOX = (90, 560, 30, 30)

# Text Box
text_boxes=[]


# Game loop
done = False
saving = False

textbox = False
text_click=False

while not done:
##    cursor = pygame.cursors.compile(Eraser_strings)
##    pygame.mouse.set_cursor((32,32),(16,16),*cursor)
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
                #reset variables
                text_boxes=[]
                SIZE = SIZE5
                color = RED
                
            if event.key == pygame.K_s:
                if not saving:
                    saving = True
            if event.key == pygame.K_e:
                SIZE=SIZE9
                current_color=BLACK
                #make black color, as well as erase cursor
            if event.key == pygame.K_t:
                if not textbox and not text_click:
                    textbox = True
                
        

    # Game logic
    if saving:
##        name = ''
        name = input('input filename: ')
        
        #if day is single digit, change it to 0[digit]
        daystr=time.asctime()[8:10]
        if time.asctime()[8]==' ':
            daystr='0'+time.asctime()[9]
            
        time_string = str(time.asctime()[4:7]+\
                          daystr+\
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

    if not textbox:
        pygame.draw.rect(screen,BLACK,(130,560,30,30))
        
    if textbox:
        #change mouse?
        pygame.draw.rect(screen,WHITE,(130,560,30,30))
        print('\n\n\n\n\n')
        print('-----------')
        t_text = input('input text: ')
        print('click position')
        print('\n\n\n')
        text_click=True
        textbox=False
    
    clicks = pygame.mouse.get_pressed()
    if clicks[0]:
        
        click_pos = pygame.mouse.get_pos()
        x = click_pos[0]
        y = click_pos[1]

        #text click
        if text_click:
            #return mouse?
            tbox_pos=[x,y]
            tbox_col=current_color
            tbox_text=t_text
            #play with multiplier/additive
            tbox_size=(SIZE*5)+10
            
            text_boxes.append({'pos':tbox_pos,
                               'col':tbox_col,
                               'text':tbox_text,
                               'size':tbox_size})
            pygame.draw.rect(screen,WHITE,(x,y,2,2))
        text_click=text_click

        #still not erasing
        for tb in text_boxes:
            font=pygame.font.Font(None,tb['size'])
            text=font.render(tb['text'],True,tb['col'])
            screen.blit(text,tb['pos'])


        
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
            if not text_click:
                pygame.draw.circle(screen, current_color, [x, y], SIZE)
        #This prevents a dot from appearing when text click
        text_click=False

    ''' draw palette '''
    pygame.draw.rect(screen, RED, RED_BOX)
    pygame.draw.rect(screen, WHITE, RED_BOX, 2)
    pygame.draw.rect(screen, GREEN, GREEN_BOX)
    pygame.draw.rect(screen, WHITE, GREEN_BOX, 2)
    pygame.draw.rect(screen, BLUE, BLUE_BOX)
    pygame.draw.rect(screen, WHITE, BLUE_BOX, 2)

##    for tb in text_boxes:
##        font=pygame.font.Font(None,tb['size'])
##        text=font.render(tb['text'],True,tb['col'])
##        screen.blit(text,tb['pos'])
                     
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)


# Close window on quit
pygame.quit()


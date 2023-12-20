import random
import Rect
import Bombs
import pygame
pygame.init()
win = pygame.display.set_mode((620, 350))
pygame.display.set_caption("Saper")
run = True
font = pygame.font.Font(None, 36)
black = (0,0,0)
colors = {'1':(0,128,255),'2':(0,153,76),'3':(255,0,0),'4':(102,0,204),'5':(255,153,51),'6':black,'7': black,'8':black}
KOLOR = (160, 160, 160)
x = 10
y = 10
szer = 25
wys = 25
list_of_squares = []
map_of_game = []
for i in range(11):
    temp = []
    for j in range(20):
        losowy = random.randint(0, 10)
        if losowy < 2:
            sqr = Rect.Pole(win, KOLOR, j, i, x + j * 30, y + i * 30, szer, wys, False)
            temp.append('*')
        else:
            sqr = Rect.Pole(win, KOLOR, j, i, x + j * 30, y + i * 30, szer, wys, True)
            temp.append('0')
        list_of_squares.append(sqr)
    map_of_game.append(temp)
for l in map_of_game:
    print(l)
map_of_bombs = Bombs.ReplaceFields(map_of_game)
map_of_bombs.update()
updated_map = map_of_bombs.get_dane()
print()
print()
for k in updated_map:
    print(k)

licz = 0
for h in range(0,len(map_of_game)):
    for t in range(0,len(map_of_game[0])):
        if updated_map[h][t] != '*':
            list_of_squares[licz].bombs_nearby = updated_map[h][t]
        licz += 1


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for square in list_of_squares:
                if (
                        square.pos_x <= mouse_x <= square.pos_x + square.width
                        and square.pos_y <= mouse_y <= square.pos_y + square.length
                        and square.checking == -1
                ):
                    square.discovered = True
                    if square.free:
                        square.color = (224,224,224)
                        if square.bombs_nearby == '0':
                            free_fields = map_of_bombs.scan(square.in_y,square.in_x)
                            full_scan = map_of_bombs.full_scan(free_fields)
                            for square_2 in full_scan:
                                for evr in list_of_squares:
                                    if square_2[0] == evr.in_y and square_2[1] == evr.in_x:
                                        evr.color = (224,224,224)
                                        evr.discovered = True
                    else:
                        for single_square in list_of_squares:
                            if not single_square.free:
                                single_square.color = (255,0,0)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for square in list_of_squares:
                if (
                        square.pos_x <= mouse_x <= square.pos_x + square.width
                        and square.pos_y <= mouse_y <= square.pos_y + square.length
                ):
                    if not square.discovered:
                        if square.checking == -1:
                            square.color = (255,255,0)
                            square.checking *= -1
                        else:
                            square.color = KOLOR
                            square.checking *= -1

    for el in list_of_squares:
        pygame.draw.rect(el.screen, el.color, (el.pos_x, el.pos_y, el.width, el.length))
        if el.discovered:
            if el.bombs_nearby != '-1' and el.bombs_nearby != '0':
                text_surface = font.render(el.bombs_nearby, True, colors[el.bombs_nearby])
                text_rect = text_surface.get_rect(topleft=(el.pos_x+5,el.pos_y))
                win.blit(text_surface, text_rect)
    pygame.display.update()
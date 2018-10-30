import pygame, sys, math, numpy

RED = (255,0,0)
GREEN = (0,200,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BLACK = (0,0,0)

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    if col >= COLUMN_COUNT and col <= 0:
        return 0
    return board[ROW_COUNT - 1][col] == 0

def get_next_pos(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(numpy.flip(board, 0))

def win(board, piece):
    #check horizontally
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] == piece:
                return True
    
    #check vetically
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c] == piece:
                return True

    #check diagonally
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3] == piece:
                return True

    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3] == piece:
                return True

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, ((c+1)*SQSIZE, (r+1)*SQSIZE, SQSIZE, SQSIZE))
            pygame.draw.circle(screen, BLACK, (int((c+1)*SQSIZE + SQSIZE/2), int((r+1)*SQSIZE + SQSIZE/2)), RADIUS)
            
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int((c+1)*SQSIZE + SQSIZE/2), height-int((r+1)*SQSIZE + SQSIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int((c+1)*SQSIZE + SQSIZE/2), height-int((r+1)*SQSIZE + SQSIZE/2)), RADIUS)
                
    pygame.display.update()
        

board = create_board()
game_over = False
turn = 0
 
pygame.init()

SQSIZE = 100
RADIUS = int(SQSIZE/2 - 5)

width = (COLUMN_COUNT+2) * SQSIZE
height = (ROW_COUNT+2) * SQSIZE

size = (width, height)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

font = pygame.font.SysFont("monospace", 75)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            quit()
        if turn ==43:
            tie=font.render("Tie",1,RED)
            screen.blit(tie,(100,10))
            game_over=True

        
        if event.type == pygame.MOUSEMOTION:
            if 700 >= event.pos[1] >= 100 and 100 <= event.pos[1] <= 800:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQSIZE))#
                posx = event.pos[0]
                if turn % 2== 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQSIZE/2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQSIZE/2)), RADIUS)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQSIZE))
            if 100 <= event.pos[1] <= 700 and 100 <= event.pos[0] <= 800:
                if turn % 2 == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQSIZE)) - 1

                    if is_valid_location(board, col):
                        row = get_next_pos(board, col)
                        drop_piece(board, row, col, 1)
                        turn += 1

                        if win(board, 1):
                            label = font.render("Player 1 Wins!!", 1, RED)
                            screen.blit(label, (100, 10))
                            game_over = True

                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQSIZE)) - 1

                    if is_valid_location(board, col):
                        row = get_next_pos(board, col)
                        drop_piece(board, row, col, 2)
                        turn += 1

                        if win(board, 2):
                            label = font.render("Player 2 Wins!!", 1, YELLOW)
                            screen.blit(label, (100, 10))
                            game_over = True
                            
            #print_board(board)
            draw_board(board)

            if game_over:
                pygame.time.wait(2000)

pygame.quit()
sys.exit()
quit()

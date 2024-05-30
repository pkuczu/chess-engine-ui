import pygame as p
import chessengine

WIDTH = HEIGHT = 512


DIMENSION = 8 # dimensions of chess board is 8x8

SQ_SIZE = 512 // DIMENSION

IMAGES = {}

def loadImages():
    IMAGES['P'] = p.transform.scale(p.image.load("images/w_pawn.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['p'] = p.transform.scale(p.image.load("images/b_pawn.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['K'] = p.transform.scale(p.image.load("images/w_king.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['k'] = p.transform.scale(p.image.load("images/b_king.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['N'] = p.transform.scale(p.image.load("images/w_knight.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['n'] = p.transform.scale(p.image.load("images/b_knight.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['Q'] = p.transform.scale(p.image.load("images/w_queen.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['q'] = p.transform.scale(p.image.load("images/b_queen.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['B'] = p.transform.scale(p.image.load("images/w_bishop.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['b'] = p.transform.scale(p.image.load("images/b_bishop.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['R'] = p.transform.scale(p.image.load("images/w_rook.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['r'] = p.transform.scale(p.image.load("images/b_rook.png"), (SQ_SIZE, SQ_SIZE))
def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]

    for row in range(DIMENSION):
        for col in range(DIMENSION):
            
            p.draw.rect(screen, colors[(row + col) % 2], p.Rect(col*SQ_SIZE, row *SQ_SIZE,SQ_SIZE, SQ_SIZE))
def drawPieces(screen, board):
    colors = [p.Color("white"), p.Color("gray")]

    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != " ":
                screen.blit(IMAGES[piece], p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chessengine.GameState()
    print(gs.board)
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick()
        p.display.flip()

main()



import pygame

# making the surface

WIDTH,HEIGHT =900,500;
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("game one")

WHITE =(255,255,255)

def main():
    
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
                WIN.fill((255,255,255))
                pygame.quit()
                
                if __name__ == '__main__':
                    main()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        WIN.fill((255,255,255))
        pygame.display.update()
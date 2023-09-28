import pygame

# making the surface

WIDTH,HEIGHT =900,500;
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("game one")

WHITE =(255,255,255)
#  changes background color
def draw_window():
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP_IMAGE,(300,100))
    pygame.display.update()


FPS = 60

SPACESHIP_WIDTH,SPACESHIP_HEIGHT =55,40

# add some image later 
YELLOW_SPACESHIP_IMAGE =pygame.image.load(os.path.join())

YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(55,40))
RED_SPACESHIP = pygame.image.load(os.path.join())
YELLOW_SPACESHIP_IMAGE =pygame.image.load(os.path.join())
YELLOW_SPACESHIP_IMAGE =pygame.image.load(os.path.join())
def main():
    clock = pygame.time.Clock()
    run = True
    
    while run:
        
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
                WIN.fill((255,255,255))
                pygame.display.update()
                pygame.quit()
                
                if __name__ == '__main__':
                    main()
                
                # unfortunately this code is not used. for now.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        WIN.fill((255,255,255))
        pygame.display.update()
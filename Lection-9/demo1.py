import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
DARKGREEN = (10, 50, 10)

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Demo app")

# display_surface.fill(BLUE)

# pygame.draw.line(display_surface, WHITE, (0, 0), (100, 100), 4)
# pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 100, 4)
# pygame.draw.circle(display_surface, RED, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 50, 0)
# pygame.draw.rect(display_surface, MAGENTA, (300, 100, 200, 200), 3)
# pygame.draw.rect(display_surface, CYAN, (400, 10, 200, 200), 0)

# dragon_image_left = pygame.image.load('dragon_left.png')
# dragon_rect_left = dragon_image_left.get_rect()
# dragon_rect_left.topleft = (0, 0)

# dragon_image_right = pygame.image.load('dragon_right.png')
# dragon_rect_right = dragon_image_right.get_rect()
# dragon_rect_right.topright = (WINDOW_WIDTH, 0)

# pygame.draw.line(display_surface, WHITE, (0, 75), (WINDOW_WIDTH, 75), 6)

sound1 = pygame.mixer.Sound('sound_1.wav')
sound1.play()

pygame.time.delay(5000)

sound2 = pygame.mixer.Sound('sound_2.wav')
sound2.play()

pygame.time.delay(5000)
sound2.set_volume(0.2)
sound2.play()

pygame.time.delay(5000)
pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1, 0.0)
sound2.play()


running = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

    # display_surface.blit(dragon_image_left, dragon_rect_left)
    # display_surface.blit(dragon_image_right, dragon_rect_right)

    pygame.display.update()

pygame.quit()
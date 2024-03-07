import pygame
import spritesheet
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheet animations')

sprite_sheet_image = pygame.image.load('character_assets/sheets/doux.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BG = pygame.transform.scale(pygame.image.load('back.png').convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
BLACK = (0, 0, 0)

# Create animation list
animation_list = []
animation_steps = [4, 6, 3, 4]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 75
frame = 0
step_counter = 0

# For loop to loop through the animations
for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 24, 24, 2, BLACK))
        step_counter += 1
    animation_list.append(temp_img_list)

run = True
while run:
    # Fills the screen with the background color we gave
    screen.blit(BG, (0, 0))

    # Update the idle animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    # Show frame image
    screen.blit(animation_list[action][frame], (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and action > 0:
                action -= 6
                frame = 0
            if event.key == pygame.K_UP and action < len(animation_list) - 1:
                animation_list[5][5]
                action += 1
                frame = 0

            
    pygame.display.update()

pygame.quit()
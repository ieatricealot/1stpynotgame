import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('F1 con Sandreke')
clock = pygame.time.Clock()

# 1. Load the image
# Pro-tip: Ensure 'neil-the-seal.png' is in the same folder as this .py file!
carImg = pygame.image.load('neil-the-seal.png')

# 2. Define Neil's starting position (x, y)
# 0,0 is the top-left corner. Let's put him in the middle.
neil_x = 0
neil_y = 0

# Get the original width and height
width = carImg.get_width()
height = carImg.get_height()

# Scale down to 50% of the original size
new_size = (int(width * 0.5), int(height * 0.5))
carImg = pygame.transform.scale(carImg, new_size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. Wipe the screen (Purple track)
    screen.fill("purple")

    # 4. Draw Neil at his coordinates
    screen.blit(carImg, (neil_x, neil_y))

    # 5. Refresh the screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
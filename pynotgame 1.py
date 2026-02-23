import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Neil thing')
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
new_size = (int(width * 0.1), int(height * 0.1))
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

    keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

    if keys[pygame.K_LEFT]: # We can check if a key is pressed like this
        neil_x -= 5

    if keys[pygame.K_RIGHT]:
        neil_x += 5

    if keys[pygame.K_UP]:
        neil_y -= 5

    if keys[pygame.K_DOWN]:
        neil_y += 5
    # 5. Refresh the screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
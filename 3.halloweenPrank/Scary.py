import pygame
from time import sleep

# Initialize Pygame modules
pygame.init()

# Set up the window in fullscreen mode
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Initialize the mixer module for playing music
pygame.mixer.init()

# Load and play the first audio file ('ratsasan.mp3')
pygame.mixer.music.load('ratsasan.mp3')
pygame.mixer.music.play()

# Wait for 5 seconds while the first audio is playing
sleep(5)

# Load and play the second audio file ('scary.mp3')
pygame.mixer.music.load('scary.mp3')
pygame.mixer.music.play()

# Wait for 1 second after playing the second audio
sleep(1)

# Load the image ('scr.jpg') and display it on the window
image = pygame.image.load('scr.jpg')
window.blit(image, (0, 0))
pygame.display.update()  # Update the display to show the image

# Wait for 3 seconds to display the image before closing
sleep(3)

# Properly quit Pygame modules
pygame.quit()

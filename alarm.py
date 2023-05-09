import pygame
import time

pygame.init()

# Set the frequency and size of the sound buffer
pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)

# Load the sound file
alarm_sound = pygame.mixer.Sound("bleep-41488.mp3")

# Set the duration of the alarm in seconds
duration = 10

# Play the sound
alarm_sound.play()

# Wait for the sound to finish playing
time.sleep(duration)

# Stop the sound
alarm_sound.stop()

# Quit pygame
pygame.quit()

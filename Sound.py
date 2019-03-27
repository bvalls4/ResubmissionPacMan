import pygame


class Sound(object):
    channel = pygame.mixer.Channel(2)
    opening = pygame.mixer.Sound("music/PAC-MAN Namco Sounds - Start Music.wav")
    pickUp_small = pygame.mixer.Sound("music/Pacman Waka Waka - Sound Effect [Free Ringtone Download].wav")
    pickUp_large = pygame.mixer.Sound("music/Pac Man Power Sound FX.wav")
    eatGhost = pygame.mixer.Sound("music/Roblox Death Sound - OOF Sound Effect.wav")
    death = pygame.mixer.Sound("music/Pac Man Death Sound FX.wav")
    lose = pygame.mixer.Sound("music/Game Over sound effect.wav")
    win = pygame.mixer.Sound("music/Video Game Level Win Clear Sound Effect.wav")

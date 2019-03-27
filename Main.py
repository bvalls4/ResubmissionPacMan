# Set up pygame and modules
import pygame
from pygame.locals import *

pygame.init()

from Constants import *

# Create window
wSurface = pygame.display.set_mode(WINDOWSIZE, 0, 32)
pygame.display.set_caption("Pacman")

from Pacman import Pacman
from Ghost import Ghost
from Walls import Walls
from Pellets import Pellets
from Sound import Sound
from text import Text

# Create game objects
background = pygame.image.load("bg.png").convert()
pacman = Pacman()
ghosts = [Ghost()]
walls = Walls.createList(Walls())
pellets_small = Pellets.createListSmall(Pellets())
pellets_large = Pellets.createListLarge(Pellets())
clock = pygame.time.Clock()
pygame.mixer.music.load("music/Pac Man Ghost Noises.wav")
pygame.mixer.music.set_volume(0.5)

# Opening screen and music
Sound.channel.play(Sound.opening)
wSurface.fill((0, 0, 0))
wSurface.blit(background, (100, 0))
wSurface.blit(pacman.getScoreSurface(), (10, 10))
wSurface.blit(pacman.getLivesSurface(), (WINDOWSIZE[0] - 200, 10))

for p in pellets_small:
    wSurface.blit(Pellets.images[0], (p[0] + Pellets.shifts[0][0], p[1] + Pellets.shifts[0][1]))
for p in pellets_large:
    wSurface.blit(Pellets.images[1], (p[0] + Pellets.shifts[1][0], p[1] + Pellets.shifts[1][1]))
for g in ghosts:
    wSurface.blit(g.orange, g.orange_rect)
    wSurface.blit(g.cyan, g.cyan_rect)
    wSurface.blit(g.pink, g.pink_rect)
    wSurface.blit(g.red, g.red_rect)
wSurface.blit(pacman.surface, pacman.rect)
pygame.display.update()
while True:
    if not pygame.mixer.get_busy():
        break


def main(self):
    count = 0
    self.create_audio()
    self.start_menu_init()
    while True:
        # Main Screen Menu
        if self.mainScreen:
            count += 1
            self.screen.blit(self.background, (0, 0))
            self.titleText.draw(self.screen)
            self.titleText1.draw(self.screen)
            self.titleText2.draw(self.screen)

            if count <= 700:
                self.start_menu_chase()
            elif count <= 1500:
                self.intro_animation()
            else:
                self.start_menu_init()
                count = 0

            pygame.display.update()
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    exit()
                if pygame.key.get_pressed()[pygame.K_h]:
                    print('Accessing high scores...')
                    self.screen.blit(self.background, (0, 0))
                    scores = []
                    x = 0
                    with open('highscores.txt') as f:
                        for line in f:
                            name, score = line.split(',')
                            score = int(score)
                            scores.append((name, score))
                    scores = sorted(scores, reverse=True)[:10]
                    for name, score in scores:
                        if name == 'You':
                            Text("font/ARCADE_R.TTF", 15, name + ': ' + str(score), WHITE, 195, 230 + (35 * x)).draw(
                                self.screen)
                        else:
                            Text("font/ARCADE_R.TTF", 15, name + ': ' + str(score), YELLOW, 195, 230 + (35 * x)).draw(
                                self.screen)
                            pygame.display.update()
                            x += 1
                        self.mainScreen = False
                        self.highScore = True
                    if pygame.key.get_pressed()[pygame.K_p]:
                        self.mainScreen = False
                        self.startGame = True
                        self.reset()
                        print('Starting game...')
                        self.draw_chars(scores)
                        self.draw_map(scores)
                        self.draw_pellets(scores)

                        self.set_position()
                        # self.player = Player(self.screen, self.position.x, self.position.y - 15)
                        # self.player_group.add(self.player)

            # High Score Menu
        elif self.highScore:
            self.hsText.draw(self.screen)
            self.hsText1.draw(self.screen)
            pygame.display.update()
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    exit()
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    print('Returning to Main menu...')
                    self.mainScreen = True
                    self.highScore = False
                if pygame.key.get_pressed()[pygame.K_p]:
                    print('Starting game...')
                    self.highScore = False
                    self.startGame = True


# Game loop
keepGoing_game = True
while keepGoing_game:
    # Round loop
    keepGoing_round = True
    pygame.mixer.music.play(-1, 0.0)
    while keepGoing_round:
        clock.tick(FPS)

        # Event handling
        for event in pygame.event.get():
            # Quitting
            if event.type == QUIT:
                keepGoing_game = keepGoing_round = False

            # Arrow key down
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    pacman.moveUp = True
                    pacman.moveLeft = pacman.moveDown = pacman.moveRight = False
                    pacman.direction = 0
                elif event.key == K_LEFT:
                    pacman.moveLeft = True
                    pacman.moveUp = pacman.moveDown = pacman.moveRight = False
                    pacman.direction = 1
                elif event.key == K_DOWN:
                    pacman.moveDown = True
                    pacman.moveUp = pacman.moveLeft = pacman.moveRight = False
                    pacman.direction = 2
                elif event.key == K_RIGHT:
                    pacman.moveRight = True
                    pacman.moveUp = pacman.moveLeft = pacman.moveDown = False
                    pacman.direction = 3

            # Arrow key up
            elif event.type == KEYUP:
                pacman.moveUp = pacman.moveLeft = pacman.moveDown = pacman.moveRight = False

        # Move pacman rectangle
        pacman.move(walls)

        # Check if pacman must teleport to the other side
        pacman.teleport()

        # Animate and rotate pacman sprite
        pacman.getSurface()

        # Check if pacman has eaten any pellets and delete them
        Pellets.check(Pellets(), pellets_small, pellets_large, pacman, ghosts)

        # Add a new ghost if necessary
        """Ghost.add(Ghost(), ghosts)"""

        # Check if blue ghosts must return to normal
        for g in ghosts:
            if g.isBlue:
                g.checkBlue()

        # Move ghosts
        for g in ghosts:
            g.ghostmove(walls, pacman)

        # Draw screen
        wSurface.fill((0, 0, 0))
        wSurface.blit(background, (100, 0))
        wSurface.blit(pacman.getScoreSurface(), (10, 10))
        wSurface.blit(pacman.getLivesSurface(), (WINDOWSIZE[0] - 200, 10))
        for p in pellets_small:
            wSurface.blit(Pellets.images[0], (p[0] + Pellets.shifts[0][0], p[1] + Pellets.shifts[0][1]))
        for p in pellets_large:
            wSurface.blit(Pellets.images[1], (p[0] + Pellets.shifts[1][0], p[1] + Pellets.shifts[1][1]))
        for g in ghosts:
            wSurface.blit(g.orange, g.orange_rect)
            wSurface.blit(g.cyan, g.cyan_rect)
            wSurface.blit(g.pink, g.pink_rect)
            wSurface.blit(g.red, g.red_rect)
        wSurface.blit(pacman.surface, pacman.rect)
        pygame.display.update()

        # Check if pacman collided with a ghost
        for g in ghosts[:]:
            if pacman.rect.colliderect(g.orange_rect):
                if not g.isBlue:
                    keepGoing_round = False
                    pacman.lives -= 1
                    if pacman.lives == 0:
                        keepGoing_game = False
                    else:
                        Sound.channel.play(Sound.death)
                    break
                else:  # Ghost is blue
                    del ghosts[ghosts.index(g)]
                    pacman.score += 100
                    Sound.channel.play(Sound.eatGhost)

            elif pacman.rect.colliderect(g.cyan_rect):
                if not g.isBlue:
                    keepGoing_round = False
                    pacman.lives -= 1
                    if pacman.lives == 0:
                        keepGoing_game = False
                    else:
                        Sound.channel.play(Sound.death)
                    break
                else:  # Ghost is blue
                    del ghosts[ghosts.index(g)]
                    pacman.score += 100
                    Sound.channel.play(Sound.eatGhost)

            elif pacman.rect.colliderect(g.pink_rect):
                if not g.isBlue:
                    keepGoing_round = False
                    pacman.lives -= 1
                    if pacman.lives == 0:
                        keepGoing_game = False
                    else:
                        Sound.channel.play(Sound.death)
                    break
                else:  # Ghost is blue
                    del ghosts[ghosts.index(g)]
                    pacman.score += 100
                    Sound.channel.play(Sound.eatGhost)

            elif pacman.rect.colliderect(g.red_rect):
                if not g.isBlue:
                    keepGoing_round = False
                    pacman.lives -= 1
                    if pacman.lives == 0:
                        keepGoing_game = False
                    else:
                        Sound.channel.play(Sound.death)
                    break
                else:  # Ghost is blue
                    del ghosts[ghosts.index(g)]
                    pacman.score += 100
                    Sound.channel.play(Sound.eatGhost)

        # Check if pacman has eaten all the pellets
        else:
            if len(pellets_small) == 0 and len(pellets_large) == 0:
                keepGoing_game = keepGoing_round = False

    # Reset round
    pygame.mixer.music.stop()
    pacman.reset()
    for g in ghosts:
        g.reset()
    while True:
        if not pygame.mixer.get_busy():
            break

# End of game screen
wSurface.fill((0, 0, 0))
surface_temp = None

if pacman.lives == 0:  # Player loses
    Sound.channel.play(Sound.lose)
    surface_temp = pacman.getLosingSurface()

elif len(pellets_small) == 0 and len(pellets_large) == 0:  # Player wins
    Sound.channel.play(Sound.win)
    surface_temp = pacman.getWinningSurface()

if surface_temp is not None:  # Player loses or wins (does not quit)
    rect_temp = surface_temp.get_rect()
    rect_temp.center = wSurface.get_rect().center
    wSurface.blit(surface_temp, rect_temp)
    pygame.display.update()

while True:
    if not pygame.mixer.get_busy():
        pygame.quit()
        break

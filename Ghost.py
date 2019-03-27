import copy

import pygame

from Character import Character

from Constants import *


class Ghost(Character):
    images = [pygame.image.load("images/Four Legged Orange Left.png").convert(),
              pygame.image.load("images/Blue Four Legs.png").convert(),
              pygame.image.load("images/Four Legged Cyan Down.png").convert(),
              pygame.image.load("images/Four Legged Pink Up.png").convert(),
              pygame.image.load("images/Four Legged Red Right.png").convert()]
    for i in range(len(images)):
        images[i].set_colorkey((0, 0, 0))
    ISBLUE_TIME = int(10 * FPS)
    ADD_TIME = int(30 * FPS)
    add_time = ADD_TIME

    def __init__(self):
        """in - (self)"""
        super().__init__()
        self.orange = Ghost.images[0]
        self.cyan = Ghost.images[2]
        self.pink = Ghost.images[3]
        self.red = Ghost.images[4]
        self.cyan_rect = self.cyan.get_rect()
        self.orange_rect = self.orange.get_rect()
        self.pink_rect = self.pink.get_rect()
        self.red_rect = self.red.get_rect()
        self.cyan_rect.left = 315
        self.cyan_rect.top = 275
        self.orange_rect.left = 325
        self.orange_rect.top = 275
        self.pink_rect.left = 305
        self.pink_rect.top = 275
        self.red_rect.left = 335
        self.red_rect.top = 275
        self.speed = 1
        self.course = [0] * 50
        self.isBlue = False
        self.isBlue_time = 0

    def makeBlue(self):
        """in - (self)
        Changes ghost into a blue ghost."""
        self.isBlue = True
        self.isBlue_time = Ghost.ISBLUE_TIME  # number of frames
        self.cyan = Ghost.images[1]
        self.pink = Ghost.images[1]
        self.orange = Ghost.images[1]
        self.red = Ghost.images[1]
        self.course = []

    def makeNotBlue(self):
        """in - (self)
        Changes blue ghost into a regular ghost."""
        self.orange = Ghost.images[0]
        self.cyan = Ghost.images[2]
        self.pink = Ghost.images[3]
        self.red = Ghost.images[4]
        self.course = []
        self.isBlue = False
        self.isBlue_time = 0

    def checkBlue(self):
        """in - (self)
        Checks if the ghost should return to normal, and does if necessary."""
        self.isBlue_time -= 1
        if self.isBlue_time <= 0:
            self.makeNotBlue()

    def reset(self):
        """in - (self)
        Resets ghost's position and makes it regular (not blue)."""
        self.makeNotBlue()
        self.cyan_rect.left = 315
        self.cyan_rect.top = 275
        self.orange_rect.left = 325
        self.orange_rect.top = 275
        self.pink_rect.left = 305
        self.pink_rect.top = 275
        self.red_rect.left = 335
        self.red_rect.top = 275
        self.course = [0] * 50

    def canMove_distance(self, direction, walls):
        """in - (self, direction, list of walls)
        Determines the number of steps the ghost can take in the specified direction.
        out - int"""
        test = copy.deepcopy(self)
        counter = 0
        while True:
            if not Character.canGhostMove(test, direction, walls):
                break
            Character.otherMove(test, direction)
            counter += 1
        return counter

    def ghostmove(self, walls, pacman):
        """in - (self, list of walls, pacman)
        Uses AI to move ghost towards pacman."""
        if len(self.course) > 0:
            if self.canGhostMove(self.course[0], walls) or self.orange_rect.colliderect(
                    pygame.Rect((268, 248), (112, 64))) or self.cyan_rect.colliderect(
                    pygame.Rect((268, 248), (112, 64))) or self.pink_rect.colliderect(
                    pygame.Rect((268, 248), (112, 64))) or self.red_rect.colliderect(
                    pygame.Rect((268, 248), (112, 64))):
                Character.otherMove(self, self.course[0])
                del self.course[0]
            else:
                self.course = []

        else:
            xDistance = pacman.rect.left - self.cyan_rect.left
            yDistance = pacman.rect.top - self.cyan_rect.top
            choices = [-1, -1, -1, -1]

            if abs(xDistance) > abs(yDistance):  # horizontal 1st
                if xDistance > 0:  # right 1st
                    choices[0] = 3
                    choices[3] = 1
                elif xDistance < 0:  # left 1st
                    choices[0] = 1
                    choices[3] = 3

                if yDistance > 0:  # down 2nd
                    choices[1] = 2
                    choices[2] = 0
                elif yDistance < 0:  # up 2nd
                    choices[1] = 0
                    choices[2] = 2
                else:  # yDistance == 0
                    if self.canMove_distance(2, walls) < self.canMove_distance(0, walls):  # down 2nd
                        choices[1] = 2
                        choices[2] = 0
                    elif self.canMove_distance(0, walls) < self.canMove_distance(2, walls):  # up 2nd
                        choices[1] = 0
                        choices[2] = 2

            elif abs(yDistance) >= abs(xDistance):  # vertical 1st
                if yDistance > 0:  # down 1st
                    choices[0] = 2
                    choices[3] = 0
                elif yDistance < 0:  # up 1st
                    choices[0] = 0
                    choices[3] = 2

                if xDistance > 0:  # right 2nd
                    choices[1] = 3
                    choices[2] = 1
                elif xDistance < 0:  # left 2nd
                    choices[1] = 1
                    choices[2] = 3
                else:  # xDistance == 0
                    if self.canMove_distance(3, walls) < self.canMove_distance(1, walls):  # right 2nd
                        choices[1] = 3
                        choices[2] = 1
                    elif self.canMove_distance(1, walls) < self.canMove_distance(3, walls):  # left 2nd
                        choices[1] = 1
                        choices[2] = 3

            if self.isBlue:
                choices.reverse()
            choices_original = choices[:]
            for i, x in enumerate(choices[:]):
                if x == -1 or (not Character.canGhostMove(self, x, walls)):
                    del choices[choices.index(x)]

            if len(choices) > 0:
                Character.move(self, choices[0])
                if choices_original.index(choices[0]) >= 2:  # if move is 3rd or 4th choice
                    global FPS
                    for i in range(int(FPS * 1.5)):
                        self.course.append(choices[0])

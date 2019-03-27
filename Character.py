class Character(object):
    def __init__(self):
        """in - (self)"""
        self.surface = None
        self.rect = None
        self.speed = None
        self.cyan_rect = None
        self.orange_rect = None
        self.pink_rect = None
        self.red_rect = None
        self.orange = None
        self.cyan = None
        self.pink = None
        self.red = None

    def canMove(self, direction, walls):
        """in - (self, direction, list of walls)
        Determines if character can move without colliding with any of the walls.
        out - bool"""
        global rectTest
        if direction == 0:
            rectTest = self.rect.move((0, -self.speed))

        elif direction == 1:
            rectTest = self.rect.move((-self.speed, 0))

        elif direction == 2:
            rectTest = self.rect.move((0, self.speed))

        elif direction == 3:
            rectTest = self.rect.move((self.speed, 0))

        for wall in walls:
            if wall.colliderect(rectTest):
                return False
        return True

    def canGhostMove(self, direction, walls):
        global rectTest
        if direction == 0:
            rectTest = self.cyan_rect.move((0, -self.speed))
            rectTest = self.orange_rect.move((0, -self.speed))
            rectTest = self.red_rect.move((0, -self.speed))
            rectTest = self.pink_rect.move((0, -self.speed))

        if direction == 1:
            rectTest = self.cyan_rect.move((-self.speed, 0))
            rectTest = self.orange_rect.move((-self.speed, 0))
            rectTest = self.pink_rect.move((-self.speed, 0))
            rectTest = self.red_rect.move((-self.speed, 0))

        if direction == 2:
            rectTest = self.cyan_rect.move((0, self.speed))
            rectTest = self.orange_rect.move((0, self.speed))
            rectTest = self.pink_rect.move((0, self.speed))
            rectTest = self.red_rect.move((0, self.speed))

        if direction == 3:
            rectTest = self.cyan_rect.move((self.speed, 0))
            rectTest = self.orange_rect.move((self.speed, 0))
            rectTest = self.pink_rect.move((self.speed, 0))
            rectTest = self.red_rect.move((self.speed, 0))

        for wall in walls:
            if wall.colliderect(rectTest):
                return False
        return True

    def move(self, direction):
        """in - (self, direction (0-3))
        Moves character in specified direction."""
        if direction == 0:
            self.rect.top -= self.speed

        elif direction == 1:
            self.rect.left -= self.speed

        elif direction == 2:
            self.rect.top += self.speed

        elif direction == 3:
            self.rect.left += self.speed

    def otherMove(self, direction):
        if direction == 0:
            self.orange_rect.top -= self.speed
            self.cyan_rect.top -= self.speed
            self.pink_rect.top -= self.speed
            self.red_rect.top -= self.speed
        elif direction == 1:
            self.orange_rect.left -= self.speed
            self.cyan_rect.left -= self.speed
            self.pink_rect.left -= self.speed
            self.red_rect.left -= self.speed
        elif direction == 2:
            self.orange_rect.top += self.speed
            self.cyan_rect.top += self.speed
            self.pink_rect.top += self.speed
            self.red_rect.top += self.speed
        elif direction == 3:
            self.orange_rect.left += self.speed
            self.cyan_rect.left += self.speed
            self.pink_rect.left += self.speed
            self.red_rect.left += self.speed

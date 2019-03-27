import pygame


class Walls(object):
    def createList(self):
        """in - (self)
        Creates a list of wall Rect objects.
        out - list"""
        walls = [pygame.Rect((100, 48), (448, 8)), pygame.Rect((100, 55), (7, 152)), pygame.Rect((180, 200), (8, 64)),
                 pygame.Rect((268, 248), (8, 64)), pygame.Rect((140, 88), (48, 32)), pygame.Rect((220, 88), (64, 32)),
                 pygame.Rect((364, 88), (65, 32)), pygame.Rect((460, 88), (49, 32)), pygame.Rect((100, 200), (86, 8)),
                 pygame.Rect((140, 152), (48, 16)), pygame.Rect((316, 55), (16, 65)), pygame.Rect((540, 55), (8, 153)),
                 pygame.Rect((460, 200), (88, 8)), pygame.Rect((460, 152), (49, 16)),
                 pygame.Rect((412, 152), (16, 112)), pygame.Rect((364, 200), (50, 16)),
                 pygame.Rect((268, 152), (112, 16)), pygame.Rect((316, 166), (16, 50)),
                 pygame.Rect((220, 152), (16, 112)), pygame.Rect((235, 200), (49, 16)),
                 pygame.Rect((100, 256), (88, 8)), pygame.Rect((460, 256), (89, 8)), pygame.Rect((460, 296), (89, 8)),
                 pygame.Rect((460, 352), (88, 8)), pygame.Rect((460, 296), (9, 64)), pygame.Rect((412, 296), (17, 65)),
                 pygame.Rect((220, 296), (16, 64)), pygame.Rect((460, 200), (8, 64)), pygame.Rect((100, 296), (88, 8)),
                 pygame.Rect((179, 296), (9, 64)), pygame.Rect((100, 352), (88, 8)), pygame.Rect((100, 352), (8, 193)),
                 pygame.Rect((107, 440), (33, 16)), pygame.Rect((100, 536), (448, 9)),
                 pygame.Rect((540, 352), (8, 193)), pygame.Rect((508, 440), (34, 16)), pygame.Rect((268, 248), (40, 8)),
                 pygame.Rect((340, 248), (41, 8)), pygame.Rect((460, 200), (9, 64)), pygame.Rect((139, 392), (49, 17)),
                 pygame.Rect((171, 406), (17, 51)), pygame.Rect((220, 392), (64, 17)),
                 pygame.Rect((364, 392), (65, 17)), pygame.Rect((460, 392), (49, 17)),
                 pygame.Rect((460, 406), (17, 51)), pygame.Rect((412, 440), (17, 50)),
                 pygame.Rect((364, 488), (145, 17)), pygame.Rect((267, 440), (114, 17)),
                 pygame.Rect((316, 358), (16, 51)), pygame.Rect((220, 440), (16, 50)),
                 pygame.Rect((139, 488), (145, 17)), pygame.Rect((372, 248), (9, 64)),
                 pygame.Rect((268, 304), (113, 7)), pygame.Rect((268, 344), (112, 16)),
                 pygame.Rect((316, 455), (16, 50)), pygame.Rect((268, 248), (112, 64))]
        # walls.append(pygame.Rect((x, y), (width, height)))
        # This wall blocks off the central box area, as it is a trap for ghosts
        return walls

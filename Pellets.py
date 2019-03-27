import pygame

from Sound import Sound


class Pellets(object):
    images = [pygame.image.load("dot.png").convert(),
              pygame.image.load("bigdot.png").convert()]
    imageRects = [images[0].get_rect(), images[1].get_rect()]
    shifts = [(-images[0].get_width() / 2, -images[0].get_height() / 2),
              (-images[1].get_width() / 2, -images[1].get_height() / 2)]

    def createListSmall(self):
        """in - (self)
        Creates a list of small pellet (x, y) tuples.
        out - list"""
        pellets = [(350, 72), (350, 423), (485, 185), (125, 185), (445, 424), (485, 136), (125, 378), (395, 378),
                   (485, 72), (395, 424), (445, 72), (445, 136), (165, 424), (255, 185), (395, 136), (125, 104),
                   (205, 424), (205, 136), (395, 474), (165, 520), (255, 136), (165, 72), (205, 72), (255, 378),
                   (395, 330), (205, 330), (350, 104), (525, 185), (525, 378), (525, 474), (485, 474), (445, 185),
                   (525, 424), (300, 72), (350, 474), (350, 232), (485, 520), (445, 520), (485, 424), (445, 280),
                   (165, 378), (395, 185), (445, 378), (125, 474), (205, 520), (205, 185), (350, 185), (255, 520),
                   (350, 378), (350, 136), (300, 136), (300, 104), (445, 232), (205, 232), (445, 330), (300, 474),
                   (125, 424), (255, 72), (125, 136), (300, 520), (395, 520), (205, 281), (205, 104), (300, 185),
                   (255, 330), (165, 185), (165, 136), (205, 474), (205, 378), (255, 474), (395, 232), (165, 474),
                   (255, 232), (300, 378), (350, 330), (255, 280), (525, 104), (300, 330), (525, 136), (395, 72),
                   (485, 378), (445, 104), (350, 520), (300, 424), (300, 232), (445, 474), (395, 280), (255, 424)]
        return pellets

    def createListLarge(self):
        """in - (self)
        Creates a list of large pellet (x, y) tuples.
        out - list"""
        pellets = [(125, 72), (125, 520), (525, 72), (525, 520)]
        return pellets

    def check(self, pellets_s, pellets_l, pacman, ghosts):
        """in - (self, list of small pellets, list of large pellets, pacman, list of ghosts)
        Checks if pacman has eaten pellets, deletes eaten pellets, and plays pickup sound."""
        for i, p in enumerate(pellets_s[:]):
            p_rect = Pellets.imageRects[0]
            (p_rect.centerx, p_rect.centery) = p
            if p_rect.colliderect(pacman.rect):
                del pellets_s[i]
                pacman.score += 10
                if not Sound.channel.get_busy():
                    Sound.channel.play(Sound.pickUp_small)

        for i, p in enumerate(pellets_l[:]):
            p_rect = Pellets.imageRects[1]
            (p_rect.centerx, p_rect.centery) = p
            if p_rect.colliderect(pacman.rect):
                for g in ghosts:
                    g.makeBlue()
                del pellets_l[i]
                pacman.score += 50
                if not Sound.channel.get_busy():
                    Sound.channel.play(Sound.pickUp_large)

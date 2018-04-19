import scrollphathd as sphd
from random import randrange


class Screen:
    width = 17
    height = 7

    def __init__(self):
        self.pixels = []
        for w in range(self.width):
            self.pixels.append([])
            for h in range(self.height):
                self.pixels[w].append(None)

    def clear(self):
        for w in range(self.width):
            for h in range(self.height):
                self.pixels[w][h] = None

    def tick(self):
        for w in range(self.width):
            for h in range(self.height):
                if self.pixels[w][h]:
                    self.pixels[w][h].tick()
        self.show()

    def set(self, x, y, pixel):
        self.pixels[x][y] = pixel

    def get(self, x, y):
        return self.pixels[x][y]

    def get_width(self):
        return self.width - 1

    def get_height(self):
        return self.height - 1

    def show(self):
        for w in range(self.width):
            for h in range(self.height):
                if self.pixels[w][h]:
                    sphd.set_pixel(w, h, self.pixels[w][h].get_brightness())
                else:
                    sphd.set_pixel(w, h, 0)
        sphd.set_brightness(0.1)
        sphd.show()


class BlinkingPixel:
    def __init__(self):
        self.state = randrange(0, 2)

    def tick(self):
        if self.state == 0:
            self.state = 1
        else:
            self.state = 0

    def get_brightness(self):
        return self.state


class RandomBlinkingPixel:
    def __init__(self):
        self.state = 0

    def tick(self):
        self.state = randrange(0, 2)

    def get_brightness(self):
        return self.state


class ConstantPixel:
    def __init__(self):
        self.state = 1

    def tick(self):
        pass

    def get_brightness(self):
        return self.state

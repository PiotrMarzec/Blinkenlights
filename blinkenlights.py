import screen
from random import randrange


class Blinkenlights:
    constant = 5
    blinking = 5
    random_blinking = 10
    pause_every_ticks = 3
    pause_length_ticks = 2
    new_screen_every_ticks = 25

    def __init__(self):
        self.screen = screen.Screen()
        self.constant_left = 0
        self.blinking_left = 0
        self.random_blinking_left = 0
        self.tick_counter = 1
        self.pause_tick_counter = 0
        self.generate_new_screen()

    def generate_new_screen(self):
        self.constant_left = self.constant
        self.blinking_left = self.blinking
        self.random_blinking_left = self.random_blinking
        self.tick_counter = 1
        self.screen.clear()

        while self.get_total_left():
            for x in range(self.screen.get_width()):
                for y in range(self.screen.get_height()):
                    if self.screen.get(x, y) is None:
                        self.screen.set(x, y, self.generate_pixel())

    def generate_pixel(self):
        rand = randrange(0, 20)

        if rand == 1:
            if self.constant_left > 0:
                self.constant_left -= 1
                return screen.ConstantPixel()

        if rand == 2:
            if self.blinking_left > 0:
                self.blinking_left -= 1
                return screen.BlinkingPixel()

        if rand == 3:
            if self.random_blinking_left > 0:
                self.random_blinking_left -= 1
                return screen.RandomBlinkingPixel()

    def get_total_left(self):
        return self.constant_left + self.blinking_left + self.random_blinking_left

    def tick(self):
        if self.tick_counter % self.pause_every_ticks == 0:
            try:
                self.pause()
                return
            except PauseOverLimit:
                pass

        self.screen.tick()

        if self.tick_counter > self.new_screen_every_ticks:
            self.generate_new_screen()

        self.tick_counter += 1

    def pause(self):
        self.pause_tick_counter += 1

        if self.pause_tick_counter > self.pause_length_ticks:
            self.pause_tick_counter = 0
            raise PauseOverLimit()


class PauseOverLimit(Exception):
    pass

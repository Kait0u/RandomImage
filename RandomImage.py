"""
[2023-05-03]

RandomImage class, by Kait0u

The following class inherits from Pillow's Image class.
Its purpose is to render a randomly generated picture based off an integer variable <complexity>.
The higher its value, the more shapes will be drawn and the more chaotic the end product will be.

"""

import PIL.Image, PIL.ImageDraw
from random import randint, choice
from random import seed as randseed

class RandomImage(PIL.Image.Image):
    __DEFAULT_DIM = 600

    def _randcol(self) -> str:
        """
        Generates a string with a random hex color, like #RRGGBB
        """
        r = hex(randint(0, 255))[2:]
        g = hex(randint(0, 255))[2:]
        b = hex(randint(0, 255))[2:]

        r = r if len(r) == 2 else f"0{r}"
        g = g if len(g) == 2 else f"0{g}"
        b = b if len(b) == 2 else f"0{b}"

        return f"#{r}{g}{b}"

    def _randpoints(self, n: int) -> list:
        """
        Generates a list of points (2*n coordinates)
        """
        return [(randint(1, self.width - 1), randint(1, self.height - 1)) for _ in range (n)]

    def add_randline(self):
        """
        Draws a random straight line (2 points)
        """
        coords = self._randpoints(2)
        color = self._randcol()
        width = randint(1, (sum(self.size) // randint(12, 80)))
        self.draw.line(coords, fill=color, width=width, joint=choice([None, "curve"]))
    
    def add_randpolyline(self):
        """
        Draws a random polyline (at least 3 points, scales with complexity)
        """
        coords = self._randpoints(randint(3, self.complexity * 2))
        color = self._randcol()
        width = randint(1, (sum(self.size) // randint(12, 80)))
        self.draw.line(coords, fill=color, width=width, joint=choice([None, "curve"]))
    
    def add_randoval(self):
        """
        Draws a random oval
        """
        coords = self._randpoints(2)
        fill_color = self._randcol()
        outline_color = self._randcol()
        width = randint(1, (sum(self.size) // randint(12, 80)))
        self.draw.ellipse(coords, fill=fill_color, outline=outline_color, width=width)
    
    def add_randpolygon(self):
        """
        Draws a random polygon (at least 3 points, scales with complexity)
        """
        coords = self._randpoints(randint(3, self.complexity * 2))
        fill_color = self._randcol()
        outline_color = self._randcol()
        width = randint(1, (sum(self.size) // randint(12, 80)))
        self.draw.polygon(coords, fill=fill_color, outline=outline_color, width=width)

    def add_randrectangle(self):
        """
        Draws a random rectangle
        """
        coords = tuple(self._randpoints(2)) # For some reason it wants a tuple here instead of a list like elsewhere
        fill_color = self._randcol()
        outline_color = self._randcol()
        width = randint(1, (sum(self.size) // randint(12, 80)))
        self.draw.rectangle(coords, fill=fill_color, outline=outline_color, width=width)
        
    def regenerate(self):
        """
        Resets the image and performs
        """
        self.__init__(self.complexity, mode=self.mode, size=self.size, aa=self.aa, seed=self.image_seed)

    def get_seed(self):
        """
        Returns the current random number seed, or None if it doesn't exist
        """
        return self.image_seed

    def set_seed(self, seed):
        """
        Sets the random number seed (can be None)
        """
        self.image_seed = seed

    def set_antialiasing(self, aa):
        """
        Sets the antialiasing setting to one of Pillow constants (can also be None)
        """
        self.aa = aa

    def __init__(self, complexity: int, mode = "RGBA", size = (__DEFAULT_DIM, __DEFAULT_DIM), aa = None, seed = None):
        """
        Creates an instance of the PIL.Image object and draws a random image using it.
        The default dimensions are 600x600px and the default mode is RGBA.
        """
        sample = PIL.Image.new(mode, size, color=self._randcol())
        state = sample.__getstate__()
        super().__setstate__(state)
        del sample
        
        self.complexity = complexity
        self.image_seed = seed
        self.draw = PIL.ImageDraw.Draw(self)
        self.element_count = randint(self.complexity // 2, self.complexity + self.complexity // 2)
        self.f = [self.add_randline, self.add_randpolyline, self.add_randoval, self.add_randpolygon, self.add_randrectangle]
        self.aa = aa
        
        if self.image_seed is not None:
            randseed(self.image_seed)
        
        for _ in range(self.element_count):
            numbers = [randint(0, len(self.f) - 1) for i in range(self.complexity)]
            num = choice(numbers)
            self.f[num]()
        
        if self.aa is not None:
            self.resize(self.size, self.aa)

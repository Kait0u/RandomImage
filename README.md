# RandomImage
 A Pillow's Image child class which generates random images.

## Usage

Simply create an instance of the class. The constructor's got arguments familiar from Pillow's Image.new() method, and a few new ones.

```python
__init__(self, complexity: int, mode = "RGBA", size = (__DEFAULT_DIM, __DEFAULT_DIM), aa = None, seed = None)
```

`complexity` is a variable that defines how chaotic the randomly generated picture will be. The higher its value, e.g. the more joints may appear in a polyline, and the more objects will be drawn on the screen. Subject to minor, random fluctuations.

`__DEFAULT_DIM` is a variable whose value is 600, thus unless specified otherwise, the end result will have a resolution of 600x600 pixels.

`aa` stands for antialiasing. You can leave it at `None` or use one of Pillow's built-in constants, such as:

* PIL.Image.LANCZOS
* PIL.Image.BILINEAR
* PIL.Image.BICUBIC
just to name a few.

`seed` takes in a `None` or a value that will serve as a seed if you want to keep things repeatable.

## Example

From there you can use it like any other Pillow Image object. Example:

```python
img = RandomImage(20, size=(1920, 1080), aa=PIL.Image.BILINEAR)
img.show()
```

## Methods

Methods you can use:

* `get_seed(self)` - returns the current seed value or None
* `set_seed(self, seed)` - sets the random number seed (can be None)
* `set_antialiasing(self, aa)` - sets the antialiasing setting to one of Pillow constants (can also be None)
* `regenerate(self)` - generates a new picture in place of the one currently stored in the object, according to set-up parameters






import math

class Complex:
    def __init__(self, re: float, im: float) -> None:
        self.re = re
        self.im = im

    def abs(self) -> float:
        return math.sqrt(self.re ** 2 + self.im ** 2)

def add(z1: Complex, z2: Complex) -> Complex:
    return Complex(z1.re + z2.re, z1.im + z2.im)

def mul(z1: Complex, z2: Complex) -> Complex:
    return Complex(z1.re * z2.re - z1.im * z2.im, z1.re * z2.im + z1.im * z2.re)


if __name__ == '__main__':
    x = Complex(1, 2)
    y = Complex(3, 5)
    z = add(x, y)
    print(z.re, z.im)
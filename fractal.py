
from complex import Complex, add, mul

SIZE = 1024
C = Complex(-0.82, 0.147)
ITERS = 200

def isInJuliaSet(z: Complex) -> bool:
    for i in range(ITERS):
        z = add(mul(z, z), C)
        if z.abs() > 1000:
            return False
    return True

def complexNumberForPixel(i: int, j: int) -> Complex:
    re = 1.5 * (SIZE - 2 * i) / SIZE
    im = 1.5 * (SIZE - 2 * j) / SIZE
    return Complex(re,im)

def fillWithColor(pixel: dict, r: int, g: int, b: int) -> None:
    pixel['R']=r
    pixel['G']=g
    pixel['B']=b
    
pixels=[]

for i in range(SIZE):
    pixels.append([])
    for j in range(SIZE):
        pixels[i].append({
            'R':0,
            'G':0,
            'B':0
        })
        z=complexNumberForPixel(i,j)
        if isInJuliaSet(z):
            fillWithColor(pixels[i][j], 40, 196, 232)
            
print('P3')
print(SIZE, SIZE)
print(255)
for i in range(SIZE):
    for j in range(SIZE):
        print(pixels[i][j]['R'],pixels[i][j]['G'],pixels[i][j]['B'])

PI = 3.141592653589793
E = 2.718281828459045

def fact(n):
    r = 1
    for i in range(2, int(n) + 1):
        r *= i
    return r

def sqrt(x):
    if x < 0:
        raise ValueError
    return x ** 0.5

def sin(x):
    x = x % (2 * PI)
    return sum((-1) ** k * x ** (2*k + 1) / fact(2*k + 1) for k in range(12))

def cos(x):
    return sin(x + PI / 2)

def tan(x):
    return sin(x) / cos(x)

def ln(x):
    if x <= 0:
        raise ValueError
    y = 0.0
    for _ in range(100):
        y = y - 1 + x / E ** y
    return y

def log10(x):
    return ln(x) / ln(10)

def rad(d):
    return d * PI / 180

def deg(r):
    return r * 180 / PI

names = {"pi": PI, "e": E, "fact": fact, "sqrt": sqrt, "sin": sin,
         "cos": cos, "tan": tan, "ln": ln, "log": log10, "rad": rad, "deg": deg}

print("Engineering Calculator .|. Press q to Exit")

while True:
    text = input(">>> ")
    if text == "q":
        break
    try:
        print(eval(text, {"__builtins__": {}}, names))
    except Exception:
        print("Erorr: this char not valid")
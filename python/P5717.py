a, b, c = map(int, input().split())
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if a >= b + c:
    print("Not triangle")
else:
    if a ** 2 == b ** 2 + c ** 2:
        print("Right triangle")
    if a ** 2 < b ** 2 + c ** 2:
        print("Acute triangle")
    if a ** 2 > b ** 2 + c ** 2:
        print("Obtuse triangle")
    if b == c:
        print("Isosceles triangle")
    if a == b == c:
        print("Equilateral triangle")

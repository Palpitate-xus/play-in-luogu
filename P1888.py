import fractions
a, b, c = map(int, input().split())
d = max(a, b, c)
e = min(a, b, c)
print(fractions.Fraction(e, d))

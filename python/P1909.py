sum = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
case1 = int(sum / a[0])
case2 = int(sum / b[0])
case3 = int(sum / c[0])
if case1 * a[0] >= sum:
    price1 = case1 * a[1]
else:
    price1 = (case1 + 1) * a[1]

if case2 * b[0] >= sum:
    price2 = case2 * b[1]
else:
    price2 = (case2 + 1) * b[1]

if case3 * c[0] >= sum:
    price3 = case3 * c[1]
else:
    price3 = (case3 + 1) * c[1]

print(min(price1, price2, price3))



x, n = map(int, input().split())
# y = n % 7
# z = n // 7
# result = z * 5 * 250 + y * 250
result = 0
for i in range(x, x + n):
    if i % 7 != 0 and i % 7 != 6:
        result += 250
print(result)
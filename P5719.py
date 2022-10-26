n, k = map(int, input().split())
count1 = 0
count2 = 0
num1 = 0
num2 = 0
for i in range(1, n + 1):
    if i % k == 0:
        count1 += i
        num1 += 1
    else:
        count2 += i
        num2 += 1
print("%.1f %.1f"%(count1 / num1, count2 / num2))

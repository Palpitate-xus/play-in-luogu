usage = int(input())
sum = 0
if usage <= 150:
    sum = 0.4463 * usage
if usage > 150 and usage <= 400:
    sum = 0.4663 * (usage - 150) + 0.4463 * 150
if usage > 400:
    sum = 0.5663 * (usage - 400) + 0.4663 * 250 + 0.4463 * 150
print("%.1f"%sum)
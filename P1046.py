tree = list(map(int, input().split()))
height = int(input())
count = 0
for i in tree:
    if i <= height + 30:
        count += 1
print(count)
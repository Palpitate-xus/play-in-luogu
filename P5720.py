length = int(input())
days = 1
while length != 1:
    length = int(length / 2)
    days += 1
print(days)
data = input().split('-')
numbers = data[0] + data[1] + data[2]
sum = 0
for i in range(1, 10):
    sum += int(numbers[i-1]) * i
if data[3] != "X" and sum % 11 == int(data[3]):
    print("Right")
elif sum % 11 == 10:
    if data[3] == 'X':
        print("Right")
    else:
        print(data[0] + '-' + data[1] + '-' + data[2] + '-' + "X")
else:
    print(data[0] + '-' + data[1] + '-' + data[2] + '-' + str(sum % 11))
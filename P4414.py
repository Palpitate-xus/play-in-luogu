data = list(map(int, input().split()))
order = input()
data.sort()
result = ''
for i in order:
    result += str(data[ord(i) - 65]) + " "
print(result)

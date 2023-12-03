nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

text = []
while True:
    line = input()
    if line == 'james':
        break

    text.append(line)


numsForAdding = []
for i in text:
    firstNum = ''
    lastNum = ''

    for j in i:
        if j in nums:
            lastNum = j
            if firstNum == '':
                firstNum = j
    finalNum = firstNum+lastNum
    numsForAdding.append(int(finalNum))

answer = 0
for i in numsForAdding:
    answer += i

print(answer)
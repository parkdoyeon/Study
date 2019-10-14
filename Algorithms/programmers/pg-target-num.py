answer = 0
TARGET = 1

def rec(numbers, sum, index):
    if index is len(numbers):
        if sum is TARGET:
            global answer
            answer += 1
        return
    rec(numbers, sum+numbers[index], index+1)
    rec(numbers, sum-numbers[index], index+1)

numbers = [1, 1, 1, 1, 1]
rec(numbers, 0, 0)
print(answer)

def unlock(pibo):
    
    return dynamicarr[pibo]

count = int(input())
nums = []
dynamicarr = [1]*1000
for _ in range(count):
    nums.append(input())
arr = list(map(int, nums))
for i in arr:
    print(koong(i))
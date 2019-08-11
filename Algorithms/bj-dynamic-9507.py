dynamicarr = [-1]*70

def koong(pibo):
    if pibo < 2: return 1
    elif pibo == 2: return 2
    elif pibo == 3: return 4
    if dynamicarr[pibo] == -1:
        dynamicarr[pibo] = int(koong(pibo-1)) + int(koong(pibo-2)) + int(koong(pibo-3)) + int(koong(pibo-4))

    return dynamicarr[pibo]

count = int(input())
nums = []
for _ in range(count):
    nums.append(input())
arr = list(map(int, nums))
for i in arr:
    print(koong(i))
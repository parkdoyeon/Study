import sys

def insertionSort1(n, arr):
    target = arr[-1]
    idx = n-2
    
    while (target < arr[idx]) and (idx >= 0):
        arr[idx+1] = arr[idx]
        print(' '.join(map(str, arr)))
        idx -= 1
        
    arr[idx+1] = target
    print(' '.join(map(str, arr)))

def insertionSort1(n, arr):
    for rvidx in range(len(arr)-1, 0, -1):
        stored = arr[rvidx]
        for cp_rvidx in range(rvidx-1, -1, -1):
            if stored >= arr[cp_rvidx]:
                if arr[cp_rvidx+1] == stored: break
                arr[cp_rvidx+1] = stored
                stored = arr[cp_rvidx]
                print(*arr)
                break
            else:
                arr[cp_rvidx+1] = arr[cp_rvidx]
                print(*arr)
        if arr[0] > stored :
            arr[0] = stored
            print(*arr)    

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort1(n, arr)
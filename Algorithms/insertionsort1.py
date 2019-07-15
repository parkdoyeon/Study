import sys

# 한번만 정렬하는 알고리즘
def insertionSort1_Best(n, arr):
    target = arr[-1]
    idx = n-2
    
    while (target < arr[idx]) and (idx >= 0):
        print(target, arr[idx], idx)
        arr[idx+1] = arr[idx]
        print(' '.join(map(str, arr)))
        idx -= 1
        
    arr[idx+1] = target
    print(' '.join(map(str, arr)))

#내건 전체 다 정렬하는 알고리즘
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
    n = 1
    #arr = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    arr = [1,3,5,9,13,22,27,35,46,51,55,83,87,23]
    insertionSort1(n, arr)
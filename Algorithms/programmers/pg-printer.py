import heapq
def solution(priorities, location):
    seq = [-1]*len(priorities)
    poped = sorted(priorities[:], reverse=True)
    item = poped.pop(0)
    idx = priorities.index(item)
    print_seq = 0
    while -1 in seq:
        print_seq += 1
        item = poped.pop(0)
        idx = priorities.index(item)
        if seq[idx] is -1:
            seq[idx] = print_seq
        else:
            while seq[idx] is not -1:
                idx += 1
            seq[idx] = print_seq
        print(seq)
    
    return seq[location]

solution([1, 1, 9, 1, 1, 1], 0)
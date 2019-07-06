#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    weight = [1]*t_nodes
    for i in range(len(t_to)):
        search_queue = [t_from[i]]
        while len(search_queue) != 0:
            for j in range(len(t_to)):
                if search_queue[-1:][0] == t_to[j]: # 마지막 요소와 연결된 노드 확인
                    search_queue = [t_from[j]] + search_queue
                    weight[i] += 1
            search_queue.pop() # 확인이 끝나면 제거
    count = 0
    for item in weight:
        if item%2 == 0: count += 1
    return count

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()

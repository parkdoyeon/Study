//
//  CircularQueue.c
//  1219_7Queue
//
//  Created by DoYeon Park on 2018. 1. 2..
//  Copyright © 2018년 DoYeon Park. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include "CircularQueue.h"

int NextPosIdx(int pos)
{
    if (pos==QUE_LEN-1)
        return 0;
    else
        return pos+1;
}


void QueueInit(Queue* pq)
{
    pq->front = 0;
    pq->rear = 0;
}


int QIsEmpty(Queue* pq)
{
    if(pq->rear == pq->front) {
        return TRUE;
    } else {
        return FALSE;
    }
}

void Enqueue(Queue* pq, Data data)
{
    if(pq->rear < 100) {
        pq->rear += 1;
        pq->queArr[pq->rear] = data;
    }
}

Data Dequeue(Queue* pq)
{
    pq->front += 1;
    return pq->queArr[pq->front];
}

Data QPeek(Queue* pq)
{
    return pq->queArr[pq->rear];
}



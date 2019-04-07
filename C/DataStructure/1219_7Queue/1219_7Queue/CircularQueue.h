//
//  CircularQueue.h
//  1219_7Queue
//
//  Created by DoYeon Park on 2018. 1. 2..
//  Copyright © 2018년 DoYeon Park. All rights reserved.
//

#ifndef CircularQueue_h
#define CircularQueue_h

#define TRUE    1
#define FALSE   0

#define QUE_LEN 100
typedef int Data;

typedef struct _cQueue
{
    int front;
    int rear;
    Data queArr[QUE_LEN];
} CQueue;

typedef CQueue Queue;

void QueueInit(Queue* pq);
int QIsEmpty(Queue* pq);

int NextPosIdx(int pos);

void Enqueue(Queue* pq, Data data);
Data Dequeue(Queue* pq);
Data QPeek(Queue* pq);


#endif /* CircularQueue_h */

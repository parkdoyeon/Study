//
//  Deque.h
//  0327_Deque
//
//  Created by doyeon park on 2017. 1. 1..
//  Copyright © 2017년 WEBZEN INC. All rights reserved.
//

#ifndef Deque_h
#define Deque_h

#include <stdio.h>

#define TRUE    1;
#define FALSE   0;

typedef int Data;
typedef struct _node
{
    Data data;
    struct _node *next;
    struct _node *prev;
} Node;

typedef struct _dlDeque
{
    Node *head;
    Node *tail;
} DLDeque;

typedef DLDeque Deque;

void DequeInit(Deque *pdeq);
int DQIsEmpty(Deque *pdeq);

void DQAddFirst(Deque *pdeq, Data data);
void DQAddLast(Deque *pdeq, Data data);

Data DQRemoveFirst(Deque *pdeq);
Data DQRemoveLast(Deque *pdeq);

Data DQgetFirst(Deque *pdeq);
Data DQGetLast(Deque *pdeq);

#endif /* Deque_h */

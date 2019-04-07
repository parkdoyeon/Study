//
//  Deque.c
//  0327_Deque
//
//  Created by doyeon park on 2017. 1. 1..
//  Copyright © 2017년 WEBZEN INC. All rights reserved.
//

#include "Deque.h"

void DequeInit(Deque *pdeq)
{
    pdeq->head = NULL;
    pdeq->tail = NULL;
};

int DQIsEmpty(Deque *pdeq)
{
    if(pdeq->head == pdeq->tail)
    {
        return TRUE;
    }
    return FALSE;
}

void DQAddFirst(Deque *pdeq, Data data)
{
    Node* node = (Node*)malloc(sizeof(Node));
    node->next = pdeq->head;
    node->data = data;
    pdeq->head->prev = node;
}
void DQAddLast(Deque *pdeq, Data data)
{
    Node* node = (Node*)malloc(sizeof(Node));
    node->prev = pdeq->tail;
    node->data = data;
    pdeq->tail = pdeq->tail->next;
}

Data DQRemoveFirst(Deque *pdeq)
{
    Data removed = pdeq->head->data;
    pdeq->head = pdeq->head->next;
    return removed;
}
Data DQRemoveLast(Deque *pdeq)
{
    Data removed = pdeq->head->data;
    pdeq->tail = pdeq->tail->prev;
    return removed;
}

Data DQgetFirst(Deque *pdeq)
{
    Data data = pdeq->head->data;
    return data;
}

Data DQGetLast(Deque *pdeq)
{
    Data data = pdeq->tail->data;
    return data;
}

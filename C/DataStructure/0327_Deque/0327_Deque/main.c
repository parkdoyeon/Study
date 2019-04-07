//
//  main.c
//  0327_Deque
//
//  Created by doyeon park on 2017. 1. 1..
//  Copyright © 2017년 WEBZEN INC. All rights reserved.
//

#include <stdio.h>
#include "Deque.h"

int main(int argc, const char * argv[]) {
    // insert code here...
    printf("Hello, World!\n");
    
    Deque deq;
    DequeInit(&deq);
    
    DQAddFirst(&deq, 3);
    printf("%d ", DQgetFirst(&deq));
    
    DQAddFirst(&deq, 2);
    printf("%d ", DQgetFirst(&deq));
    
    DQAddFirst(&deq, 1);
    printf("%d ", DQgetFirst(&deq));
    
    
    DQAddLast(&deq, 4);
    printf("%d ", DQGetLast(&deq));
    DQAddLast(&deq, 5);
    printf("%d ", DQGetLast(&deq));
    DQAddLast(&deq, 6);
    printf("%d ", DQGetLast(&deq));
    
    while(!DQIsEmpty(&deq))
        printf("%d ", DQRemoveFirst(&deq));
    
    printf("\n");
    
    DQAddFirst(&deq, 3);
    DQAddFirst(&deq, 2);
    DQAddFirst(&deq, 1);
    
    DQAddLast(&deq, 4);
    DQAddLast(&deq, 5);
    DQAddLast(&deq, 6);
    
    while(!DQIsEmpty(&deq))
        printf("%d ", DQRemoveFirst(&deq));
    
    return 0;
}

//
//  main.c
//  1219_7Queue
//
//  Created by DoYeon Park on 2017. 12. 19..
//  Copyright © 2017년 DoYeon Park. All rights reserved.
//

#include <stdio.h>
#include "CircularQueue.h"


int main(int argc, const char * argv[]) {
    // insert code here...
    Queue q;
    QueueInit(&q);
    
    Enqueue(&q, 1);
    Enqueue(&q, 2);
    Enqueue(&q, 3);
    Enqueue(&q, 4);
    Enqueue(&q, 5);
    
    while(!QIsEmpty(&q))
        printf("%d ", Dequeue(&q));
    
    return 0;
}

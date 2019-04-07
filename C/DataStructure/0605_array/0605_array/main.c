//
//  main.c
//  0605_array
//
//  Created by DoYeon Park on 2017. 6. 6..
//  Copyright © 2017년 DoYeon Park. All rights reserved.
//

#include <stdio.h>

int main(void)
{
    
    //선언
    int aList[5][5] = { 0 };
    int col = -1, row = 0, nCounter = 0, nLine=9;
    int i = 0, j = 0, nDirection = 1;
    

    //배열 입력
    for(nLine = 9; nLine > 0; nLine -=2)
    {
        for(i = 0; i < nLine; ++i)
        {
            if(i < nLine/2+1) col += nDirection;
            else row += nDirection;
            
            aList[row][col] = ++nCounter;
        }
        
        nDirection = -nDirection;
    }
    
    
    //출력
    for(i=0; i<5; ++i)
    {
        for(j=0; j<5; ++j)
        {
         printf("%d ", aList[i][j]);
        }
        putchar('\n');
    }
    
    return 0;
}

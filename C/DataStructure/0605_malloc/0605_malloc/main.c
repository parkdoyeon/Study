//
//  main.c
//  0605_malloc
//
//  Created by DoYeon Park on 2017. 6. 5..
//  Copyright © 2017년 DoYeon Park. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>

int main(void) {
    char szSrcBuf[12] = { "Hello" };
    char szDstBuf[12] = { 0 };
    
    char* const pszData = malloc( sizeof(char)*12 ); //pszData에는 *pszData주소값이 저장되고, *pszData에는 malloc사이즈가 만들어진다.
    
    memcpy(szDstBuf, szSrcBuf, sizeof(szDstBuf));
    
    pszData = szSrcBuf;
    
    puts(pszData);
    free(pszData);
    
    return 0;
}

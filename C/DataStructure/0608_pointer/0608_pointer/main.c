//
//  main.c
//  0608_pointer
//
//  Created by DoYeon Park on 2017. 6. 8..
//  Copyright © 2017년 DoYeon Park. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>

typedef struct USERDATA
{
    int nAge;
    char szName[32];
    char szPhone[32];
} USERDATA;

int main(void)
{
    USERDATA *pUser = NULL; //pUser에는 Null이 담기고, *pUser에는 USERDATA형태로 자료형이 구축된 상태
    
    pUser = (USERDATA*)malloc(sizeof(USERDATA)); //USERDATA만큼의 메모리를 할당하고 그 주소값을 저장. (주소의 이름은 *pUser이 됨)
    //pUser의 자료형이 USERDATA*이므로, malloc의 void*자료형을 강제 형변환 해준다. (사실 C에선 안해도 되지만 C++과의 호환을 위해 형변환 표시를 해준다.)
    //malloc의 자료형이 void*인 것은, 주소를 리턴하므로 포인터는 맞지만, 그 주소의 자료형을 어떻게 해석할지는 정하지 않았기 때문이다.
    
    pUser->nAge = 10;  //*pUser의 nAge위치에 10이 들어감 (배열과 같음, 화살표가 인덱스를 표시한다고 생각하면 됨.)
    strcpy(pUser->szName, "Hoon"); //*pUser의 szName위치에 "Hoon"이 들어감
    strcpy(pUser->szPhone, "98736"); //*pUser의 szPhone위치에 "98736"이 들어감
    
    printf("%d살\t%s\t%s\n", pUser->nAge, pUser->szName, pUser->szPhone);
    
    free(pUser);
    
    return 0;
}

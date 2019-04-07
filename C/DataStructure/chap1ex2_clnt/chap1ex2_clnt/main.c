//
//  main.c
//  chap1ex2_clnt
//
//  Created by DoYeon Park on 2017. 6. 3..
//  Copyright © 2017년 DoYeon Park. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

void error_handling(char *message);

int main(int argc, const char * argv[]) {
    
    int sock;
    struct sockaddr_in serv_addr;
    char message[30];
    int str_len;
    
    if(argc!=3)
    {
        printf("Usage : %s <IP> <port>\n", argv[0]);
        exit(1);
    }
    
    sock = socket(PF_INET, SOCK_STREAM, 0);
    if(sock == -1)
        error_handling("socket() error");
    
    memset(&serv_addr, 0, sizeof(serv_addr));
    
    //소켓의 주소를 초기화한다. 그런데 위에서 생성한 소켓의 주소가 아닌 연결할 상대의 주소를 할당하는 것이다.
    serv_addr.sin_family=AF_INET;
    serv_addr.sin_addr.s_addr=inet_addr(argv[1]);
    serv_addr.sin_port=htons(atoi(argv[2]));
    
    //그리고 할당받은 주소로 연결한다
    if(connect(sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) == -1)
        error_handling("connect() error!");
    
    //서버쪽에서 write한 데이터를 read하는 것이다.
    str_len = read(sock, message, sizeof(message)-1);
    if(str_len == -1)
        error_handling("read() error!");
    
    //읽은 데이터를 출력한다
    printf("Message from server: %s \n", message);
    close(sock);
    
    return 0;
}


void error_handling(char *message)
{
    fputs(message, stderr);
    fputc('\n', stderr);
    exit(1);
}

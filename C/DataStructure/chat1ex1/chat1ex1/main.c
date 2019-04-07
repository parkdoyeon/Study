//
//  main.c
//  chat1ex1
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
    // insert code here...
    int serv_sock;
    int clnt_sock;
    
    struct sockaddr_in serv_addr;
    struct sockaddr_in clnt_addr;
    socklen_t clnt_addr_size;
    
    char message[]="Hello World!";
    
    if(argc != 2)
    {
        printf("Usage : %s <port>\n", argv[0]);
        exit(1);
    }
    
    serv_sock = socket(PF_INET, SOCK_STREAM, 0); //소켓을 생성함, OS가 생성한 소켓을 int형으로 넘겨준다
    
    if(serv_sock == -1)
        error_handling("socket() error");
    
    memset(&serv_addr, 0, sizeof(serv_addr)); //serv_addr이라는 구조체에 서버정보를 저장하기 전에 우선 0으로 다 클리어 해준다
    
    //주소정보 부여 과정
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    serv_addr.sin_port = htons(atoi(argv[1]));
    
    //바인드 함수 호출해서 소켓의 주소정보를 전달한다.
    if(bind(serv_sock, (struct sockaddr*) &serv_addr, sizeof(serv_addr)) == -1)
        error_handling("socket() error");
    
    if(listen(serv_sock, 5) == -1)
        error_handling("listen() error");
    
    //누군가 내게 연락을 했든 안했든 우선 호출하면서 묻는것임 누가 날 호출했는지, 연결이 되면 그때서야 accept함수가 int를 반환함
    clnt_addr_size = sizeof(clnt_addr);
    clnt_sock = accept(serv_sock, (struct sockaddr*)&clnt_addr, &clnt_addr_size);
    if(clnt_sock == -1)
        error_handling("accpet() error");
    
    // 데이터 전달
    write(clnt_sock, message, sizeof(message));
    
    // OS에 통신 종료를 알리면서 소켓 소멸을 요구 - 서버와 클라이언트 둘 다 종료시켜야함
    close(clnt_sock);
    close(serv_sock);
    
    return 0;
}

void error_handling(char *message)
{
    fputs(message, stderr);
    fputc('\n', stderr);
    exit(1);
}

#include <stdio.h>
#include <stdlib.h>

typedef struct _node
{
    int data;
    struct _node * next;
} Node;

int main(void)
{
    Node* head = NULL;
    Node* cur = NULL;
    Node* tail = NULL;
    Node* newNode = NULL;
    int readData;
    
    while(1) {
        printf("자연수 입력: ");
        scanf("%d", &readData);
        
        if(readData < 0)
            break;
        
        newNode = malloc(sizeof(Node));
        newNode->data = readData;
        newNode->next = NULL;
        
        if(head == NULL)
            head = newNode;
        else
            tail->next = newNode;
        
        tail = newNode;
    }
    
    //출력
    if(head == NULL)
        puts("출력할 데이터가 없습니다.");
    else
    {
        cur = head;
        printf("%d ", cur->data);
        
        while(cur->next != NULL)
        {
            cur = cur->next;
            printf("%d ", cur->data);
        }
        printf("출력 완료\n");
    }
    
    
    //삭제
    
    if(head == NULL)
        puts("삭제할 데이터가 없습니다.");
    else
    {
        Node* deleteNode = head;
        Node* deleteNodeNext = head->next;
        printf("%d을(를) 삭제합니다. \n", deleteNode->data);
        free(deleteNode);
        
        while(deleteNodeNext != NULL)
        {
            deleteNode = deleteNodeNext;
            deleteNodeNext = deleteNode->next;
            
            printf("%d을(를) 삭제합니다. \n", deleteNode->data);
            free(deleteNode);
        }
    
    }
    
    return 0;
}

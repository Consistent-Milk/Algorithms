#include <stdlib.h>
#include <stdio.h>

struct Node {
    int data;
    struct Node* next;  
};

struct Node* head;

int main() {
    head = NULL;
}
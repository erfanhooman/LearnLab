#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
    struct Node *prev;
};

struct List {
    struct Node *head;
    int n;
};

struct Node* createNode(int data) {
    struct Node *node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->next = NULL;
    node->prev = NULL;
    return node;
}

struct List* createList() {
    struct List *list = (struct List*)malloc(sizeof(struct List));
    list->head = createNode(0); // The head's data is set to 0 (or any other suitable default value)
    list->head->next = list->head;
    list->head->prev = list->head;
    list->n = 0;
    return list;
}

struct Node* get(struct List *list, int ind) {
    if (ind > list->n) {
        printf("Out of list\n");
        exit(1);
    }
    struct Node *x = list->head;
    for (int i = 0; i < ind; ++i) {
        x = x->next;
    }
    return x;
}

struct Node* insert_after(struct List *list, struct Node *x, int data) {
    struct Node *y = createNode(data);
    list->n += 1;
    y->prev = x;
    y->next = x->next;
    x->next = y;
    y->next->prev = y;
    return y;
}

struct Node* delete(struct List *list, struct Node *x) {
    list->n -= 1;
    if (list->n == 0) {
        printf("Linked list is empty\n");
        exit(1);
    }
    x->prev->next = x->next;
    x->next->prev = x->prev;
    return x;
}

struct Node* find(struct List *list, int val) {
    struct Node *x = list->head->next;
    for (int i = 0; i < list->n; ++i) {
        if (x->data == val) {
            return x;
        }
        x = x->next;
    }
    return NULL;
}

int size(struct List *list) {
    return list->n;
}

int is_empty(struct List *list) {
    return list->n == 0;
}

struct Node* insert(struct List *list, int ind, int data) {
    if (ind > list->n + 1 || ind < 1) {
        printf("Invalid index for insertion\n");
        exit(1);
    }
    struct Node *x = get(list, ind - 1);
    return insert_after(list, x, data);
}

struct Node* delete_at(struct List *list, int ind) {
    if (ind > list->n || ind < 1) {
        printf("Invalid index for deletion\n");
        exit(1);
    }
    struct Node *x = get(list, ind);
    return delete(list, x);
}
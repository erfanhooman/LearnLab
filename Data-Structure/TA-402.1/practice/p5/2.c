#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Function to create a new node
Node* create_node(int value) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    if (!new_node) {
        printf("Memory allocation failed.\n");
        exit(1);
    }
    new_node->data = value;
    new_node->next = NULL;
    return new_node;
}

// Insert at the end of the list
void append(Node** head, int value) {
    Node* new_node = create_node(value);
    if (*head == NULL) {
        *head = new_node;
        return;
    }
    Node* temp = *head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = new_node;
}

// Insert after a given node
void insert_after(Node* node, int value) {
    if (node == NULL) {
        printf("The given node is NULL.\n");
        return;
    }
    Node* new_node = create_node(value);
    new_node->next = node->next;
    node->next = new_node;
}

// Insert before a given node
void insert_before(Node** head, Node* node, int value) {
    if (node == NULL || *head == NULL) {
        printf("The given node or the head is NULL.\n");
        return;
    }
    if (*head == node) { // If inserting before the head
        Node* new_node = create_node(value);
        new_node->next = *head;
        *head = new_node;
        return;
    }
    Node* temp = *head;
    while (temp->next != node && temp->next != NULL) {
        temp = temp->next;
    }
    if (temp->next == node) {
        Node* new_node = create_node(value);
        new_node->next = node;
        temp->next = new_node;
    } else {
        printf("The given node is not in the list.\n");
    }
}

// Delete the node after a given node
void delete_after(Node* node) {
    if (node == NULL || node->next == NULL) {
        printf("No node to delete after the given node.\n");
        return;
    }
    Node* temp = node->next;
    node->next = temp->next;
    free(temp);
}

// Delete the node before a given node
void delete_before(Node** head, Node* node) {
    if (node == NULL || *head == NULL || *head == node) {
        printf("No node to delete before the given node.\n");
        return;
    }
    if ((*head)->next == node) { // If deleting the head
        Node* temp = *head;
        *head = (*head)->next;
        free(temp);
        return;
    }
    Node* temp = *head;
    while (temp->next != NULL && temp->next->next != node) {
        temp = temp->next;
    }
    if (temp->next->next == node) {
        Node* to_delete = temp->next;
        temp->next = node;
        free(to_delete);
    } else {
        printf("The given node is not in the list.\n");
    }
}
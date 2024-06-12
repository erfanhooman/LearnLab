#include <stdio.h>
#include <stdlib.h>

struct DoubleEndedQueue {
    int max_size;
    int *Q;
    int num;
    int first;
};

struct DoubleEndedQueue* createDeque(int max_size) {
    struct DoubleEndedQueue *deque = (struct DoubleEndedQueue*)malloc(sizeof(struct DoubleEndedQueue));
    deque->max_size = max_size;
    deque->Q = (int*)malloc(max_size * sizeof(int));
    deque->num = 0;
    deque->first = 0;
    return deque;
}

void push_back(struct DoubleEndedQueue *deque, int item) {
    if (deque->num >= deque->max_size) {
        printf("Queue overflow\n");
        exit(1);
    }
    deque->Q[(deque->num + deque->first) % deque->max_size] = item;
    printf("Push_back at index: %d\n", (deque->num + deque->first) % deque->max_size);
    deque->num += 1;
}

void push_front(struct DoubleEndedQueue *deque, int item) {
    if (deque->num >= deque->max_size) {
        printf("Queue overflow\n");
        exit(1);
    }
    deque->first = (deque->first - 1 + deque->max_size) % deque->max_size;
    printf("Push_front at index: %d\n", deque->first);
    deque->Q[deque->first] = item;
    deque->num += 1;
}

int pop_front(struct DoubleEndedQueue *deque) {
    if (deque->num == 0) {
        printf("Queue empty\n");
        exit(1);
    }
    int item = deque->Q[deque->first];
    deque->first = (deque->first + 1) % deque->max_size;
    deque->num -= 1;
    return item;
}

int front(struct DoubleEndedQueue *deque) {
    if (deque->num == 0) {
        printf("Queue empty\n");
        exit(1);
    }
    return deque->Q[deque->first];
}

int pop_back(struct DoubleEndedQueue *deque) {
    if (deque->num == 0) {
        printf("Queue empty\n");
        exit(1);
    }
    deque->num -= 1;
    return deque->Q[(deque->num + deque->first) % deque->max_size];
}

int back(struct DoubleEndedQueue *deque) {
    if (deque->num == 0) {
        printf("Queue empty\n");
        exit(1);
    }
    return deque->Q[(deque->num + deque->first - 1 + deque->max_size) % deque->max_size];
}

int is_empty(struct DoubleEndedQueue *deque) {
    return deque->num == 0;
}

int size(struct DoubleEndedQueue *deque) {
    return deque->num;
}

int is_full(struct DoubleEndedQueue *deque) {
    return deque->num >= deque->max_size;
}

void freeDeque(struct DoubleEndedQueue *deque) {
    free(deque->Q);
    free(deque);
}

int main() {
    struct DoubleEndedQueue *deque = createDeque(10);

    push_back(deque, 1);
    push_back(deque, 2);
    push_front(deque, 3);

    printf("Front: %d\n", front(deque));
    printf("Back: %d\n", back(deque));

    pop_front(deque);

    printf("Front after pop_front: %d\n", front(deque));

    pop_back(deque);

    printf("Back after pop_back: %d\n", back(deque));

    freeDeque(deque);

    return 0;
}
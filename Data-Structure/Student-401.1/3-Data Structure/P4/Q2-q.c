#include <stdio.h>
#include <stdlib.h>

struct Queue {
    int max_size;
    int *Q;
    int num;
    int first;
};

struct Queue* createQueue(int max_size) {
    struct Queue *queue = (struct Queue*)malloc(sizeof(struct Queue));
    queue->max_size = max_size;
    queue->Q = (int*)malloc(max_size * sizeof(int));
    queue->num = 0;
    queue->first = 0;
    return queue;
}

void enqueue(struct Queue *queue, int item) {
    if (queue->num >= queue->max_size) {
        printf("Queue overflow\n");
        exit(1);
    }
    queue->Q[(queue->num + queue->first) % queue->max_size] = item;
    queue->num += 1;
}

int dequeue(struct Queue *queue) {
    if (queue->num == 0) {
        printf("Queue empty\n");
        exit(1);
    }
    int item = queue->Q[queue->first];
    queue->first = (queue->first + 1) % queue->max_size;
    queue->num -= 1;
    return item;
}

int front(struct Queue *queue) {
    if (queue->num == 0) {
        printf("Queue empty\n");
        exit(1);
    }
    return queue->Q[queue->first];
}

int end_Q(struct Queue *queue) {
    if (queue->num == 0) {
        printf("Queue empty\n");
        exit(1);
    }
    return queue->Q[(queue->num + queue->first - 1 + queue->max_size) % queue->max_size];
}

int first_IDX(struct Queue *queue) {
    return queue->first;
}

int is_empty(struct Queue *queue) {
    return queue->num == 0;
}

int size(struct Queue *queue) {
    return queue->num;
}

int is_full(struct Queue *queue) {
    return queue->num >= queue->max_size;
}

int get_i(struct Queue *queue, int i) {
    return queue->Q[i];
}

void freeQueue(struct Queue *queue) {
    free(queue->Q);
    free(queue);
}

int main() {
    struct Queue *queue = createQueue(10);

    enqueue(queue, 1);
    enqueue(queue, 2);
    enqueue(queue, 3);

    printf("Front: %d\n", front(queue));
    printf("End: %d\n", end_Q(queue));
    printf("First index: %d\n", first_IDX(queue));

    dequeue(queue);

    printf("Front after dequeue: %d\n", front(queue));

    printf("Value at index 1: %d\n", get_i(queue, 1));

    freeQueue(queue);

    return 0;
}
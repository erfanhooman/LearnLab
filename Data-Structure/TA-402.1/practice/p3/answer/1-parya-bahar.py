def radix_sort(A):
    radix=1
    while radix <= max(A): # go from first bucket until the largest number
        bucket = [[] for _ in range(16)] # initial bucket

        for i in A:
            bucket[(i//radix)%16]+=[i]

        A=[]
        for i in range(len(bucket)):
            A+=bucket[i]
        radix*=16

    for i in range(len(A)):
        A[i]=hex(A[i])

    return A


a=list(map(str,input().split(',')))
int_a=[]
result=[]
for i in a:
    int_a.append(int(i,16))
result=radix_sort(int_a)
print(result)
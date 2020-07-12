import math

num = int(input())

opcount = [0, 0] + [math.inf]*(num-1)

for i in range(2,num+1):
    t1, t2, t3 = [math.inf]*3

    t1 = opcount[i-1]+1
    if i%2 == 0: t2 = opcount[i//2]+1
    if i%3 == 0: t3 = opcount[i//3]+3

    min_opcount = min(t1,t2,t3)
    opcount[i] = min_opcount

print(opcount[num])

numbers = [num]
while num!=1:
    if num%3 == 0 and opcount[num] - 1 == opcount[num//3]:
        numbers += [num//3]
        num = num // 3
    elif num%2 == 0 and opcount[num]-1 == opcount[num//2]:
        numbers += [num//2]
        num = num//2
    else:
        numbers += [num-1]
        num = num - 1

print(' '.join([str(i) for i in numbers][::-1]))
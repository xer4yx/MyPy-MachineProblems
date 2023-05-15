N = list(map(int, input().split()))
M = int(input())
counter = 0
i = 1

while i < len(N):
    if N[i] - N[i - 1] == M:
        counter += 1
    i += 1 
    
if counter != 0:
    print(counter)
else:
    print('none')
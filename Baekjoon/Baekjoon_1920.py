from sys import stdin
import time
start = time.time()

n_1 = int(stdin.readline())
input_list = list(map(int, stdin.readline().split()))

input_list = sorted(list(set(input_list)))

n_2 = int(stdin.readline())
flag_list = list(map(int, stdin.readline().split()))

for x in flag_list:
    

print()
print(time.time() - start)
k = int(input())

n = 0
while True:
    if k < (2**n) - 1:
        k -= (2**(n-1)) - 1
        break
    n += 1
n -= 1

bin_k = bin(k)[2:]
bin_k = bin_k.replace("1", "3")
minus_flag = "0"*(n-len(bin_k))
minus_flag += str(bin_k)

flag = ("4"*n)
print(int(flag) + int(minus_flag))

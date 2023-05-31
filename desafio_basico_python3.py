
import sys

N = int(input())



while(N > 0):
    input_number = sys.stdin.readline()
    #print(input_number)

    N = N - 1

    A = input_number.split()[0]
    B = input_number.split()[1]

    result = A.endswith(B)

    if result == True:
        print(f"encaixa")
    else:
        print(f"nao encaixa")
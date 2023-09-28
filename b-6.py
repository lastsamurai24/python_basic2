import random

def dice():
   
    N = int(input("サイコロの面の数は?: "))

    M = int(input("何回振りますか?: "))

    results = [random.randint(1, N) for _ in range(M)]

  
    print(results)
    print("以上")

dice()
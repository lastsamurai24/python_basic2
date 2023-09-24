num = int(input("行数を入力してください: "))
nim = int(input("列数を入力してください: "))

for i in range(1, num+1):
    for j in range(1, nim+1):
        print(i * j, end=" ")
    print()
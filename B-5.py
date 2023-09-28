
"""
def main():
    data_input = input("データを入力してください(スペース区切り) > ")
    numbers = list(map(int, data_input.split()))

    print("合計値:", calculate_sum(numbers))
    print("最大値:", find_max(numbers))
    print("最小値:", find_min(numbers))
    print("平均値:", calculate_average(numbers))

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def find_max(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


def find_min(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value


def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)

  

if __name__ == "__main__": 
    main()
"""
"""
def main():
    data_input = input("データを入力してください(スペース区切り) > ")
    numbers = [int(num) for num in data_input.split()]

    print("合計値:", calculate_sum(numbers))
    print("最大値:", find_max(numbers))
    print("最小値:", find_min(numbers))
    print("平均値:", calculate_average(numbers))

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def find_max(numbers):
    max_value = numbers[0]
    for num in numbers[1:]:
        if num > max_value:
            max_value = num
    return max_value

def find_min(numbers):
    min_value = numbers[0]
    for num in numbers[1:]:
        if num < min_value:
            min_value = num
    return min_value

def calculate_average(numbers):
    total = calculate_sum(numbers)
    count = 0
    for _ in numbers:
        count += 1
    return total / count

if __name__ == "__main__":
    main()
"""
def calculator():
    numbers = input("データを入力してください(スペース区切り) > ")
    sum_numbers = 0 
    number_list = []
    for num in numbers.split():
        number_list.append(int(num))
       
    for i in number_list:
        sum_numbers += i
    print(f"合計数:{sum_numbers}")
    max_value = number_list[0]
    min_value = number_list[0]

    for num in number_list[1:]: 
        if num > max_value:
           max_value = num
        if num < min_value:
           min_value = num 
    print(f"最大値:{max_value}")
    print(f"最小値:{min_value}")

    count = 0
    for _ in number_list:
        count += 1

    average = sum_numbers / count
    print(f"平均値:{average}")

calculator()      
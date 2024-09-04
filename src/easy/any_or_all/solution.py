if __name__ == '__main__':
    n = int(input())  # 输入元素个数
    numbers = list(map(int, input().split()))  # 输入数字列表

    all_positive = all(num > 0 for num in numbers)

    any_palindrome = any(str(num) == str(num)[::-1] for num in numbers)

    if all_positive and any_palindrome:
        print(True)
    else:
        print(False)
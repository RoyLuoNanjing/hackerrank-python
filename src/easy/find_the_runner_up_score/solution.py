if __name__ == '__main__':
    n = int(input())  # 输入数字个数
    arr = list(map(int, input().split()))  # 输入的数字列表

    # 将列表转换为集合以去除重复元素
    arr = list(set(arr))

    # 去除最大的数字
    arr.remove(max(arr))

    # 找到剩下的最大的数字，即第二大的数字
    runner_up = max(arr)

    print(runner_up)
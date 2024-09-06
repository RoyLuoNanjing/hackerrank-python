def print_door_mat(N, M):
    # 上部分
    for i in range(1, N, 2):
        print((i * ".|.").center(M, "-"))

    # 中间部分
    print("WELCOME".center(M, "-"))

    # 下部分
    for i in range(N - 2, 0, -2):
        print((i * ".|.").center(M, "-"))


# 示例输入
N, M = map(int, input().split())  # 输入地垫的高度 N 和宽度 M
print_door_mat(N, M)
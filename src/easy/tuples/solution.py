# 获取输入的整数 n
n = int(input())

# 获取空格分隔的整数，并将它们转换为一个整数元组
tuple_values = tuple(map(int, input().split()))

# 计算并打印元组的哈希值
print(hash(tuple_values))
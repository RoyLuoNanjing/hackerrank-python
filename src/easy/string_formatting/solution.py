def print_formatted(number):
    # 计算二进制表示的最大宽度（不包含 '0b' 前缀）
    width = len(bin(number)) - 2

    # 从 1 到 number 逐个打印
    for i in range(1, number + 1):
        # 依次打印十进制、八进制、十六进制（大写）、二进制，并对齐
        print(f"{i:{width}d} {oct(i)[2:]:{width}} {hex(i)[2:].upper():{width}} {bin(i)[2:]:{width}}")
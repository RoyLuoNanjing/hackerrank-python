
if __name__ == '__main__':
    N = int(input())

    res_list = []

    def perform_actions(input_str_list):
        _str = input_str_list[0]
        value = int(input_str_list[1]) if len(input_str_list) > 1 else None

        if _str == "insert":
            res_list.insert(value, int(input_str_list[2]))
        elif _str == "print":
            print(res_list)
        elif _str == "remove":
            res_list.remove(value)
        elif _str == "append":
            res_list.append(value)
        elif _str == "sort":
            res_list.sort()
        elif _str == "pop":
            res_list.pop()
        elif _str == "reverse":
            res_list.reverse()

    for i in range (N):
        input_str = input()
        input_str_list = input_str.split(" ")
        action_str = input_str_list[0]
        perform_actions(input_str_list)









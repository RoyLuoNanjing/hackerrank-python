def count_substring(string, sub_string):
    count = 0
    # Loop through the string with a window the size of the substring
    for i in range(len(string) - len(sub_string) + 1):
        # If the slice of the string matches the substring, increment count
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    result = count_substring(string, sub_string)
    print(result)
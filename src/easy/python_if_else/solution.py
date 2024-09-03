if __name__ == '__main__':
    n = int(input().strip())

    modules = n % 2

    if modules == 1 or (6 <= n <=20):
        print("Weird")
    elif 2 <= n <= 5 or n >= 20:
        print("Not Weird")

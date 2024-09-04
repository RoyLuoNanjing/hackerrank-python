# Complete the time_delta function below.
from datetime import datetime
def time_delta(t1, t2):
    # 定义时间格式
    fmt = "%a %d %b %Y %H:%M:%S %z"

    # 将字符串解析为 datetime 对象
    time1 = datetime.strptime(t1, fmt)
    time2 = datetime.strptime(t2, fmt)
    # 计算时间差
    delta = abs(time1 - time2)

    # 返回时间差的秒数
    return str(int(delta.total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
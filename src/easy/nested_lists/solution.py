if __name__ == '__main__':
    list_total = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_single = [name,score]
        list_total.append(list_single)

    list_score = [x[1] for x in list_total]

    min_score = min(list_score)
    list_score = [score for score in list_score if score != min_score]
    second_max_score = min(list_score)

    list_second_names = sorted([x[0] for x in list_total if x[1] == second_max_score])
    for i in list_second_names:
        print(i)

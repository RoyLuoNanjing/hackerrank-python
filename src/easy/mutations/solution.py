def mutate_string(string, position, character):
    _list = [x for x in string]
    _list[position] = character


    return "".join(_list)
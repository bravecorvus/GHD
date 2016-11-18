def exists(key, my_list):
    if not isinstance(my_list, list) or not my_list:
        return False
    return (my_list[0] == key
        or exists(key, my_list[0])
        or exists(key, my_list[1:]))


print(exists("yolo", [[1, 2, 3, 4, 15], [15, 0, 3, 4], [6, 7, 2, 15]]))
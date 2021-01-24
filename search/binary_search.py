def binary_search(list1, v):
    list_size = len(list1)
    index_i = 0
    index_n = list_size - 1

    while index_i < index_n:
        mid = int((index_i+index_n)/2)

        if list1[mid] == v:
            return mid

        if list1[mid] < v:
            index_i = mid + 1
        else:
            index_n = mid - 1

    if index_i > index_n:
        return None


list1 = [1, 2, 3, 4, 5, 56, 90]

if __name__ == '__main__':
    print(binary_search(list1, 56))
    print(binary_search(list1, 8))

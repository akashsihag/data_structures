def binary_search(list, indx0, indxn, val):
    if indxn < indx0:
        return None
    else:
        midval = int((indx0 + indxn)/2)

        if list[midval] < val:
            return binary_search(list, midval+1, indxn, val)
        elif list[midval] > val:
            return binary_search(list, 0, midval-1, val)
        else:
            return midval


list2 = [1,2,33,45,56,71]

if __name__ == '__main__':
    print(binary_search(list2, 0, 5, 56))
def intersection(arrays):
    """
    YOUR CODE HERE
    """
    integers = {}
    result = []
    for x in arrays:
        for y in x:
            if y not in integers:
                integers[y] = 0
            else:
                result.append(y) 
    result= list(dict.fromkeys(result))

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

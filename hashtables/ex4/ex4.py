def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = []
    dict = {}
    for num in a:
        if dict.get(abs(num)):
            result.append(abs(num))
        else:
            dict[abs(num)] = num

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    result = []
    
    z = {}
    
    for num in a:
        if z.get(abs(num)):
            result.append(abs(num))
        else:
            z[abs(num)] = num

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

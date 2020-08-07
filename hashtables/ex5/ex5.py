# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []
    
    z = {}

    for f in files:
        x = f.split("/")
        y = x[-1]

        if y not in z:
            z[y] = []

        z[y].append(f)

    for query in queries:
        if query in z:
            result.extend(z[query])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

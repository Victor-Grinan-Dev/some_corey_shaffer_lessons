def regression(x):
    print(x)
    if x > 0:
        regression(x - 1)
    print(x)
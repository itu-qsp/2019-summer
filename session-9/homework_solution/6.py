def make_positive(a):
    for i in range(len(a)):
        if a[i] < 0:
            a[i] = -a[i]
    return a

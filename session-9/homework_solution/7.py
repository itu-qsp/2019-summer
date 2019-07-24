def count_small(l):
    return len([x for x in l if x >= 1 and x <= 100])


# Alternative solution with loop instead of list comprehension
# We only mentioned list comprehensions
def count_small(l):
    smalls = []
    for x in l:
        if x >= 1 and x <= 100:
            smalls.append(x)
    return len(smalls)

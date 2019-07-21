import random
from timeit import default_timer
from sort_algos import bubble_sort, selection_sort, merge_sort
import matplotlib.pyplot as plt

list1 = list(range(1000))
list2 = list(range(10000))
list3 = list(range(100000))
list4 = list3[:] # Copy the full list3 into list4 ([:] is a slicing operation that copies ALL elements)
random.shuffle(list4) # Shuffles list4, so the elements are now in random positions
"""
for idx, current_list in enumerate([list1, list2, list3, list4]):
    startb = default_timer()
    bubble_sort(current_list)
    endb = default_timer()

    starts = default_timer()
    selection_sort(current_list)
    ends = default_timer()

    startm = default_timer()
    merge_sort(current_list)
    endm = default_timer()

    print("List"+str(idx+1), endb-startb, ends-starts, endm-startm)
"""
"""
                | list1   list2   list3   list4
                |
bubble_sort     | 0.04    4.99    729.2    1532
selection_sort  | 0.03    3.50    546      471.6
merge_sort      | 0.51    0.03    0.52     0.93
"""

for algorithm in [[0.04, 4.99, 729.2], [0.03, 3.5, 546], [0.51, 0.03, 0.52]]:
    x = [1000, 10000, 100000]
    y = algorithm
    plt.plot(x, y)
    plt.show()

#Bubble sort in 2 minutes: https://www.youtube.com/watch?v=xli_FI7CuzA
#Selection sort in 3 minutes: https://www.youtube.com/watch?v=g-PGLbMth_g
#Merge sort in 3 minutes: https://www.youtube.com/watch?v=4VqmGXwpLqc
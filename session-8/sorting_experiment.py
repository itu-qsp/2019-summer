import sys
import math
import string
from sort_algos import merge_sort, selection_sort


def prepare_data(path):
    with open(path, encoding='utf-8') as f:
        data = f.read()

    trans_table = str.maketrans({key: None for key in string.punctuation})
    new_data = data.translate(trans_table)
    return new_data.split()


def main(a_or_b):
    words = prepare_data('the_adventures_of_sherlock_holmes.txt')
    # words = words[:10000]
    n = len(words)

    if a_or_b == 'a':
        print('The book contains {} words'.format(n))
        print('Sort  algorithm A, O(n log n)')
        merge_sort(words)
        # print(words)
    else:
        print('----------------------------------------------------')
        print('Sort  algorithm  B, O(n**2)')
        selection_sort(words)


if __name__ == '__main__':
    main(sys.argv[1])

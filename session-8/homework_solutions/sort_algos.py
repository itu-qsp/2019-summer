"""A collection of sorting algorithms, based on:
  * http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html
  * http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html

Use the resources above for illustrations and visualizations.
"""


def bubble_sort(data_list):
    for passnum in range(len(data_list) - 1, 0, -1):
        for idx in range(passnum):
            if data_list[idx] > data_list[idx + 1]:
                temp = data_list[idx]
                data_list[idx] = data_list[idx + 1]
                data_list[idx + 1] = temp
#Growth rate is O(n*n)
#Bubble sort in 2 minutes: https://www.youtube.com/watch?v=xli_FI7CuzA


def selection_sort(data_list):
    for fill_slot in range(len(data_list) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fill_slot + 1):
            if data_list[location] > data_list[position_of_max]:
                position_of_max = location

        temp = data_list[fill_slot]
        data_list[fill_slot] = data_list[position_of_max]
        data_list[position_of_max] = temp

#O(n*n)
#Selection sort in 3 minutes: https://www.youtube.com/watch?v=g-PGLbMth_g

def merge_sort(data_list):
    # print("Splitting ", data_list)
    if len(data_list) > 1:
        mid = len(data_list) // 2
        left_half = data_list[:mid]
        right_half = data_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data_list[k] = left_half[i]
                i = i + 1
            else:
                data_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            data_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            data_list[k] = right_half[j]
            j = j + 1
            k = k + 1
    # print("Merging ", data_list)

#O(n*logn) (linearithmic time)
#Merge sort in 3 minutes: https://www.youtube.com/watch?v=4VqmGXwpLqc


def sort_algo_b(data_list):
    selection_sort(data_list)


def sort_algo_a(data_list):
    merge_sort(data_list)



if __name__ == '__main__':

    data_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(data_list)
    print(data_list)

    data_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort(data_list)
    print(data_list)
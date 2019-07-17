def bubble_sort(data_list):
    """Sorts a given list

    Args: 
      data_list: A list of numbers

    Returns:
      The same list sorted such that the first number is the smallest
    """
    for passnum in range(len(data_list) - 1, 0, -1):
        for idx in range(passnum):
            if data_list[idx] > data_list[idx + 1]:
                temp = data_list[idx]
                data_list[idx] = data_list[idx + 1]
                data_list[idx + 1] = temp

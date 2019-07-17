def find_element_in_list(data_list, element):
    for idx, el in enumerate(data_list):
        if el == element:
            return idx

if __name__ == '__main__':
    data_list = range(10000)
    result = find_element_in_list(data_list, 5000)
    print(result)
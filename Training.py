# small file to stroing training data from webside:
# https://www.practicepython.org/


def odd_even(num_1: int):
    if num_1 % 2 > 0:
        print('odd number')
    else:
        print('even numebr')


def list_les(list_1: list, num_1: int):
    res = []

    for element in list_1:
        if element < num_1:
            res.append(element)

    print(res)


def divisorts(num_1: int):
    res = []
    rezult = []
    res = list(range(1, num_1))
    print(res)
    for i in res:
        if num_1 % i == 0:
            rezult.append(i)
    print(rezult)

def overlap_lists(list_1, list_2):
    list_1_len = len(list_1)
    list_2_len = len(list_2)
    list_larger = []
    list_smaller= []
    outout_list = []

    if list_1_len > list_2_len:
        list_larger= list_1
        list_smaller = list_2
    else:
        list_larger = list_2
        list_smaller = list_1

    for element in list_smaller:
        if element in list_larger:
            if element not in outout_list:
             outout_list.append(element)

    print(outout_list)
# small file to stroing training data from webside:
# https://www.practicepython.org/


def odd_even(num_1 : int):
    if num_1 % 2 > 0:
        print('odd number')
    else:
        print('even numebr')
def list_les(list_1: list, num_1:int):
    res =[]

    for element in list_1:
        if element < num_1:
            res.append(element)

    print(res)

def divisorts(num_1 : int):
    res = []
    res = range(2,num_1)
    print(res)




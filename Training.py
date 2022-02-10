# small file to stroing training data from webside:
# https://www.practicepython.org/
import random


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
    #(res)
    for i in res:
        if num_1 % i == 0:
            rezult.append(i)
    return rezult

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


def palindorm(sentence):
    sentence = str(sentence)
    reverse = sentence[::-1]
    if sentence == reverse:
        print("it is palindorm")
    else:
        print("it is not palindrom")

def guessing_game():
    ran_num = random.randint(1, 9)
    input_num = input("Please provide number")
    while input_num != "exit":

        if int(input_num) == ran_num:
            print("Exact number")
            break
        elif int(input_num) > ran_num:
            print("too high")
        else:
            print("too low")

        input_num = input("Please provide number")

def comprehension_list(list_1:[], list_2:[]):
    result_list = [i for i in set(list_1) if i in list_2]
    return [i for i in result_list if result_list.count(i)==1]

def prime_number(number_1: int):
    if len(divisorts(number_1)) == 1:
        print("it is prime numebr")
    else:
        print("it is not prime numebr")

def list_ends(input_list:[]):
    return [input_list[0], input_list[-1]]

def Fibonacci(input_num: int):
    result_list =[]
    while len(result_list)< input_num:
        if len(result_list)==0:
            result_list.append(1)
        elif len(result_list) == 1:
            result_list.append(1)
        else:
            result_list.append(result_list[-1]+result_list[-2])
    return result_list
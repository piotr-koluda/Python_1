# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# section to import library. It could be created by myself or downloaded.
import random
import Training

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_twinkle(name):
    print('Twinkle, twinkle, little star,\n\tHow I wonder what you are! ')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   # print_twinkle('test')
    listt_1 = list(range(1, random.randint(1,30)))
    listt_2 = list(range(1, random.randint(1,67)))
    a = [1,1,2,3,5,8,13,21,34,55,89]
    b = [1,78,44,34,2,3,5,8,13,21,34,55,89]
   # Training.odd_even(3)
   # Training.list_les(a, 55)
   # Training.divisorts(10)
   # Training.overlap_lists(listt_1, listt_2)
    #Training.palindorm("aabcaa")
    #a = [1,4,9,16,25,36,49,64,81,100]
    #new_list = [num for num in a if num%2==0] # całkiem instotne - zapamiętać jak to robić, bo może się bardzo przydał w przysłości
    #print(new_list);
    #vlaue = input("value")
    #Training.guessing_game()
    #print(sorted(Training.comprehension_list(a, b)))
    #Training.prime_number(12)
    #print(Training.list_ends(a))
    print(Training.Fibonacci(14))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import matplotlib.pyplot as plt
import numpy as np
import random

amt = int(input('Enter a random integer greater than 10: '))

if amt <= 10:
    amt = 15

sort = int(input('''Enter
\t 1 for Bubble Sort
\t 2 for Selection Sort
\t 3 for Insertion Sort
\t 4 for Merge Sort
'''))

def BubbleSort(amt):
    lst = np.random.randint(0, 100, amt)
    x = np.arange(0, amt, 1)
    n = len(lst)

    for i in range(n):
        for j in range(0, n-i-1):
            plt.bar(x,lst)
            plt.pause(0.001)
            plt.clf()
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        
    plt.show()


def InsertionSort(amt):
    lst = np.random.randint(0, 100, amt)
    x = np.arange(0, amt, 1)

    n=len(lst)
    # INSERTION SORT

    for k in range(1, n):
        key = lst[k]
        l = k-1
        while l>=0 and key < lst[l]:
            lst[l+1] = lst[l]
            l = l-1
            plt.bar(x,lst)
            plt.pause(0.001)
            plt.clf()
        else:
            lst[l+1] = key

    plt.show()


def SelectionSort(amt):
        lst = np.random.randint(0, 100, amt)
        x = np.arange(0, amt, 1)
        n = len(lst)


        for i in range(0, n - 1):
                smallest = i    
                for j in range(i + 1, n):
                        plt.bar(x,lst)
                        plt.pause(0.001)
                        plt.clf()
                        if lst[j] < lst[smallest]:
                                smallest = j
                lst[i], lst[smallest] = lst[smallest], lst[i]
        plt.show()


def MergeSort(amt):
    num =  [random.randint(0, 1000) for _ in range(amt)]

    def merge_sort(lst, left, right):

        if left >= right:
            return

        mid = (left + right)//2
    
        plt.bar(list(range(amt)), lst)
        plt.pause(0.001)
        plt.clf()

        merge_sort(lst, left, mid)
        merge_sort(lst, mid+1, right)
    
        plt.bar(list(range(amt)), lst)
        plt.pause(0.001)
        plt.clf()

        merge(lst, left, right, mid)
        plt.bar(list(range(amt)), lst)
        plt.pause(0.001)
        plt.clf()


    def merge(lst, left, right, mid):

        l_cy = lst[left:mid+1]
        r_cy = lst[mid+1:right+1]

        l_cou = r_cou = 0

        count = left
    
        while l_cou < (len(l_cy)) and r_cou < (len(r_cy)):
            if l_cy[l_cou] <= r_cy[r_cou]:
                lst[count] = l_cy[l_cou]
                l_cou += 1
            else:
                lst[count] = r_cy[r_cou]
                r_cou += 1

            count += 1

        while l_cou < (len(l_cy)):
            lst[count] = l_cy[l_cou]
            l_cou += 1
            count += 1
    
        while l_cou < (len(r_cy)):
            lst[count] = r_cy[r_cou]
            r_cou += 1
            count += 1



    merge_sort(num, 0, len(num)-1)
    plt.bar(list(range(amt)), num)
    plt.show()


if sort == 1:
    BubbleSort(amt)
elif sort == 2:
    SelectionSort(amt)
elif sort == 3:
    InsertionSort(amt)
elif sort == 4:
    MergeSort(amt)
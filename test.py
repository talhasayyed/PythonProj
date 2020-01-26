# class Pycharm:
#     def execute(self):
#         print('compile')
#
# class Laptop:
#     def code(self,ide):
#         ide.execute()
#
# ide = Pycharm()
#
# l1 = Laptop()
# l1.execute(ide)








#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    sum=0
    for e in ar:
        sum = sum + e
    print(sum)
    #

if __name__ == '__main__':
    fptr = open('abc', 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()




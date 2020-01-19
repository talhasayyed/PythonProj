# linear search

list = [1,2,3,4,5,6,7]

n = 6

def search(list,n):
    i = 0

###     using while loop
    while i<=len(list):
        if list[i] == n:
            return True
        i += 1
    return False


###     using for loop

    # for i in list:
    #     if i == n:
    #         return True
    #
    # return False


if search(list,n):
    print('fount',n)
else:
    print('not found')
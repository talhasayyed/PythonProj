# linear search

#      [0][1]......[7]
list0 = [1,7,3,8,5,6,9]
list = sorted(list0)
n = 6       # Search Value
pos = 0


def search(list,n):
    l = 0
    u = len(list)-1

###     using while loop
    while l <= u:
        mid = (l+u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid
            else:
                u = mid
    return False




###     using for loop

    # for i in list:
    #     if i == n:
    #         return True
    #
    # return False


if search(list,n):
    print('fount',n,'at pos=',pos+1)
else:
    print('not found')
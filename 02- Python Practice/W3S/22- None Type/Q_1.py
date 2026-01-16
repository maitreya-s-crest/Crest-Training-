def none_calc(arr):
    if len(arr) == 0:
        return 0
    head , *tail = arr
    if head == None:
        return 1 + none_calc(tail)
    else:
        return none_calc(tail)


list1 = [None,1,2,4,None,None,None,3,4,None]

print(none_calc(list1))
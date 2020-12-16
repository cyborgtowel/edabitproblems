def find_fulcrum(lst):
    sumleft = 0
    sumright = 0
    for i in range(len(lst)-1):
        sumleft = sum(l for l in lst[:i])
        sumright = sum(r for r in lst[i+1:])
        if sumleft == sumright:
            return lst[i]
    return -1


    

print(find_fulcrum([1, 2, 4, 9, 10, -10, -9, 3])) #➞ 4

print(find_fulcrum([9, 1, 9])) #➞ 1

print(find_fulcrum([7, -1, 0, -1, 1, 1, 2, 3])) #➞ 0

print(find_fulcrum([8, 8, 8, 8])) #➞ -1	
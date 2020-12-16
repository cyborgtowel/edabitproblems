def find_fulcrum(lst):
    sumleft = 0
    sumright = 0
    for i in range(len(lst)-1):
        sumleft = sum(l for l in lst[:i])
        sumright = sum(r for r in lst[i+1:])
        if sumleft == sumright:
            return lst[i]
    return -1


    

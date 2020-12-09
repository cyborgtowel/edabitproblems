def stock_picker(lst):
    diff = -1
    for curr in lst:
        curr_index = lst.index(curr)
        for remaining in range(curr_index+1, len(lst)):
            if lst[remaining] - curr >= diff:
                diff = lst[remaining] - curr
    return diff
            

print(stock_picker([90, 100, 111, 0, 1, 2, 3]))# 21
print(stock_picker([1, 2, 4, 10, 100, 2, 3]))# 99
print(stock_picker([10, 1000, 1, 1, 1, 2000, 3]))# 1999
print(stock_picker([7, 1, 5, 5, 2, 1, 3]))# 4
print(stock_picker([100, 10, 8, 5]))# -1

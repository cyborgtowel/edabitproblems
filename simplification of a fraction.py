#simplification of a fraction
def simplify(n):
    for i in range(len(n)):
        if n[i] == '/':
            numer = int(n[:i])
            denom = int(n[i+1:])
    if numer > denom:
        if numer % denom == 0:
            return str(int(numer/denom))
        else:
            whole = numer//denom
            numer = numer-(whole*denom)
            largest = denom
    else:
        whole = "Nothing"
        largest = numer
    for divisor in range(largest+1, 0, -1):
        if denom % divisor == 0 and numer % divisor == 0 and whole == "Nothing":
            numer = int(numer/divisor)
            denom = int(denom/divisor)
            result = str(numer) + '/' + str(denom)
            return result
        if denom % divisor == 0 and numer % divisor == 0:
            numer = int(numer/divisor)
            denom = int(denom/divisor)
            result = str(numer) + '/' + str(denom)
            return str(whole) + '/' + result


# print(simplify("4/6"))
# print(simplify("10/11"))
# print(simplify("100/400"))
# print(simplify("8/4"))
# print(simplify("800/300"))
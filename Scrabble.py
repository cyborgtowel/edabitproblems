def can_build(word, letters):
    wildcardcount = sum(1 for h in letters if h == "#")
    result = True
    for e in word:
        out = False
        index = 0
        size = len(letters)-1
        while index <= size:
            if e == letters[index].lower():
                out = True
                letters.pop(letters.index(e.upper()))
                break
            index += 1
        if out == False:
            if wildcardcount == 0:
                return False
            else: 
                letters.remove("#")
                wildcardcount -= 1
    return result


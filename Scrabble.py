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

# Alternative solution
# def can_build(word, letters):
# 	for i in word.upper():
# 		if i in letters:
# 			letters.remove(i)
# 		elif '#' in letters:
# 			letters.remove('#')
# 		else:
# 			return False
# 	return True


print(can_build("quavers", ["S", "U", "Q", "V", "A", "#", "#"])) #, True)
print(can_build("move", ["M", "U", "T", "V", "E", "J", "#"])) #, True)
print(can_build("banter", ["N", "E", "B", "N", "#", "A", "T"])) #, True)
print(can_build("snake", ["S", "K", "E", "N", "V", "J", "A"])) #, True)
print(can_build("move", ["M", "U", "T", "V", "E", "J", "S"])) #, False)
print(can_build("sharp", ["S", "K", "H", "#", "#", "F", "F"])) #, False)
print(can_build("more", ["M", "R", "I", "E", "U", "S", "F"])) #, False)
print(can_build("talker", ["#", "#", "Z", "V", "P", "A", "K"])) #, False)
print(can_build("talker", ["#", "#", "T", "T", "A", "A", "L"])) #, False)
print(can_build("brain", ["#", "S", "B", "B", "I", "I", "#"])) #, False)
print(can_build("pip", ["#", "P", "I", "S", "V", "W", "Z"])) #, True)
print(can_build("pip", ["X", "P", "I", "S", "V", "W", "Z"])) #, False)
print(can_build("stuff", ["F", "F", "X", "S", "U", "A", "T"])) #, True)
print(can_build("stuff", ["F", "Z", "X", "S", "U", "A", "T"])) #, False)
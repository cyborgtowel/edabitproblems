# The Karaca's Encryption Algorithm

def encrypt(n):
    encrypted = ''
    vowels = {'a':0, 'e':1, 'i':2, 'o':2, 'u':3}
    for letter in range(len(n)-1, 0, -1):
        if n[letter] in vowels:
            encrypted += str(vowels[n[letter]])
        else:
            encrypted += n[letter]
    return encrypted+'aca'

# print(encrypt("banana"))  #"0n0n0baca"
# print(encrypt("karaca"))  #"0c0r0kaca"
# print(encrypt("burak"))  #"k0r3baca"
# print(encrypt("alpaca"))  #"0c0pl0aca"
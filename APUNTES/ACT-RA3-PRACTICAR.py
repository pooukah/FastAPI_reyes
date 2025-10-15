
################################# 7.9.3 #####################################

def uses_only(palabra, letras):
    for letra in palabra:
        if letra not in letras:
            return False
    return True

#print(uses_only('banana', 'ban'))           #TRUE
#print(uses_only('apple', 'apl'))            #FALSE
#print(uses_only('hello', 'helo'))           #TRUE
#print(uses_only('python', 'pythn'))         #FALSE

################################# 7.9.4 #####################################

def uses_all(palabra, letras):
    for letra in palabra:
        if letra not in letras:
            return False
    return True

#print(uses_all('banana', 'ban'))
#print(uses_all('apple', 'api'))

################################# 9.15.2 #####################################

def is_anagram(pal1, pal2):
    if sorted(pal1) == sorted(pal2):
        return True
    return False

#print(is_anagram('tops', 'stop'))           #TRUE
#print(is_anagram('sopa', 'paso'))           #TRUE
#print(is_anagram('josep', 'jose'))          #FALSE

################################# 9.15.3 #####################################

def reverse_word(pal):
    return ''.join(reversed(pal))

#print(reverse_word('nipsi'))           #ispin
#print(reverse_word('sergio'))          #oigres
#print(reverse_word('niksa'))           #askin

def reverse






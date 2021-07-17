vowels = ['a', 'e', 'i', 'u', 'o']

def nya(sentence):
    listy = sentence.split()
    num = 0
    for i in listy:
        curr = list(i)
        try:
            if curr[0] not in vowels:
                curr[0] = 'ny'

            elif curr[1] == 'y':
                curr[0] = 'n'

            else:
                curr[0] = 'ny' + curr[0]

        except:
            if curr[0] not in vowels:
                curr[0] = 'ny'

            else:
                curr[0] = 'ny' + curr[0]

        listy[num] = ''.join(curr)
        num += 1

    return ' '.join(listy)


def split_str(s):
  return [ch for ch in s]

def oo(sentence):
    listy = split_str(sentence)

    for n, i in enumerate(listy):
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
         listy[n] = 'oo'

        if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
         listy[n] = 'OO'


    return ''.join(listy)

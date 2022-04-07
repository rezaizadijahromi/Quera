import string


def ascii_word(s):
    letter_counter = 0
    word = ""
    for w in s:
        if w in string.ascii_letters:
            letter_counter += 1
            word += w
    return word, letter_counter


def words_check(i):
    dic = dict()
    lis = i.split()
    lis2 = []
    for w in lis:
        counte = ascii_word(w)[1]
        if counte > len(w) // 2:
            lis2.append(ascii_word(w)[0].title())
    for w in lis2:
        if w not in dic:
            dic[w] = 1
        else:
            dic[w] += 1

    return dic

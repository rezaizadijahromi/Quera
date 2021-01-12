from collections import Counter
import itertools
import re 


def expand(s):
       s = iter(s)
       return "".join(c*int(d) for (c,d) in zip(s,s))

def greate_typer(n):
    result = []
    
    for i in range(n):
        switch = int(input())
        word = ''
        if switch == 1:
            lettres = list(input())
            asnswer = Counter(lettres)
            for i,j in asnswer.items():
                if j == 1:
                    word += f'{i}'
                else:
                    word += f'{i}{j}'
            result.append(word)
            

        elif switch == 2:
            letters2 = list(input())
            alph = []
            num = []
            word = ''
            store = {}
            for i in range(len(letters2)-1):
                if letters2[i].isalpha():
                    if letters2[i+1].isnumeric():
                        store[letters2[i]] = letters2[i+1]
                    else:
                        store[letters2[i]] = 1

            for i in range(len(letters2)):
                if letters2[-i].isalpha() and letters2[-i] not in store:
                    index = -i
                    store[letters2[-i]] = 1
                    break
            
            for i,j in store.items():
                k = int(j) * i
                word += k

            result.append(word)


            # print(store)
            # print(num)


        #### Garbage ####
        # else:
        #     s = (input())
        #     groups = ''.join(chr * int(num or 1) for chr, num in re.findall(r'(\w)(\d+)?', s)) 
        #     result.append(str(groups))


    for word in result:
        print(word)



n = int(input())
greate_typer(n)
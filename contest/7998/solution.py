def election_keyboard():
    n = int(input())
    caps = False
    candidate = []
    for i in range(n):
        word = input()
        if word == 'CAPS':
            caps = not caps
        elif caps:
            candidate.append(word.upper())
        else:
            candidate.append(word)

    return ''.join(candidate)


print(election_keyboard())

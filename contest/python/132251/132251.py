def departed():
    words = []
    response = []
    for i in range(5):
        code = input()
        words.append(code)
    for i in range(len(words)):
        if "FBI" in words[i]:
            response.append(str(i+1))
    if len(response) == 0:
        print("HE GOT AWAY!")
    else:
        print(*response)


departed()

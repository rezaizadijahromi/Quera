from operator import le


def compare(string1, string2):
    while string1 is not None or string2 is not None:
        s1, s2 = string1[0], string2[0]
        if ord(s1) > ord(s2):
            string2 = string2[1::]
        elif ord(s1) < ord(s2):
            string1 = string1[1::]
        elif ord(s1) == ord(s2):
            string1 = string1[1::]
            string2 = string2[1::]

        if len(string1) == 0 and len(string2) == 0:
            return "Both strings are empty!"

        if len(string1) == 0 or len(string2) == 0:
            if len(string1) == 0:
                return string2
            else:
                return string1

        string1 = string1[::-1]
        string2 = string2[::-1]


# print(compare('amin', 'nima'))
# compare('ali', 'salib')

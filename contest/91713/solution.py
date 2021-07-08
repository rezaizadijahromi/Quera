def round_number():
    javab = []
    adad = []
    n = int(input())
    for i in range(n):
        number = list(input())
        adad.append(number)


    for number in adad:
        counter_point = 0
        number_reverse = number[::-1]

        if counter_point == 0:
            for i in number:
                number_counter = number.count(i)
                if number_counter >= 4:
                    counter_point = 1
        if counter_point == 0:
            for i in range(0, len(number) - 2):
                if number[i] == number[i+1] and number[i+1] == number[i+2] :
                    counter_point = 1
        if counter_point == 0:
            if number == number_reverse:
                founded = True
                counter_point = 1

        if counter_point == 1:
            javab.append("Ronde!")
        else:
            javab.append("Rond Nist")

    for i in javab:
        print(i)




round_number()
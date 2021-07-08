def petrol():
    masraf = int(input())
    remain = int(input())
    if masraf <= 60:
        sumation = masraf * 1500
    else:
        dolaty = remain + 60
        if dolaty < masraf:
            qeymat_dolaty = dolaty * 1500
            bishtar = (masraf - dolaty) * 3000
            sumation = bishtar + qeymat_dolaty
        else:
            sumation = masraf * 1500

    return sumation
print(petrol())
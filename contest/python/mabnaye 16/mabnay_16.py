
def hex_to_hex_pulse():
    hexa = input()    
    dec = int(hexa, 16)
    # print(dec)
    return dec

def convert_to_binary():
    remainder_stack = []
    decimal_number = hex_to_hex_pulse()
    decimal_number += 1

    while decimal_number > 0:
        remainder = decimal_number % 2
        remainder_stack.append(remainder)
        decimal_number = decimal_number // 2

    if len(remainder_stack) % 4 != 0:
        while len(remainder_stack) % 4 != 0:
            remainder_stack.append(0)
    else:
        pass

    binary_digits = []
    while remainder_stack:
        binary_digits.append(str(remainder_stack.pop()))

    return ''.join(binary_digits)

def convert_binary_to_hex():
    simbles = {
        'a':'A', 'b':'B', 'c':'C',
        'd':'D', 'e':'E', 'f':'F'
    }

    hexa = []
    binary = convert_to_binary()
    for i in range(0, len(binary), 4):
        b_to_h = binary[i:i+4]
        hexa.append(hex(int(b_to_h, 2)).lstrip('0x') or '0')

    hexa_revers = []
    for i in hexa:
        pop_value = i
        if pop_value in simbles.keys():
            repl = simbles[pop_value]
            hexa_revers.append(repl)
        else:
            hexa_revers.append(pop_value)

    return ''.join(hexa_revers)

def str_base(val, base):
    res = ''
    while val > 0:
        res = str(val % base) + res
        # val /= base # only valid for Py2
        val //= base # for getting integer division
    if res: return res
    return '0'

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b

    listNumbers = []
    for i in range(len(digits)):
        listNumbers.append(str(digits.pop()))

    listNumbers = listNumbers[::-1]
    return ''.join(listNumbers)
    
    # binary_digits = []
    # while remainder_stack:
    #     binary_digits.append(str(remainder_stack.pop()))

    # return ''.join(binary_digits)
# print(convert_binary_to_hex())
# print(convert_to_binary())
# print(str_base(5639, 6))
# print(convert_binary_to_hex())
print(numberToBase(545330, 10))
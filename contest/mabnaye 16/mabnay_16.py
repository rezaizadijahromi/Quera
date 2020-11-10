
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
    

print(convert_binary_to_hex())
# print(convert_to_binary())
# print(convert_binary_to_hex())
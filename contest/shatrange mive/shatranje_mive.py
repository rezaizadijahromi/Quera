def fruits(fruit_list):
    result = {}
    for i in fruit_list:
        if i['shape'] == 'sphere' and 300 <= i['mass'] <= 600 and 100 <=['volume'] <= 500 :
            name = i['name']
            k = result.get(name,0)
            k += 1
            result[name] = k
    print(result)
    return result

        
        
output = fruits ((
    {'name':'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
    {'name':'mango', 'shape': 'square', 'mass': 150, 'volume': 120}, 
    {'name':'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
    {'name':'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250}))


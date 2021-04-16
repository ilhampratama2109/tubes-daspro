def split_csv(string, delimiter=';'):
    result = []
    data = ''

    for letter in string:
        if letter not in delimiter:
            data += letter

        else:
            if data != '':
                result.append(data)
                data = ''

    if data != '':
        result.append(data)

    return result
    
a = split_csv('adsada;asdas;adsad')
print(a)

            
    
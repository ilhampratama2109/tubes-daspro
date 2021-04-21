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

def remove_if_last_enter(arr):
    last_member = arr[len(arr)-1]
    if last_member[len(last_member)-1] == '\n':
        arr[len(arr)-1] = last_member[:len(last_member)-1]

    return arr

def remove_last_char(string):
    return string[:len(string)-1]

from .helper import split_csv

def remove_last_enter(arr):
    last_member = arr[len(arr)-1]
    arr[len(arr)-1] = last_member[:len(last_member)-1]

    return arr

def remove_last_char(string):
    return string[:len(string)-1]

def get_header(filename):
    
    with open(filename, 'r') as file_data:
        head_data = file_data.readlines()[0]
        head_data = split_csv(head_data)

        head_data = remove_last_enter(head_data)

        return head_data

def is_format_correct(data, filename):
    head = get_header(filename)

    inputan = [*data]
    for i in range(len(inputan)):
        if head[i] != inputan[i]:
            return False

    return True

def create(data, filename):

    string = ''

    # error handling
    if not is_format_correct(data, filename):
        correct_header = get_header(filename)
        raise Exception(f"Header harus: {correct_header}")

    list_key = [*data]
    ls = list(data.values())

    ls = list(map(str, ls))

    

    for key in list_key:
        string += str(data[key])
        string += ';'

    string = remove_last_char(string)
    string += '\n'

    with open(filename, 'a') as user_file:
        user_file.write(string)

def get_all_data(filename):
    f = open(filename, 'r')
    read_line = f.readlines()

    arr = []
    for line in read_line:
        arr.append(line[:len(line)-1])

    arr = arr[1:]

    f.close()
    return arr


def serialize_user(string):
    id, username, nama, alamat, password, role = split_csv(string)

    temp = {
        "id": id,
        "username": username,
        "nama": nama,
        "alamat": alamat,
        "password": password,
        "role": role,
    }

    return temp

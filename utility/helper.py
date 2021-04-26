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


#CONTOH APLIKASI SEARCH(filename,cari) :
#print(search('data/gadget.csv', {"rarity" : "SSS"}))

def search(filename, cari) :
    head = get_header(filename)
    ada = False
    kategori = [*cari][0]
    nama = cari[kategori]
    print(nama,kategori)
    for i in range (len(head)) :        #VALIDISASI APAKAH KATEGORI YANG DIINPUT ADA DI FILENAME
        if head[i] == [kategori][0] :
            indeks = i
            ada = True
    if ada == False : 
        print("Kategori yang ingin dicari tidak ada dalam file")  # Apabila kategori tidak ada dalam filename
        return
    else : 
        bersih = []
        kotor = get_all_to_dictionary(filename) #Apabila kategori ada, dan mencari hal yang diinginkan di kategori
        for i in range (len(kotor)) :
            if kotor[i][kategori] == nama :
                bersih.append(kotor[i])
        return bersih

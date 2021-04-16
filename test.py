from utility import *

filename = 'data/user.csv'

user_dummy = {
    "id": '20',
    "username": 'bebas',
    "nama": "my name is",
    "alamat": "Jl. Ganesha",
    "password": "Mau tau aja",
    "role": "ngadimin"
}

gadget_dummy = {
    "id": "XP",
    "nama": "Bukan Windows",
    "deskripsi": "Turunan ARM",
    "jumlah": 10,
    "rarity": "S",
    "tahun_ditemukan": "1945"
}

consumable_dummy = {
    "id": 9,
    "nama": "mangsut?",
    "deskripsi": "ini berguna",
    "jumlah": "4",
    "rarity": "C"
}

consumable_history_dummy = {
    "id": 5,
    "id_pengambil": 12321313,
    "id_consumable": 390,
    "tanggal_peminjaman": "DD/MM/YEYE",
    "jumlah": 1238

}

gadget_borrow_history = {
    "id": 5,
    "id_peminjam": 12321313,
    "id_gadget": 390,
    "tanggal_peminjaman": "DD/MM/YEYE",
    "jumlah": 1238
}


gadget_return_history = {
    "id": 5,
    "id_peminjam": 12321313,
    "id_gadget": 390,
    "tanggal_pengembalian": "DD/MM/YEYE",
}


create(user_dummy, filename)
head = get_header(filename)
print(f"Data dengan format {head} telah dimasukkan ke dalam {filename}")

filename2 = 'data/gadget.csv'
create(gadget_dummy, filename2)
head2 = get_header(filename2)
print(f"Data dengan format {head2} telah dimasukkan ke dalam {filename2}")

filename3 = 'data/consumable.csv'
create(consumable_dummy, filename3)
head3 = get_header(filename3)
print(f"Data dengan format {head3} telah dimasukkan ke dalam {filename3}")

filename4 = 'data/consumable_history.csv'
create(consumable_history_dummy, filename4)
head4 = get_header(filename4)
print(f"Data dengan format {head4} telah dimasukkan ke dalam {filename4}")

filename5 = 'data/gadget_borrow_history.csv'
create(gadget_borrow_history, filename5)
head5 = get_header(filename5)
print(f"Data dengan format {head5} telah dimasukkan ke dalam {filename5}")

filename6 = 'data/gadget_return_history.csv'
create(gadget_return_history, filename6)
head6 = get_header(filename6)
print(f"Data dengan format {head6} telah dimasukkan ke dalam {filename6}")
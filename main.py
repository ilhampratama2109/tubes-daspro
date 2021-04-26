from autentikasi import *
from saul import *

# untuk authorization
akses = {
    "user": False,
    "admin": False
}

user_filename = 'data/users.csv'
remove_all_empty_lines(user_filename)
#login(user_filename)
#remove_all_empty_lines(user_filename)

query = {
    "username": "lol",
}

tambahitem()
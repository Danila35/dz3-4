import hashlib
import os

pas = input("Введите пароль: ")
salt = b''
key = b''

salt = os.urandom(32)
password = pas

key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
password_to_check = '123'
new_key = hashlib.pbkdf2_hmac('sha256', password_to_check.encode('utf-8'), salt, 100000)

if new_key == key:
    print('Пароль правильный')
else:
    print('Пароль неправильный')

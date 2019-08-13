# /usr/bin/python
import os
import sys
import random
import string
import shutil
import click
import hashlib

app_name = sys.argv[1]
pass_len = sys.argv[2]
with_special_char = sys.argv[3]

def gen_pass(for_length, with_special):
    if with_special:
        password_characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(password_characters) for i in range(for_length))
    else:
        password_characters = string.ascii_letters + string.digits
        return ''.join(random.choice(password_characters) for i in range(for_length))


def who_am_i():
    return os.popen('whoami').read().strip()


def change_file(file_name, new_file_name):
    return os.rename(file_name, new_file_name)


def encrypt_password(u5r_04s5):
    sha_signature = hashlib.sha256(u5r_04s5.encode()).hexdigest()
    return sha_signature


def make_it(app_name, pass_len, with_special):
    p8 = gen_pass(int(pass_len), with_special)
    encrypted = encrypt_password(p8)
    if os.path.isfile(f"/Users/{who_am_i()}/desktop/pass-keep-public.txt"):
        with open(f"/Users/{who_am_i()}/desktop/pass-keep-public.txt", "a+") as f:
            f.write(f'\n{app_name}: {encrypted}')
            f.close()
        with open(f"/Users/{who_am_i()}/desktop/.pass_keep_private.txt", "a+") as g:
            g.write(f'\n{app_name}: {p8}')
            g.close()
    else:
        with open(f"password_keeper.txt", "w+") as f:
            f.write(f'\n{app_name}: {encrypted}')
            f.close()
            shutil.move("password_keeper.txt", f"/Users/{who_am_i()}/desktop/pass-keep-public.txt")
        with open(f"/Users/{who_am_i()}/desktop/.pass_keep_private.txt", "w+") as g:
            g.write(f'\n{app_name}: {p8}')
            g.close()


def get_arguments(app_name, pass_len, with_special_char):
    if with_special_char.lower():
        make_it(app_name, pass_len, with_special_char)
    else:
        make_it(app_name, pass_len, with_special_char)

print(get_arguments(app_name, pass_len, with_special_char))
sys.stdout.flush()



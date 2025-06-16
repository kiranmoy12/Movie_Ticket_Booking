import random
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

def get_otp():
    return random.randint(100000, 999999)


def enc_uname(uname):
    return urlsafe_base64_encode(force_bytes(uname))

def dec_uname(encode_uname):
    return urlsafe_base64_decode(encode_uname)
import random
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

def get_otp():
    return random.randint(100000, 999999)


def enc_uname(uname):
    return urlsafe_base64_encode(force_bytes(uname))

def dec_uname(encode_uname):
    return force_str(urlsafe_base64_decode(encode_uname))

def get_backend_path(user=None):
    from django.contrib.auth import get_backends
    backend = get_backends()[0]
    return f"{backend.__class__.__module__}.{backend.__class__.__name__}"

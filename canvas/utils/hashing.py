import hashlib
import binascii
import os


def hash_password(password: str):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
    pwdhash = hashlib.pbkdf2_hmac("sha512",
                                  password.encode("utf-8"),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    res = (salt + pwdhash).decode("ascii")
    return res


def verify_password(stored_password, provided_password):
    salt = stored_password[:64].encode("ascii")
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac("sha512",
                                  provided_password.encode("utf-8"),
                                  salt,
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return stored_password == pwdhash
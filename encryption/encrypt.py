import base64
from Crypto.Cipher import AES
from Crypto import Random
from encryption.helper import Helper

unpad = lambda s: s[:-ord(s[len(s) - 1:])]
class EncryptService:
    def __init__(self, block_size = 16):
        self.block_size = block_size

    def encrypt(self, raw, password):
        pad = lambda s: s + (self.block_size - len(s) % self.block_size) * chr(self.block_size - len(s) % self.block_size)

        private_key = Helper.get_private_key(password)
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(private_key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode())).decode()

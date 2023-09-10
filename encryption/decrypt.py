import base64
from Crypto.Cipher import AES
from encryption.helper import Helper

class DecryptService:
    @staticmethod
    def decrypt(enc, password):
        unpad = lambda s: s[:-ord(s[len(s) - 1:])]
        private_key = Helper.get_private_key(password)

        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(private_key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(enc[16:]))
        return bytes.decode(decrypted)
 


from Crypto.Protocol.KDF import PBKDF2

class Helper:
    @staticmethod
    def get_private_key(password):
        salt = b"this is a salt"
        kdf = PBKDF2(password, salt, 64, 1000)
        key = kdf[:32]
        return key
 
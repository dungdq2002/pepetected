from stegatool.decode import Decoder
from authenticator.password_service import PasswordService
from encryption.decrypt import DecryptService

if __name__ == "__main__":
    password_stored_file = "sample/user/password.txt"
    encoded_image = "sample/pepe_encoded.png"

    while True:
        print("> Password: ", end = "")
        password = input()
        
        if not PasswordService.validate(password, password_stored_file):
            print("Wrong password!")
            continue
        
        decoder = Decoder()
        encrypted_message = decoder.decode(encoded_image)

        decrypt = DecryptService()
        decrypted_message = decrypt.decrypt(encrypted_message, password)

        print(decrypted_message)

        break

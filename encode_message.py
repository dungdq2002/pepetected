from stegatool.encode import Encoder
from authenticator.password_service import PasswordService
from encryption.encrypt import EncryptService

if __name__ == "__main__":
    encoder = Encoder()

    password = "password1"
    password_stored_file = "sample/user/password.txt"
    cover_image = "sample/pepe.png"
    message = "Welcome to pepetected!"
    output_image = "sample/pepe_encoded.png"

    PasswordService.save_password(password, password_stored_file)

    encrypt = EncryptService()
    encrypted_message = encrypt.encrypt(message, password)

    # Encode image
    # encoder.encode_image(cover_image, encrypted_message, output_image)
    
    # Encode text
    sample_text = "Xin chao"
    encoder.encode_text(sample_text, encrypted_message, output_image)
    
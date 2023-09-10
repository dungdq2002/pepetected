import bcrypt

class PasswordService:
    @staticmethod
    def save_password(password: str, file_path: str):
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        with open(file_path, 'w') as f:
            f.write(hashed.decode())

    @staticmethod
    def validate(input_user: str, file_path: str):
        with open(file_path, 'r') as f:
            hashed_password = f.readline()
            return bcrypt.checkpw(input_user.encode(), hashed_password.encode())
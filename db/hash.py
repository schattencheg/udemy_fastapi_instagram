from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes='argon2', deprecated='auto')


class Hash():
    @staticmethod
    def bcrypt(password: str) -> str:
        return pwd_cxt.hash(password)

    @staticmethod
    def verify(hashed_password: str, plain_password: str):
        return pwd_cxt.verify(plain_password, hashed_password)

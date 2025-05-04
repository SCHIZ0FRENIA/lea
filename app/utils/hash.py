from werkzeug.security import generate_password_hash, check_password_hash


def hash_password(password):
    return generate_password_hash(
        password,
        method='pbkdf2:sha256'
    )

def check_password(hashed, password):
    return check_password_hash(hashed, password)
import bcrypt

password = "super1234*"

hash_password = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
)

print(hash_password.decode("utf-8"))
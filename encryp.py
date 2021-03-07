from cryptography.fernet import Fernet
import base64


chipher = Fernet(base64.b64encode(b'12182192819281928129819839583958'))

with open('quiz.db', 'rb') as file:
    e_file = file.read()

encrypted_file = chipher.encrypt(e_file)

with open('quiz.db'+'.enc', 'wb') as file:
    file.write(encrypted_file)
from cryptography.fernet import Fernet
import base64

key = base64.b64encode(b'12182192819281928129819839583958')
# using the key 
fernet = Fernet(key) 

# opening the encrypted file 
with open('quiz.db.enc', 'rb') as enc_file: 
	encrypted = enc_file.read() 

# decrypting the file 
decrypted = fernet.decrypt(encrypted) 

# opening the file in write mode and 
# writing the decrypted data 
with open('quiz.db', 'wb') as dec_file: 
	dec_file.write(decrypted) 

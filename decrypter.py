import os
import pyaes

# Nome do arquivo criptografado
file_name = "teste.txt.ransomwaretroll"

# Ler o arquivo criptografado
with open(file_name, "rb") as file:
    file_data = file.read()

# Chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# Remover o arquivo criptografado
os.remove(file_name)

# Criar o arquivo descriptografado
with open("teste.txt", "wb") as new_file:
    new_file.write(decrypt_data)

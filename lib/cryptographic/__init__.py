from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def save_key_to_file(key, filename):
  
    key_file=open(filename, "wb")
    
    if("public" in filename):
      binary_data=key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo)
      key_file.write(binary_data)

    if("private" in filename):
      binary_data=key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption())
      key_file.write(binary_data)
  
    key_file.close()

def load_key(filename):
    key_file=open(filename, "rb")
    if("public" in filename):
       key = serialization.load_pem_public_key(
           key_file.read(),
           backend=default_backend()
          )
    if("private" in filename):
       key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    key_file.close()
    return key


def encrypt_file(bytes_data, public_key):
    """
     Generate encrypted data 
   
    Args:
        input_file (string): Path of the file
        public_key (_RSAPublicKey object): object from loaded_public_key
        
    Return:
          bytes :encrypted data of input file
     
    """
  
    chunk_size = (public_key.key_size//8)-11 #bytes 
    final_chunk=b""
    data=bytes_data
    position=0
    
    while True:
      chunk = data[position:position+chunk_size]
      position=position+chunk_size
      if(len(chunk)==0):
          break
      encrypted_chunk=public_key.encrypt(
                    chunk,padding.PKCS1v15())
      final_chunk+=encrypted_chunk
            
    return final_chunk

def decrypt_file(bytes_data,private_key):
    
    chunk_size=private_key.key_size//8 #bytes
    final_chunk=b""
    position=0
    data=bytes_data
  
    while True:
      chunk = data[position:position+chunk_size]
      position=position+chunk_size
      if(len(chunk)==0):
         break
      else:
         decrypted_chunk = private_key.decrypt(
                              chunk,
                              padding.PKCS1v15()
                                )
         final_chunk+=decrypted_chunk
            
    
    return final_chunk

# Generate the key pair
#private_key, public_key = generate_key_pair()

#save_key_to_file(private_key, 'private_key.pem')
#save_key_to_file(public_key, 'public_key.pem')

# Load the keys from files
#loaded_private_key = load_key('private_key.pem')
#loaded_public_key =  load_key('public_key.pem')


# Encrypt and decrypt a file
#input_filename = "006.jpg"
#encrypted_filename = 'encrypted.bin'
#decrypted_filename = 'shshsh.jpg'

#input_file=open(input_filename,"rb")
#input_content=input_file.read()
#encrypted_file=open(encrypted_filename,"wb")
#decrypted_file=open(decrypted_filename,"wb")

#encrypted_content=encrypt_file(input_content, loaded_public_key)
#encrypted_file.write(encrypted_content)

#decrypted_content=decrypt_file(encrypted_content,loaded_private_key)
#decrypted_file.write(decrypted_content)

#input_file.close()
#encrypted_file.close()
#decrypted_file.close()

import hashlib
import binascii

def whash256(get_hash_text):
    
    str1 = hashlib.sha256(bytes.fromhex(get_hash_text))
    #print(str1)
    str2 = str1.digest()
    #print(str2)
   
    str3 = hashlib.sha256(str2)
    str4 = str3.digest()[:4]
    #print(str4)
    #print(str4[0:4], str4[60:64])
    return(binascii.hexlify(str4).decode())



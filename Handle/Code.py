from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import MD5 , SHA1 , SHA256 , SHA512
from Crypto.Cipher import PKCS1_v1_5
import base64
from tkinter import *

def hasing(Input : Entry , Output : Entry , hashmode ):
    plain  = Input.get().encode()
    if(hashmode == 0):
        result = MD5.new(plain)
    elif(hashmode == 1):
        result = SHA1.new(plain)
    elif(hashmode == 2):
        result = SHA256.new(plain)
    elif(hashmode == 3):
        result = SHA512.new(plain)
    Output.delete(0,END)
    Output.insert(0,result.hexdigest())


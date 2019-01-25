import string
import random

Z26 = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
small_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
small_case_dict = {}
for i in Z26:
    small_case_dict[small_case[i]] = i

   
def encryption_function(ptext,key):
    ctext = []
    for i in ptext:
        pnum = (small_case_dict[i] + key ) % 26
        for k,v in small_case_dict.items():
            if v == pnum:
                ctext.append(k)
    return(''.join(ctext)) 

def decryption_function(ctext,key):
    ptext = []
    for i in ctext:
        cnum = (small_case_dict[i] - key) % 26
        for k,v in small_case_dict.items():
            if v == cnum:
                ptext.append(k)
    return(''.join(ptext))

sample_text = 'testingshiftcipher'
key = random.randint(0,25) 
cipher_text = encryption_function(sample_text,key) 
print(sample_text,cipher_text)
plain_text = decryption_function(cipher_text,key)
print(cipher_text,plain_text)






        





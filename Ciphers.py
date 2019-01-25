import string
import random
from copy import deepcopy

Z26 = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
small_case = string.ascii_lowercase
Z26copy = ''.join(random.sample(small_case,k=len(small_case)))
small_case_dict = {}
for i in Z26:
    small_case_dict[small_case[i]] = i
shuffled_dict = {}
for i in range(0,len(small_case)):
    shuffled_dict[small_case[i]] = Z26copy[i]

def shiftcipher_encryption(ptext,key):
    ctext = []
    for i in ptext:
        pnum = (small_case_dict[i] + key ) % 26
        for k,v in small_case_dict.items():
            if v == pnum:
                ctext.append(k)
    return(''.join(ctext)) 

def shiftcipher_decryption(ctext,key):
    ptext = []
    for i in ctext:
        cnum = (small_case_dict[i] - key) % 26
        for k,v in small_case_dict.items():
            if v == cnum:
                ptext.append(k)
    return(''.join(ptext))

def monoalphabet_sub_encryption(ptext):
    ctext = []
    for a in ptext:
        ctext.append(shuffled_dict[a])
    return(''.join(ctext))

def monoalphabet_sub_decryption(ctext):
    ptext = []
    for a in ctext:
        for k,v in shuffled_dict.items():
            if v == a:
                ptext.append(k)
    return(''.join(ptext))
        


sample_text = 'testingcipher'
key = random.randint(0,25) 
# using shift cipher
cipher_text = shiftcipher_encryption(sample_text,key) 
print('encrypted shift cipher',cipher_text)
plain_text = shiftcipher_decryption(cipher_text,key)
print('decrypted shift text  ',plain_text)

# using monoaplhabetic substitution cipher

cipher_text = monoalphabet_sub_encryption(sample_text) 
print('encrypted monoalphabet_sub cipher',cipher_text)
plain_text = monoalphabet_sub_decryption(cipher_text)
print('decrypted monoalphabet_sub text  ',plain_text)






        





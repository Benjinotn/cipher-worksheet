import random


def encrypt(text):   
    encryption_dictionary = create_sub_dict()
    
    encrypted_text = ""
    
    for index in range(0, len(text)):
        if not text[index].isalpha():
            encrypted_text += text[index]
        else:
            encrypted_text += encryption_dictionary[text[index].lower()]  
    
    return encrypted_text
    
  

def create_sub_dict():
    chars = "abcdefghijklmnopqrstuvwxyz"
    sub_dict = {}
    
    
    for char in chars:
        sub_dict[char] = ""
        
    shuffle = ''.join(random.sample(chars,len(chars)))
    
    for key, value in zip(chars, shuffle):
        sub_dict[key] = value
        
    return sub_dict
        
    
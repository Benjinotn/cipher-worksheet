# reduces everything to alphanumeric characters, to make encryption functions as simple as possible

def clean(text):
    clean_text = ""
    
    accepted_characters = "abcdefghijklmnopqrstuvwxyz ,."
    
    for char in text:
        if char.lower() not in accepted_characters:
            continue
        else:
            clean_text += char.lower()
    
    return clean_text

def save(filename, text):
    
    text = clean(text)
    
    name = filename + ".txt"
    textfile = open(name, "w")
    
    textfile.write(text)
    
    textfile.close()
    
def get_task_text(filename):
    
    name = filename + ".txt"
    textfile = open(name , "r")
    
    text = textfile.read()
    
    textfile.close()
    
    return text
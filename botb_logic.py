import random
    
def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
def cipher(text):
    index = 1
    cipher_str = ""
    
    for el in text:
        if index == 1:
            el_buff = el
            index = 2
        elif index == 2:
            cipher_str = cipher_str + str(el)
            cipher_str = cipher_str + str(el_buff)
            index = 1
    if len(text) % 2 != 0:
        cipher_str = cipher_str + str(text[-1])
    return(cipher_str)
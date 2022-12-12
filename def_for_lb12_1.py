def divisor(u_num_1, u_num_2):
    if u_num_1 >= u_num_2:
        ran = u_num_2
    elif u_num_1 < u_num_2:
        
        ran = u_num_1 
        
    i = 1
    divisors = ""   
    
    while i <= ran:
        if i == 1:
            divisors = divisors + str(i)
        elif u_num_1 % i == 0 and u_num_2 % i == 0 and i > 1:
            divisors = divisors + ", " + str(i)
        i += 1
           
    return(divisors)
        
def multiple (u_num):
    multiples = ""
    i = 1
    
    while i < u_num:
        if i == 1:
            multiples = multiples + str(i)
        elif u_num % i == 0 and i > 1:
            multiples = multiples + ", " + str(i)
        i += 1
        
    return(multiples)
    
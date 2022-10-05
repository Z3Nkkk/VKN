inp = input("Веведіть: ")
start_inp = inp

for  x in inp:
    
    count = inp.count(x)
    
    if count >= 1 :
        
        inp = inp.replace( x, '')
        print( f'"{x}"- зустрічається {count} раз(ів)')    
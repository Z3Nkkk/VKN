import lb13_ComplexModule

class Complex1(lb13_ComplexModule.Complex):
    pass
class Complex2(lb13_ComplexModule.Complex):
    pass

def dif(r1, r2, i1, i2):
    return(f'{r1 - r2} + {i1 - i2}i')
def suma(r1, r2, i1, i2):
    return(f'{r1 + r2} + {i1 + i2}i')

comp1 = Complex1(2,4)
comp2 = Complex2(3,2)
print(comp1.ShowComplex())
comp2.SetReal(9)
comp2.SetImaginary(7)
print(comp2.ShowComplex())

print("Різниця комплексних чисел: ",dif(comp1.GetReal(), comp2.GetReal(), comp1.GetImaginary(), comp2.GetImaginary()))
print("Сума комплексних чисел: ",suma(comp1.GetReal(), comp2.GetReal(), comp1.GetImaginary(), comp2.GetImaginary())) 
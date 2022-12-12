class Complex:

    def __init__(self, r_n, i_n):
        self.real = round(float(r_n))
        self.imaginary = round(float(i_n), 2)
    def __del__(self):
        pass
    def SetReal (self, r_n):
        self.real = round(float(r_n), 2)
    def GetReal(self):
        return(self.real)
    def SetImaginary (self, i_n):
        self.imaginary = round(float(i_n), 2)
    def GetImaginary(self):
        return(self.imaginary)    
    def ShowComplex(self):
        return(f'{self.real} + {self.imaginary}i')
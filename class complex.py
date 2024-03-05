class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i= imagpart
        
x = int(input("Ingrese la parte real: "))
im = float(input("Ingrese ka parte imaginaria: "))
p = Complex(x,im)
p.r, p.i
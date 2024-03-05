class Circunferencia:
    def __init__(self, radio):
        self.rad = radio
    def area(self,r):
        return (self.rad*self.rad)*3.14

x = int(input("Digite el area del circulo: "))
p = Circunferencia(x)
print("El radio es: ", p.rad)
print("El area del circulo es: ",p.area(x))
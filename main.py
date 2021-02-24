class Cislo():
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return Cislo(self.value + other.value)
    def __sub__(self, other):
        return Cislo(self.value - other.value)
    def __mul__(self, other):
        return Cislo(self.value * other.value)
    def __truediv__(self, other):
        return Cislo(self.value / other.value)
    def __str__(self):
        return str(self.value)
vysledek = eval("Cislo(5)*Cislo(-2) + Cislo(-7) - (Cislo(3) + Cislo(4)/Cislo(2))")
print(vysledek)
a = 4+3j
a *= 2
print(a)
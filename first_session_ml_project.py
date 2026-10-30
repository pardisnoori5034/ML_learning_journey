class Bmi():
    def __init__(self, fn, ln, by, w, h):
        self.first_name = fn
        self.last_name = ln
        self.birth_year = by
        self.weight = w
        self.height = h

    def age(self):
        curent_year = 2026
        return curent_year - self.birth_year
    
    def bmi(self):
        return self.weight / (self.height ** 2)
    
p1 = Bmi(fn="sara", ln ="moradi", w=54, h= 1.65, by= 2003)

print(p1.first_name)
print(p1.last_name)
print(p1.age())
print(p1.bmi())
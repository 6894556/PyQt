# 클래스 복습

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

sonata = Car("sonata", 2017)
g80 = Car("g80", 2018)

print(sonata.model, sonata.year)
print(g80.model, g80.year)
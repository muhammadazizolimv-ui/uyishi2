
class Xodim:
    def __init__(self, ism, maosh):
        self.ism = ism
        self.maosh = maosh

    def malumot(self):
        print(f"Ism: {self.ism}, Maosh: {self.maosh} so'm")


class Oqituvchi(Xodim):
    def __init__(self, ism, maosh, fan):
        super().__init__(ism, maosh)
        self.fan = fan

    def malumot(self):
        super().malumot()
        print(f"Fani: {self.fan}")


class Farrosh(Xodim):
    def __init__(self, ism, maosh, qavat):
        super().__init__(ism, maosh)
        self.qavat = qavat

    def malumot(self):
        super().malumot()
        print(f"Qavat: {self.qavat}")


oqituvchi = Oqituvchi("Dilnoza", 5000000, "Matematika")
farrosh = Farrosh("Karim", 2500000, 2)

oqituvchi.malumot()
farrosh.malumot()

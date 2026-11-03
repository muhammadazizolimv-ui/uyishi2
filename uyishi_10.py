
class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx


class Savat:
    def __init__(self, nom, mahsulotlar=None):
        self.nom = nom
        if mahsulotlar is None:
            mahsulotlar = []
        self.mahsulotlar = mahsulotlar

    def qosh(self, mahsulot):
        self.mahsulotlar.append(mahsulot)

    def __len__(self):
        return len(self.mahsulotlar)

    def __bool__(self):
        return len(self.mahsulotlar) > 0

    def umumiy_narx(self):
        return sum(m.narx for m in self.mahsulotlar)

    def __str__(self):
        return f"Savat: {self.nom}, mahsulotlar soni: {len(self)}"


bosh_savat = Savat("Bo'sh savat")
savat = Savat("Mening savatim")
savat.qosh(Mahsulot("Non", 5000))
savat.qosh(Mahsulot("Sut", 12000))
savat.qosh(Mahsulot("Tuxum", 18000))

print(savat)

if savat:
    print("Savat bo'sh emas.")
    print("Umumiy narx:", savat.umumiy_narx(), "so'm")

if not bosh_savat:
    print(f"'{bosh_savat.nom}' bo'sh.")

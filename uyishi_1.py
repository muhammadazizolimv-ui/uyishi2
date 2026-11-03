
class Hayvon:
    def __init__(self, nomi, yoshi):
        self.nomi = nomi
        self.yoshi = yoshi

    def ovoz(self):
        print(f"{self.nomi} ovoz chiqarmoqda...")


class It(Hayvon):
    def qoriqlash(self):
        print(f"{self.nomi} uyni qo'riqlayapti.")


class Mushuk(Hayvon):
    def sichqon_tutish(self):
        print(f"{self.nomi} sichqon tutyapti.")


it = It("Rex", 3)
mushuk = Mushuk("Murka", 2)

it.qoriqlash()
mushuk.sichqon_tutish()
it.ovoz()
mushuk.ovoz()

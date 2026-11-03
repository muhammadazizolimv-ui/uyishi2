
class Kitob:
    def __init__(self, nom, muallif, sahifa_soni):
        self.nom = nom
        self.muallif = muallif
        self.sahifa_soni = sahifa_soni

    def malumot(self):
        print(f"Kitob: {self.nom}, Muallif: {self.muallif}, Sahifa: {self.sahifa_soni}")


class ElektronKitob(Kitob):
    def __init__(self, nom, muallif, sahifa_soni, format, fayl_hajmi):
        super().__init__(nom, muallif, sahifa_soni)
        self.format = format
        self.fayl_hajmi = fayl_hajmi

    def malumot(self):
        super().malumot()
        print(f"Format: {self.format}, Fayl hajmi: {self.fayl_hajmi} MB")


kitob = Kitob("O'tgan kunlar", "Abdulla Qodiriy", 380)
e_kitob = ElektronKitob("Mehrobdan chayon", "Abdulla Qodiriy", 320, "pdf", 4.5)

kitob.malumot()
e_kitob.malumot()

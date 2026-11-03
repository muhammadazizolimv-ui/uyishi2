
class Transport:
    def harakatlanish(self):
        print("Transport harakatlanmoqda.")


class Mashina(Transport):
    def harakatlanish(self):
        print("Mashina yo'lda g'ildiraklari bilan yuryapti.")


class Velosiped(Transport):
    def harakatlanish(self):
        print("Velosiped pedal aylantirilib harakatlanyapti.")


class Poyezd(Transport):
    def harakatlanish(self):
        print("Poyezd relslar ustida yuryapti.")


transportlar = [Mashina(), Velosiped(), Poyezd()]
for t in transportlar:
    t.harakatlanish()

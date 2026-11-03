
class Shakl:
    def yuza(self):
        return 0


class Kvadrat(Shakl):
    def __init__(self, tomon):
        self.tomon = tomon

    def yuza(self):
        return self.tomon ** 2


class TogriTortburchak(Shakl):
    def __init__(self, eni, boyi):
        self.eni = eni
        self.boyi = boyi

    def yuza(self):
        return self.eni * self.boyi


shakllar = [Kvadrat(5), TogriTortburchak(4, 6)]
for shakl in shakllar:
    print(f"{type(shakl).__name__} yuzasi: {shakl.yuza()}")


class Inson:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh


class Talaba(Inson):
    def __init__(self, ism, yosh, universitet, baho):
        super().__init__(ism, yosh)
        self.universitet = universitet
        self.baho = baho

    def natija(self):
        if self.baho >= 86:
            return "A'lo"
        elif self.baho >= 71:
            return "Yaxshi"
        elif self.baho >= 56:
            return "Qoniqarli"
        else:
            return "Qoniqarsiz"


talabalar = [
    Talaba("Ali", 19, "TATU", 92),
    Talaba("Vali", 20, "TATU", 75),
    Talaba("Sardor", 21, "TATU", 60),
    Talaba("Jasur", 20, "TATU", 40),
]
for t in talabalar:
    print(f"{t.ism} ({t.universitet}), baho: {t.baho} -> {t.natija()}")

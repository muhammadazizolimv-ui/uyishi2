
class Telefon:
    def __init__(self, brend, model, narx):
        self.brend = brend
        self.model = model
        self.narx = narx

    def __str__(self):
        narx_matn = f"{self.narx:,}".replace(",", " ")
        return f"{self.brend} {self.model} — {narx_matn} so'm"

    def __eq__(self, other):
        if not isinstance(other, Telefon):
            return NotImplemented
        return self.narx == other.narx


t1 = Telefon("Samsung", "A54", 4500000)
t2 = Telefon("Xiaomi", "Redmi Note 12", 4500000)
t3 = Telefon("iPhone", "13", 9000000)

print(t1)
print(t2)
print(t3)
print("t1 == t2:", t1 == t2)
print("t1 == t3:", t1 == t3)

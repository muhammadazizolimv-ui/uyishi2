
class FilmKutubxonasi:
    def __init__(self, nom, filmlar=None):
        self.nom = nom
        if filmlar is None:
            filmlar = []
        self.filmlar = filmlar

    def __len__(self):
        return len(self.filmlar)

    def __getitem__(self, index):
        return self.filmlar[index]

    def __contains__(self, film):
        return film in self.filmlar


kutubxona = FilmKutubxonasi("Mening filmlarim", ["Avatar", "Titanic", "Inception"])
bosh_kutubxona = FilmKutubxonasi("Bo'sh kutubxona")

print("Filmlar soni:", len(kutubxona))
print("0-indeksdagi film:", kutubxona[0])
print("Oxirgi film:", kutubxona[-1])
print("'Titanic' bormi?", "Titanic" in kutubxona)
print("'Matrix' bormi?", "Matrix" in kutubxona)
print("Bo'sh kutubxonada filmlar soni:", len(bosh_kutubxona))

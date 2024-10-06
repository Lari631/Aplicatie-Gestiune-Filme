from domeniu.film import Film
from exceptii.repo_error import RepoError
class RepoFilme:
    def __init__(self):
        self._filme={}

    def __len__(self):
        return len(self._filme)

    def adaugare_film(self,film):
        """
        Functia adauga un film in lista
        """
        id = Film.get_id_film(film)
        if id in self._filme:
            raise RepoError("film existent!")
        self._filme[id] = film

    def stergere_film(self,film):
        """
        Functia sterge un film din lista dupa id
        """
        id = Film.get_id_film(film)
        del self._filme[id]

    def cautare_id(self,id):
        """
        citeste si cauta elementul in dictionar
        :param id_student: entitate de tip student
        :return:
        """
        for key in list(self._filme.keys()):
            if self._filme[key].get_id_film()==id:
                return 1
        return 0

    def cautare_film_id(self, id):
        """
        citeste si cauta dupa id
        :param id: atribut de tip client
        :return:
        """
        if self.cautare_id(id) == 1:
            for key in list(self._filme.keys()):
                if self._filme[key].get_id_film() == id:
                    return self._filme[key]
        else:
            raise RepoError("nu exista id!\n")
            #print("nu exista id!\n")

    def create_lista_id(self):
        """"
        functia creeaza o lista cu idurile tuturor filmelor (pt cautare)
        si o sorteaza (pt cautare binara)
        """
        dictionar = self._filme
        lista = []
        for key in list(self._filme.keys()):
            lista.append(key)
        lista.sort()
        return lista

    def cautare_recursiva(self,lista,id_film):
        """"
        returneaza filmul cu id dat
        """
        #lista = self._filme
        if id_film in lista: return lista[id_film]
        for key, value in lista.items():
            if key == id_film:
                return lista[id_film]
            if isinstance(value,dict):
                self.cautare_recursiva(value, id_film)

    def cautare_recursiva2(self,id_film):
        """"
        sortez lista id-uri
        cautare binara
        """
        lista = self.create_lista_id()
        low = 0
        high = len(lista)
        self.binary_search(lista,id_film,low,high)

    def binary_search(self,array, x, low, high):
        if high >= low:
            mid = low + (high - low)//2
            # If found at mid, then return it
            if array[mid] == x:
                return mid
            # Search the left half
            elif array[mid] > x:
                return self.binary_search(array, x, low, mid-1)
            # Search the right half
            else:
                return self.binary_search(array, x, mid + 1, high)
        else:
            return -1

    def modificare_film(self,film):
        """
        Functia modifica datele unui film din lista
        """
        id_film = film.get_id_film()
        titlu = film.get_titlu()
        gen = film.get_gen()
        descriere = film.get_descriere()
        if self.cautare_id(id_film)==1:
            for key in list(self._filme.keys()):
                if self._filme[key].get_id_film() == id_film:
                    self._filme[key].set_titlu(titlu)
                    self._filme[key].set_gen(gen)
                    self._filme[key].set_descriere(descriere)
        else:
            raise RepoError("nu exista id!\n")
            #print("nu exista id!")

    def get_all(self):
        """
        Functia returneaza toate filmele
        """
        return[self._filme[x] for x in self._filme]
        #return self._filme


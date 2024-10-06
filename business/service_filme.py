from domeniu.film import Film

class ServiceFilme():
    def __init__(self,repo_filme,validare_film):
        self.__repo_filme = repo_filme
        self.__validare_film = validare_film

    def adaugare_film(self,id_film,titlu,gen,descriere):
        film= Film(id_film,titlu,gen,descriere)
        self.__validare_film.validare_film(film)
        self.__repo_filme.adaugare_film(film)

    def stergere_film(self,id_film,titlu,gen,descriere):
        film= Film(id_film,titlu,gen,descriere)
        self.__validare_film.validare_film(film)
        self.__repo_filme.stergere_film(film)

    def cautare_film_id(self,id):
        self.__validare_film.validare_id(id)
        return self.__repo_filme.cautare_film_id(id)

    def cautare_recursiva(self,id_film):
        return self.__repo_filme.cautare_recursiva_file(id_film)

    def modificare_film(self,id_film,titlu,gen,descriere):
        film = Film(id_film,titlu,gen,descriere)
        self.__validare_film.validare_film(film)
        self.__repo_filme.modificare_film(film)

    def lista_iduri(self):
        return self.__repo_filme.file_create_lista_id()

    def get_all_filme(self):
        return self.__repo_filme.get_all()

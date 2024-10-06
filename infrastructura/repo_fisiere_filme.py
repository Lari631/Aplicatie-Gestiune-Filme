from domeniu.film import Film
from infrastructura.repo_filme import RepoFilme
from exceptii.repo_error import RepoError

class FileRepoFilme(RepoFilme):
    def __init__(self,file_path):
        self.__filepath=file_path
        RepoFilme.__init__(self)

    def __len__(self):
        self.__read_all_filme_from_file()
        return RepoFilme.__len__(self)

    def __read_all_filme_from_file(self):
        with open(self.__filepath,"r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_film = int(parts[0])
                    titlu = parts[1]
                    gen = parts[2]
                    descriere = parts[3]
                    film = Film(id_film,titlu,gen,descriere)
                    self._filme[id_film]=film

    def __append_film_to_file(self,film):
        with open(self.__filepath,"a") as f:
            f.write(str(film)+"\n")

    def __write_all_filme_to_file(self):
        with open(self.__filepath,"w") as f:
            for id_film in self._filme:
                f.write(str(self._filme[id_film])+"\n")

    def adaugare_film(self,film):
        self.__read_all_filme_from_file()
        RepoFilme.adaugare_film(self,film)
        self.__append_film_to_file(film)

    def stergere_film(self,film):
        self.__read_all_filme_from_file()
        RepoFilme.stergere_film(self,film)
        self.__write_all_filme_to_file()

    def cautare_film_dupa_id(self,id):
        self.__read_all_filme_from_file()
        if id not in self._filme:
            raise RepoError("nu exista film!")
        return self._filme[id]
        #return RepoClienti.cautare_client_id(self,id)

    def cautare_recursiva_file(self,id_film):
        self.__read_all_filme_from_file()
        #lista = self._filme
        return RepoFilme.cautare_recursiva2(self,id_film)

    def cautare(self,id_film):
        self.__read_all_filme_from_file()
        def cautare_recursiva(lista,id_film):
            pass


    def modificare_film(self,film):
        self.__read_all_filme_from_file()
        id_film = film.get_id_film()
        titlu = film.get_titlu()
        gen = film.get_gen()
        descriere = film.get_descriere()
        if id_film not in self._filme:
            raise RepoError("nu exista film!")
        self._filme[id_film].set_titlu(titlu)
        self._filme[id_film].set_gen(gen)
        self._filme[id_film].set_descriere(descriere)
        self.__write_all_filme_to_file()

    def file_create_lista_id(self):
        lista = RepoFilme.create_lista_id()
        return lista

    def get_all(self):
        self.__read_all_filme_from_file()
        return RepoFilme.get_all(self)





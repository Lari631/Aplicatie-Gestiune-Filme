from domeniu.inchiriere import Inchiriere
from exceptii.repo_error import RepoError
#clasa de legatura
class RepoInchirieri:
    """"
    inchirierile for fi memorate intr-o lista dupa id-ul filmului si al clientului
    """
    def __init__(self):
        self._inchirieri=[]

    def adaugare_inchiriere(self,inchiriere):
        film_de_inchiriat = inchiriere.get_id_film()
        #id = inchiriere.get_id_inchiriere()
        status = 0
        for inchiriere_existenta in self._inchirieri:
            film_deja_inchiriat = inchiriere_existenta.get_id_film()
            if film_de_inchiriat == film_deja_inchiriat:
                status = inchiriere_existenta.get_status()
        if status == 1:
            raise RepoError("film deja inchiriat!")
        else:
            self._inchirieri.append(inchiriere)

    def adaugare_returnare(self,inchiriere):
        film_de_returnat = inchiriere.get_id_film()
        status = 0 # daca nu e in lista de inchirieri, nu a fost inchiriat
        for inchiriere in self._inchirieri:
            if inchiriere.get_id_film() == film_de_returnat:
                status = inchiriere.get_status()
                returnare = inchiriere
        # la finalul for - ului, status = ultimul status (e sau nu nchiriat la momentul actual
        if status == 0:
            raise RepoError("filmul nu este inchiriat!")
        else:
            returnare.set_status(0)
            self._inchirieri.append(returnare)

    def cauta_inchiriere_dupa_id_film(self,id_film):
        for inchiriere in self._inchirieri:
            if inchiriere.get_id_film() == id_film:
            #if inchiriere[1] == id_film:
                return inchiriere
        raise RepoError("film inexistent!")

    def cauta(self,id_film):
        inchirieri = self.get_all()

    def stergere_inchiriere(self,id_film):
        inchiriere = self.cauta_inchiriere_dupa_id_film(id_film)
        self._inchirieri.remove(inchiriere)

    def __len__(self):
        return len(self._inchirieri)

    def get_all(self):
        return self._inchirieri

class FileRepoInchirieri(RepoInchirieri):

    def __init__(self,filepath):
        self.__filepath = filepath
        RepoInchirieri.__init__(self)

    def __read_all_inchirieri_from_file(self):
        with open(self.__filepath,"r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_client = int(parts[0])
                    id_film = int(parts[1])
                    status = int(parts[2])
                    inchiriere = Inchiriere(id_film,id_client,status)
                    self._inchirieri.append(inchiriere)

    def __append_to_file(self,inchiriere):
        with open(self.__filepath,"a") as f:
            f.write(str(inchiriere)+"\n")

    def __write_all_inchirieri_to_file(self):
        with open(self.__filepath,"w") as f:
            for inchiriere in self._inchirieri:
                f.write(str(inchiriere)+"\n")

    def adauga_inchiriere(self,inchiriere):
        self.__read_all_inchirieri_from_file()
        RepoInchirieri.adaugare_inchiriere(self,inchiriere)
        self.__append_to_file(inchiriere)

    def stergere_inchiriere(self,id_film):
        self.__read_all_inchirieri_from_file()
        RepoInchirieri.stergere_inchiriere(self,id_film)
        self.__write_all_inchirieri_to_file()

    def adauga_returnare(self,inchiriere):
        self.__read_all_inchirieri_from_file()
        RepoInchirieri.adaugare_returnare(self,inchiriere)
        self.__append_to_file(inchiriere)

    def get_id_client(self,inchiriere):
        id = Inchiriere.get_id_client(inchiriere)
        return id

    def get_all_clienti(self):
        self.__read_all_inchirieri_from_file()
        return RepoInchirieri.get_all(self)

    def get_all_inchirieri(self):
        self.__read_all_inchirieri_from_file()
        return self._inchirieri

#merge append?
#merge la write fara id?


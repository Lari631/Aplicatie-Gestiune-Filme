from domeniu.client import Client
from exceptii.repo_error import RepoError
class RepoClienti:
    def __init__(self):
        self._clienti={}

    def __len__(self):
        return len(self._clienti)

    def adaugare_client(self,client):
        """
        Functia adauga un client in lista
        """
        id = Client.get_id_client(client)
        if id in self._clienti:
            raise RepoError("client existent!")
        self._clienti[id]=client

    def stergere_client(self,client):
        """
        Functia sterge un client din lista
        """
        id = Client.get_id_client(client)
        del self._clienti[id]

    def cautare_id(self,id):
        """
        citeste si cauta elementul in lista
        :param id_student: entitate de tip student
        :return:
        """
        for key in list(self._clienti.keys()):
            if self._clienti[key].get_id_client()==id:
                return 1
        return 0


    def cautare_client_id(self, id):
        """
        citeste si cauta dupa id
        :param id: atribut de tip client
        :return
        """
        if self.cautare_id(id) == 1:
            for key in list(self._clienti.keys()):
                if self._clienti[key].get_id_client() == id:
                    return self._clienti[key]
        else:
            raise RepoError("nu exista id!\n")

    def modificare_client(self,client):
        """
        Functia modifica datele unui client din lista
        """
        id_client = client.get_id_client()
        nume = client.get_nume()
        cnp = client.get_cnp()
        if self.cautare_id(id_client)==1:
            for key in list(self._clienti.keys()):
                if self._clienti[key].get_id_client() == id_client:
                    self._clienti[key].set_nume(nume)
                    self._clienti[key].set_cnp(cnp)
        else:
            #raise RepoError("nu exista id!\n")
            print("nu exista id!")

    def get_all(self):
        return[self._clienti[x] for x in self._clienti]

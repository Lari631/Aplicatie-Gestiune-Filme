from domeniu.client import Client
from infrastructura.repo_clienti import RepoClienti
from exceptii.repo_error import RepoError
class FileRepoClienti(RepoClienti):
    def __init__(self,file_path):
        self.__filepath = file_path
        RepoClienti.__init__(self)
        self._clienti={}

    def __len__(self):
        self.__read_all_clienti_from_file()
        return RepoClienti.__len__(self)

    def __read_all_clienti_from_file(self):
        """"
        citeste clientii din fisier si formeaza dictionarul de clienti
        """
        with open(self.__filepath,"r") as f:
            #self._clienti.clear()
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line !="":
                    parts = line.split(",")
                    id_client = int(parts[0])
                    nume = parts[1]
                    cnp = int(parts[2])
                    client = Client(id_client,nume,cnp)
                    self._clienti[id_client]=client

    def __append_client_to_file(self,client):
        with open(self.__filepath,"a") as f:
            f.write(str(client)+"\n")

    def __write_all_clienti_to_file(self):
        with open(self.__filepath,"w") as f:
            for id_client in self._clienti:
                f.write(str(self._clienti[id_client])+"\n")

    def adaugare_client(self,client):
        self.__read_all_clienti_from_file()
        RepoClienti.adaugare_client(self,client)
        self.__append_client_to_file(client)

    def stergere_client(self,client):
        self.__read_all_clienti_from_file()
        RepoClienti.stergere_client(self,client)
        self.__write_all_clienti_to_file()

    def cautare_client_dupa_id(self,id):
        self.__read_all_clienti_from_file()
        if id not in self._clienti:
            raise RepoError("nu exista client!")
        return self._clienti[id]
        #return RepoClienti.cautare_client_id(self,id)

    def cautare_recursiva(self,id_client):
        """"
        functia cauta un client in lista de clienti dupa id
        returneaza : clientul, daca exista
        None, caz contratr
        """
        self.__read_all_clienti_from_file()
        dictionar = self._clienti
        lista = list(dictionar.keys())

        def cautare(lista,id_client):
            if lista[0]==id_client:
                return self._clienti[id_client]
            return cautare(lista[1:],id_client)

        cautare(lista,id_client)

    def modificare_client(self,client):
        self.__read_all_clienti_from_file()
        id_client = client.get_id_client()
        nume= client.get_nume()
        cnp = client.get_cnp()
        if id_client not in self._clienti:
            raise RepoError("nu exista client!")
        self._clienti[id_client].set_nume(nume)
        self._clienti[id_client].set_cnp(cnp)
        self.__write_all_clienti_to_file()

    def get_all_clienti(self):
        self.__read_all_clienti_from_file()
        return RepoClienti.get_all(self)

"""
    def read_all_from_file_clienti(self):
        with open(self.__filepath,"r") as f:
            line = f.readline().strip()
            while line!="":
                line = line.split(" ")
                client = Client(line[0],line[1],line[2])
                self.repo.adauare_client(client)

                line = f.readline().strip()

    def load_clienti(self,i):
        return (self.repo._clienti[i].get_id_client() + " " + self.repo._clienti[i].get_nume() + " " + self.repo._clienti[i].get_cnp())

    def write_all_to_file_clienti(self):
        file = open(self.__filepath,"w")
        for i in self.repo._clienti:
            string = self.load_clienti(i)
            file.write(string + "\n")
        file.close()
"""

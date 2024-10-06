from domeniu.client import Client
from domeniu.film import Film
from validare.validare_client import ValidareClient
from validare.validare_film import ValidareFilm
from exceptii.valid_error import ValidationError
from infrastructura.repo_clienti import RepoClienti
from exceptii.repo_error import RepoError
from infrastructura.repo_fisiere_clienti import FileRepoClienti
from business.service_clienti import ServiceClienti

class Teste:
    def __init__(self):
        pass

    def __ruleaza_teste_domeniu(self):
        #print("se incep testele pentru domeniu...")
        self.__id_client= 100
        self.__nume= "Maria"
        self.__cnp = 6050913349028
        self.__client =Client(self.__id_client,self.__nume,self.__cnp)
        assert self.__client.get_id_client() == self.__id_client
        assert self.__client.get_nume() == self.__nume
        assert self.__client.get_cnp()==self.__cnp
        self.__alt_nume = "Elena"
        self.__alt_cnp = 6050913349028
        self.__alt_client_acelasi_id = Client(self.__id_client,self.__alt_nume,self.__alt_cnp)
        assert self.__client == self.__alt_client_acelasi_id
        assert Client.__eq__(self.__client,self.__alt_client_acelasi_id)
        assert self.__client.__eq__(self.__alt_client_acelasi_id)

        self.__id_film=1
        self.__titlu= "StarWars"
        self.__gen = "sf"
        self.__descriere = "frumos"
        self.__film= Film(self.__id_film,self.__titlu,self.__gen,self.__descriere)
        assert self.__film.get_id_film() == self.__id_film
        assert self.__film.get_titlu() == self.__titlu
        assert self.__film.get_gen() == self.__gen
        assert self.__film.get_descriere() == self.__descriere

        #print("teste domeniu rulate cu succes!")

    def __ruleaza_teste_validare(self):
        #print("se incep testele de validare...")
        self.__validator_client = ValidareClient()
        self.__validator_client.validare_client(self.__client)
        self.__id_invalid = -287
        self.__nume_invalid = ""
        self.__cnp_invalid = -9827
        self.__client_invalid= Client(self.__id_invalid,self.__nume_invalid,self.__cnp_invalid)
        try:
            self.__validator_client.validare_client(self.__client_invalid)
            assert False
        except ValidationError as ve:
            assert str(ve)=="id invalid!\nnume invalid!\ncnp invalid!\n"

        #print("teste validare rulate cu succes!")

    def __goleste_fisier(self,file_path):
        #f = open(file_path,"v")
        with open(file_path,"w") as f:
            f.write("")
        #f.close()

    def __ruleaza_teste_adaugare_client_repo(self):
        file_path="C:\\Users\\A\\PycharmProjects\\Lab7_fisiere\\teste\\teste_clienti.txt"
        self.__goleste_fisier(file_path)
        self.__repo_clienti = RepoClienti()
        assert len(self.__repo_clienti)== 0
        self.__repo_clienti.adaugare_client(self.__client)
        id = self.__id_client
        client_gasit = self.__repo_clienti.cautare_client_id(id)
        assert client_gasit == self.__client
        assert client_gasit.get_nume()==self.__client.get_nume()
        assert client_gasit.get_cnp()== self.__client.get_cnp()
        assert len(self.__repo_clienti)==1
        try:
            self.__repo_clienti.adaugare_client(self.__alt_client_acelasi_id)
            assert False
        except RepoError as ex:
            assert str(ex)=="client existent!"

    def run_all_tests(self):
        print("se incep testele...")
        self.__ruleaza_teste_domeniu()
        self.__ruleaza_teste_validare()
        self.__ruleaza_teste_adaugare_client_repo()
        #self.__ruleaza_teste_adaugare_client_service()
        print("teste finalizate cu succes!")

""""
    def __ruleaza_teste_adaugare_client_service(self):
        file_path="C:\\Users\\A\\PycharmProjects\\Lab7_fisiere\\teste\\teste_clienti.txt"
        self.__goleste_fisier(file_path)
        self.__repo_clienti = RepoClienti()
        self.__service_clienti= ServiceClienti(self.__repo_clienti,self.__validator_client)
        self.__service_clienti.adaugare_client(self.__id_client,self.__nume,self.__cnp)
        client_gasit = self.__service_clienti.cautare_client_id(self.__id_client)
        assert client_gasit == self.__client
        assert client_gasit.get_nume()==self.__client.get_nume()
        assert client_gasit.get_cnp()== self.__client.get_cnp()
        assert len(self.__repo_clienti)==1
        try:
            self.__service_clienti.adaugare_client(self.__alt_client_acelasi_id.get_id_client(),self.__alt_client_acelasi_id.get_nume(),self.__alt_client_acelasi_id.get_cnp())
            assert False
        except RepoError as ex:
            assert str(ex)=="client existent!"
        try:
            self.__service_clienti.adaugare_client(self.__id_invalid,self.__nume_invalid,self.__cnp_invalid)
            assert False
        except ValidationError as ex:
            assert str(ex)=="id invalid!\nnume invalid!\ncnp invalid!\n"
"""

teste = Teste()
teste.run_all_tests()

#def __ruleaza_teste_get_all_clienti  - repo si service, pe la 2;20

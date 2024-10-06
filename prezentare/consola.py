import validare.validare_client
from infrastructura import repo_clienti
from infrastructura import repo_filme
from exceptii.ui_error import UIError
from exceptii.valid_error import ValidationError
from exceptii.repo_error import RepoError
from business import *

class Consola():

    def __init__(self,srv_filme,srv_clienti,srv_inchirieri):
        self.__srv_filme = srv_filme
        self.__srv_clienti = srv_clienti
        self.__srv_inchirieri = srv_inchirieri
        self.__comenzi = {
            "add_client":self.__ui_add_client,
            "print_clienti":self.__ui_print_clienti,
            "print_nr_clienti":self.__ui_print_nr_clienti,
            "del_client":self.__ui_delete_client,
            "cauta_client":self.__ui_cauta_client,
            "modifica_client":self.__ui_modifica_client,
            "add_film":self.__ui_add_film,
            "del_film":self.__ui_delete_film,
            "print_filme":self.__ui_print_filme,
            "cauta_film":self.__ui_cauta_film,
            "modifica_film":self.__ui_modifica_film,
            "inchiriaza_film":self.__ui_inchiriaza_film,
            "returneaza_film":self.__ui_returneaza_film,
            "print_inchirieri":self.__ui_afiseaza_inchirieri,
            "print_nr_filme_inchiriate":self.__ui_nr_filme_inchiriate,
            "ordonare_dupa_nr_filme":self.__ui_ordoneaza_dupa_nr_filme,
            "ordonare_dupa_nume":self.__ui_ordoneaza_dupa_nume,
            "raport_filme":self.__ui_raport_filme,
            "top_clienti":self.__ui_top_clienti,
            "top_filme":self.__ui_top_filme,
            "random":self.__ui_random,
            "lista_iduri":self.__ui_a,
            "nu":self.__ui_numar_recursiv,
            "cautare_recursiva":self.__ui_cautare_recursiva_client,
            "numar_filme_recursiv":self.__ui_numar_filme_recursiv,
            "print_inchirieri_recursiv":self.__ui_print_inchirieri_recursiv,
            "o":self.__ui_ordonare_insertion_dupa_nr_filme
        }

    def __ui_ordonare_insertion_dupa_nr_filme(self,params):
        raport = self.__srv_inchirieri.insertion_dupa_nr_filme()
        for element in raport:
            print(element)

    def __ui_print_inchirieri_recursiv(self,params):
        inchirieri = self.__srv_inchirieri.get_all_inchirieri()
        def printeaza(inchirieri):
            print(inchirieri[0])
            if len(inchirieri[1:])!=0:
                printeaza(inchirieri[1:])
            else:
                return
        printeaza(inchirieri)

    def __ui_numar_filme_recursiv(self,params):
        if len(params)!=1:
            raise UIError("nr params invalid!")
        id = int(params[0])
        nr = self.__srv_inchirieri.nr_filme_recursiv(id)
        print("clientul a inchiriat",nr,"filme")
        #print(nr)
        #print("filme")

    def __ui_cautare_recursiva_client(self,params):
        if len(params)!=1:
            raise UIError("nr params invalid!")
        id = int(params[0])
        client = self.__srv_clienti.cautare_client_id(id)
        if client:
            print("client gasit!")
            print (client)
        else:
            print("client inexistent!")

    def __ui_numar_recursiv(self,params):
        lista = self.__srv_inchirieri.get_all_inchirieri()
        numar = self.__srv_inchirieri.nr_recursiv()
        print(numar)

    def __ui_a(self,params):
        lista = self.__srv_filme.lista_iduri
        for id in lista:
            print(lista)

    def __ui_cauta_film(self,params):
        if len(params)==1:
            id=int(params[0])
            film_gasit = self.__srv_filme.cautare_recursiva(id)
            if film_gasit != None:
                print("Film gasit!")
                print(film_gasit)
            else:
                print("nu exista film")
        else:
            raise UIError("nr params invalid")

    def __ui_print_nr_clienti(self,params):
        nr = self.__srv_clienti.get_nr_clienti()
        print(nr)

    def __ui_top_filme(self,params):
        lista = self.__srv_inchirieri.raport_filme()
        for element in lista:
            print(element)

    def __ui_random(self,params):
        if len(params) != 1:
            raise UIError("nr params invalid")
        numar = int(params[0])
        self.__srv_clienti.random_client(numar)
        print("generare facuta cu succes")

    def __ui_add_film(self,params):
        if len(params)!=4:
            raise UIError("nr params invalid")
        try:
            id_film=int(params[0])
            titlu=params[1]
            gen=params[2]
            descriere=params[3]
            self.__srv_filme.adaugare_film(id_film,titlu,gen,descriere)
        except ValueError:
            raise UIError("valoare numerica invalida!")
            #print("valoare numerica invalida")

    def __ui_delete_film(self,params):
        if len(params)!=4:
            raise UIError("nr params invalid")
        try:
            id_film=int(params[0])
            titlu=params[1]
            gen=params[2]
            descriere=params[3]
            self.__srv_filme.stergere_film(id_film,titlu,gen,descriere)
        except ValueError:
            raise UIError("valoare numerica invalida!")
            #print("valoare numerica invalida")

    def __ui_print_filme(self,params):
        filme = self.__srv_filme.get_all_filme()
        for film in filme:
            print(film)

    def __ui_modifica_film(self,params):
        if len(params)!=4:
            raise UIError("nr params invalid")
        try:
            id_film = int(params[0])
            titlu = params[1]
            gen = params[2]
            descriere = params[3]
            self.__srv_filme.modificare_film(id_film,titlu,gen,descriere)
        except ValueError:
            raise UIError("valoare numerica invalida")
            #print("valoare numerica invalida")

    def __ui_inchiriaza_film(self,params):
        """
                imparte parametrul params in id_client,id_film
                apeleaza service inchiriere
                :return: value error daca nu sunt de tipul precizat si mesaj sugestiv
            """
        if len(params)!=2:
            raise UIError("nr params invalid")
        try:
            id_film=int(params[0])
            id_client=int(params[1])
            self.__srv_inchirieri.inchiriere_film(id_film,id_client)
            print(f'filmul {id_film} a fost inchiriat cu succes de clientul {id_client}')
        except ValueError:
            raise UIError("parametri invalizi!")

    def __ui_returneaza_film(self,params):
        if len(params)!=2:
            raise UIError("nr params invalid")
        try:
            id_film = int(params[0])
            id_client = int(params[1])
            self.__srv_inchirieri.returnare_film(id_film,id_client)
            print(f'filmul {id_film} a fost returnat cu succes de clientul {id_client}')
        except ValueError:
            raise UIError("parametri invalizi!")

    def __ui_afiseaza_inchirieri(self,params):
        #nr=params[0]
        inchirieri = self.__srv_inchirieri.get_all_inchirieri()
        for inchiriere in inchirieri:
            print(inchiriere)
        if not inchirieri:
            print("nu exista inchirieri")

    def __ui_nr_filme_inchiriate(self,params):
        if len(params)!=1:
            raise UIError("nr params invalid!")
        try:
            id_client = int(params[0])
        except ValueError:
            raise UIError("parametri invalizi!")
        nr = self.__srv_inchirieri.nr_filme_inchiriate(id_client)
        if nr == 0:
            print("clientul nu a inchiriat nici un film")
            return
        else:
            print("clientul a inchiriat ",nr," filme")

    def __ui_ordoneaza_dupa_nr_filme(self,params):
        #nr=params[0]
        #lista = self.__srv_inchirieri.ordonare_dupa_nr_filme()
        lista = self.__srv_inchirieri.ordonare_insertion_dupa_nr_filme()
        for element in lista:
            print (element)

    def __ui_ordoneaza_dupa_nume(self,params):
        #lista = self.__srv_inchirieri.ordonare_dupa_nume()
        lista = self.__srv_inchirieri.ordonare_comb_dupa_nume()
        for client in lista:
            print(client)

    def __ui_raport_filme(self,params):
        lista = self.__srv_inchirieri.raport_filme()
        for film in lista:
            print(film)

    def __ui_top_clienti(self,params):
        lista = self.__srv_inchirieri.top_clienti()
        for element in lista:
            print(element)

    def __ui_add_client(self,params):
        if len(params)!= 3:
            raise UIError("nr params invalid")
        try:
            id_client = int(params[0])
            nume = params[1]
            cnp = int(params[2])
            self.__srv_clienti.adaugare_client(id_client,nume,cnp)
        except ValueError:
            raise RepoError("Valoare numerica invalida!\n")

    def __ui_delete_client(self,params):
        if len(params)!= 3:
            raise UIError("nr params invalid")
        try:
            id_client = int(params[0])
            nume = params[1]
            cnp = int(params[2])
            self.__srv_clienti.stergere_client(id_client,nume,cnp)
        except ValueError:
            raise UIError("valoare numerica invalida!\n")
            #print("valoare numerica invalida")

    def __ui_print_clienti(self,params):
        clienti = self.__srv_clienti.get_all_clienti()
        for client in clienti:
            print(client)

    def __ui_cauta_client(self,params):
        if len(params)==1:
            id=int(params[0])
            client_gasit = self.__srv_clienti.cautare_client_id(id)
            if client_gasit:
                print("Client gasit!")
            print(client_gasit)
        else:
            raise UIError("nr params invalid")

    def __ui_modifica_client(self,params):
        if len(params)!=3:
            raise UIError("nr params invalid")
        try:
            id_client = int(params[0])
            nume = params[1]
            cnp = int(params[2])
            self.__srv_clienti.modificare_client(id_client,nume,cnp)
        except ValueError:
            raise UIError("valoare numerica invalida")
            #print("valoare numerica invalida")

    def run(self):
        while True:
            cmd = input(">>>")
            cmd = cmd.strip()
            if cmd == "":
                continue
            if cmd == "exit":
                return
            parts = cmd.split()
            cmd_name = parts[0]
            params = parts[1:]
            if not params:
                params = 0
            if cmd_name in self.__comenzi:
                try:
                    self.__comenzi[cmd_name](params)
                except ValidationError as ve:
                    print(f"Validation Error:{ve}")
                except RepoError as re:
                    print(f"Repo Error:{re}")
                except UIError as ui:
                    print(f"UI Error:{ui}")
            else:
                print("comanda invalida!")

# !!!!!!!!ana si sergiu

#fa altcumva sa nu afiseze film inchiriat cu succes cand nu trebuie
# cand adaug student, printez student

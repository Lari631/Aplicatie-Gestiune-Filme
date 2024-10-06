from domeniu.inchiriere import Inchiriere
from domeniu.client import Client
from domeniu.dtos import RaportClient
from domeniu.dtos import RaportFilm
from sortari.sortari import Sort

class ServiceInchirieri():
    def __init__(self,repo_filme,repo_clienti,repo_inchirieri):
        self.__repo_clienti = repo_clienti
        self.__repo_filme = repo_filme
        self.__repo_inchirieri = repo_inchirieri
       # self.__validator_inchiriere = validator_inchiriere

    def inchiriere_film(self,id_film,id_client):
        film = self.__repo_filme.cautare_film_dupa_id(id_film)
        client = self.__repo_clienti.cautare_client_dupa_id(id_client)
        status = 1
        inchiriere = Inchiriere(id_film,id_client,status)
        self.__repo_inchirieri.adauga_inchiriere(inchiriere)

    def returnare_film(self,id_film,id_client):
        #self.__repo_inchirieri.stergere_inchiriere(id_film)
        film = self.__repo_filme.cautare_film_dupa_id(id_film)
        client = self.__repo_clienti.cautare_client_dupa_id(id_client)
        status = 0
        inchiriere= Inchiriere(id_film,id_client,status)
        self.__repo_inchirieri.adauga_returnare(inchiriere)

    def inchirieri(self):
        inchirieri = self.__repo_inchirieri.get_all_inchirieri()
        return inchirieri

    def nr_filme_inchiriate(self,id_client):
        """"
        functia returneaza numarul de filme inchiriate de un client
        """
        inchirieri = self.__repo_inchirieri.get_all_inchirieri()
        nr=0
        for inchiriere in inchirieri:
            id = inchiriere.get_id_client()
            status = inchiriere.get_status()
            if id == id_client and status==1:
                    nr = nr+1
        return nr

    def nr_filme_recursiv(self,id_client):
        inchirieri = self.__repo_inchirieri.get_all_inchirieri()

        def nr_filme(inchirieri,id_client):
            inchiriere = inchirieri[0]
            if len(inchirieri[1:])==0:
                return 0
            else:
                if inchiriere.get_id_client()==id_client and inchiriere.get_status()==1:
                    return 1+nr_filme(inchirieri[1:],id_client)
                else:
                    return 0+nr_filme(inchirieri[1:],id_client)

        nr = nr_filme(inchirieri,id_client)
        return nr

    def lista_dupa_nr_filme(self):
        """"
        functia returneaza o lista cu id_client si nr_filme_inchiriate de client
        """
        inchirieri = self.__repo_inchirieri.get_all_inchirieri()
        lista={}
        for inchiriere in inchirieri:
            id_client = inchiriere.get_id_client()
            status = inchiriere.get_status()
            if id_client not in lista:
                lista[id_client] = 1
            elif status == 1:
                lista[id_client]+=1
        lista_sortata = dict(sorted(lista.items(),key = lambda x:x[1],reverse=True))
        list_raport=[]
        for element in lista_sortata:
            #client = element
            nume = self.__repo_clienti.cautare_client_dupa_id(element).get_nume()
            client_raport = RaportClient(element,nume,lista_sortata[element])
            list_raport.append(client_raport)
        return list_raport

    def lista_raport(self):
        """"
        functia returneaza dictionar cu : key = id_client, value = nr_filme_inchiriate
        """
        inchirieri = self.__repo_inchirieri.get_all_inchirieri()
        lista={}
        for inchiriere in inchirieri:
            id_client = inchiriere.get_id_client()
            status = inchiriere.get_status()
            if id_client not in lista:
                lista[id_client] = 1
            elif status == 1:
                lista[id_client]+=1
        return lista

    def nr_de_filme_inchiriate(self,id_client):
        lista = self.lista_raport()
        return lista[id_client]

    def nume(self,client):
        return client.get_nume()

    def nr(self,inchiriere):
        id_client = inchiriere.get_id_client()
        return self.nr_de_filme_inchiriate(id_client)

    def ordonare_dupa_nume(self):
        """"
        functia returneaza lista clientilor ordonata alfabetic dupa nume
        """
        clienti = self.__repo_clienti.get_all_clienti()
        lista=[]
        for client in clienti:
            nume = client.get_nume()
            #nume = self.__repo_clienti.cautare_client_dupa_id(id_client).get_nume()
            #client_raport = RaportNume(id_client,nume)
            lista.append(nume)
        lista.sort()
        #generic_insertion(lista,reversed=True,key=nume)
        return lista

    def top_clienti(self):
        """"
        functia returneaza o lista cu top 30% clienti dupa nr filme inchiriate
        """
        top = []
        lista = self.lista_raport()
        nr = len(lista)*30//100
        i=0
        while i <= nr :
            top.append(lista[i])
            i=i+1
        return top

    def raport_filme(self):
        dictionar = {} # key: id_film, value: nr inchirieri
        inchirieri = self.__repo_inchirieri.get_all_inchirieri()
        for inchiriere in inchirieri:
            if inchiriere.get_status()==1:
                id_film = inchiriere.get_id_film()
                if id_film in dictionar.keys():
                    dictionar[id_film] += 1
                else:
                    dictionar[id_film] = 1
        dictionar_sortat = dict(sorted(dictionar.items(),key = lambda x:x[1],reverse=True))
        #dictionar_sortat=generic_insertion(dictionar,reversed=True,key=nr)
        list_raport=[]
        for element in dictionar_sortat:
            id_film = element
            titlu = self.__repo_filme.cautare_film_dupa_id(id_film).get_titlu()
            film_raport = RaportFilm(id_film,titlu,dictionar_sortat[id_film])
            list_raport.append(film_raport)
        return list_raport

    def get_all_inchirieri(self):
        return self.__repo_inchirieri.get_all_inchirieri()

    def combsort(self,arr, key=None, reverse=False):
        def getNextGap(gap):
            # factor of 1.3
            gap = (gap * 10) // 13
            return max(1, gap)

        n = len(arr)
        gap = n
        swapped = True
        while gap != 1 or swapped:
            gap = getNextGap(gap)
            swapped = False
            for i in range(0, n - gap):
                compare_element_1 = arr[i]
                compare_element_2 = arr[i + gap]
                if key:
                    compare_element_1 = key(arr[i])
                    compare_element_2 = key(arr[i + gap])
                comparison_result = compare_element_1 > compare_element_2 if not reverse else compare_element_1 < compare_element_2
                if comparison_result:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    swapped = True
        return arr

    def ordonare_comb_dupa_nume(self):
        clienti = self.__repo_clienti.get_all_clienti()
        lista_ordonata = self.combsort(clienti,key=self.nume)
        return lista_ordonata

    def insertionsort(self,arr, key=None, reverse=False):
        n = len(arr)
        for i in range(1, n):
            current_element = arr[i]
            key_value = key(current_element) if key else current_element
            j = i - 1
            while j >= 0 and (key_value > key(arr[j]) if key else key_value > arr[j]) if reverse else (key_value < key(arr[j]) if key else key_value < arr[j]):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = current_element
        return arr

    def cmp(self,client1_raport,client2_raport):
        if client1_raport.get_nr() < client2_raport.get_nr():
            return -1
        if client1_raport.get_nume() == client2_raport.get_nume():
            if client1_raport.get_nume() < client2_raport.get_nume():
                return -1
            return 1
        return 1
# cu cmp
    def insertionsort1(self,arr, key=None, reverse=False):
        n = len(arr)
        for i in range(1, n):
            current_element = arr[i]
            key_value = key(current_element) if key else current_element
            j = i - 1
            ok=-1
            if reverse:
                while j >= 0 and ok==-1:
                    if key:
                            el=key(arr[j])
                    else:
                            el=arr[j]
                    ok = self.cmp(key_value,el)
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = current_element
            else:
                while j >= 0 and ok==1:
                    if key:
                            el=key(arr[j])
                    else:
                            el=arr[j]
                    ok = self.cmp(key_value,el)
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = current_element
        return arr

    def numar_filme(self,id_client):
        lista_raport = self.lista_raport()
        return lista_raport[id_client]

    def numaar(self,element):
        return element.get_nr()

    def ordonare_insertion_dupa_nr_filme(self):
        inchirieri = self.__repo_inchirieri.get_all_inchirieri()
        #lista_ordonata = self.insertionsort(inchirieri,key=self.numar)
        list_raport = self.lista_dupa_nr_filme()
        lista_ordonata = self.insertionsort1(list_raport,reverse=True)
        return lista_ordonata



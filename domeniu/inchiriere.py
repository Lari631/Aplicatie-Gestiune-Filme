from domeniu.client import Client
from domeniu.film import Film

class Inchiriere:
    def __init__(self,id_film,id_client,status):
        self.__id_film=id_film
        self.__id_client=id_client
        self.__status = status # inhiriere/returnare : 1=inchiriat, 0=returnat

    def get_id_client(self):
        return self.__id_client

    def get_id_film(self):
        return self.__id_film

    def get_status(self):
        return self.__status

    def set_id_client(self,id_client):
        self.__id_client=id_client

    def set_id_film(self,id_film):
        self.__id_film=id_film

    def set_status(self,status_nou):
        self.__status = status_nou

    def __eq__(self,other):
        return self.__id_film==other.__id_film

    def __str__(self):
        return f"{self.__id_client},{self.__id_film},{self.__status}"



#vezi daca nu trb get set pt client si film  pe aici

    #def inchiriere_set_id_client(self):
     #trebuie setter?



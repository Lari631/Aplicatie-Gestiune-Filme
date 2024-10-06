class RaportClient:
    def __init__(self,id_client,nume,nr):
        self.__id_client = id_client
        self.__nume= nume
        self.__nr=nr

    def get_nume(self):
        return self.__nume

    def get_nr(self):
        return self.__nr

    def __str__(self):
        return f"{self.__nume},{self.__nr}"

class RaportNume:
    def __init__(self,id_client,nume):
        self.__id_client = id_client
        self.__nume = nume

    def get_nume(self):
        return self.__nume

    def __str__(self):
        return f"{self.__nume}"

class RaportFilm:
    def __init__(self,id_film,titlu,nr):
        self.__id_film = id_film
        self.__nr = nr
        self.__titlu = titlu

    def __str__(self):
        return f"{self.__titlu},{self.__nr}"



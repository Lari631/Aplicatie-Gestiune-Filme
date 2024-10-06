class Client:
    def __init__(self,id_client,nume,cnp):
        self.__id_client = id_client
        self.__nume = nume
        self.__cnp = cnp

    def get_id_client(self):
        return self.__id_client

    def get_nume(self):
        return self.__nume

    def get_cnp(self):
        return self.__cnp

    def set_nume(self,nume_nou):
        self.__nume = nume_nou

    def set_cnp(self,cnp):
        self.__cnp = cnp

    def __eq__(self,client):
        return self.__id_client == client.__id_client

    def __str__(self):
        return f"{self.__id_client},{self.__nume},{self.__cnp}"

#!!!!!!! ana. bine si sergiu

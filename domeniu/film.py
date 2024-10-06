class Film:
    def __init__(self,id_film,titlu,gen,descriere):
        self.__id_film = id_film
        self.__titlu = titlu
        self.__gen = gen
        self.__descriere = descriere

    def get_id_film(self):
        return self.__id_film

    def get_titlu(self):
        return self.__titlu

    def get_descriere(self):
        return self.__descriere

    def get_gen(self):
        return self.__gen

    def set_titlu(self,titlu_nou):
        self.__titlu = titlu_nou

    def set_descriere(self,descriere_noua):
        self.__descriere = descriere_noua

    def set_gen(self,gen_nou):
        self.__gen = gen_nou

    def __eq__(self,film):
        return self.__id_film == film.__id_film

    def __str__(self):
        return f"{self.__id_film},{self.__titlu},{self.__gen},{self.__descriere}"

#f1 = Film(23,"harry potter","fain", "fan")


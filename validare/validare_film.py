class ValidareFilm:

    def validare_film(self,film):
        erori = ""
        if film.get_id_film()<0:
            erori += "id invalid!\n"
        if film.get_titlu()=="":
            erori += "titlu invalid!\n"
        if film.get_descriere()=="":
            erori += "descriere invalida!\n"
        if film.get_gen()=="":
            erori+="gen invalid!\n"
        if len(erori)>0:
            raise Exception(erori)

    def validare_id(self,id):
        erori=""
        if id<0:
            erori+="id invalid!"

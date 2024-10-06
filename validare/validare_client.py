from exceptii.valid_error import ValidationError
class ValidareClient:
    def validare_client(self,client):
        erori = ""
        if client.get_id_client()<0:
            erori += "id invalid!\n"
        if client.get_nume()=="":
            erori += "nume invalid!\n"
        if client.get_cnp()<0:
            erori += "cnp invalid!\n"
        #alte conditii cnp
        if len(erori)>0:
            raise ValidationError(erori)

    def validare_id(self,id):
        erori=""
        if id<0:
            erori+="id invalid!"

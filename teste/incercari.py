
v = [3,6,1,7,9]

def cauta(v,item):
    def cauta_recursiv(v,item):
        if v[0]==item:
            return 0
        return 1+cauta_recursiv(v[1:],item)
    try:
        return cauta_recursiv(v,item)
    except IndexError: return -1

#print(cauta(v,10))

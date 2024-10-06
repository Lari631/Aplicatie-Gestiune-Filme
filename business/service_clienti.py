from domeniu.client import Client
import random

class ServiceClienti():
    def __init__(self,repo_file_clienti,validare_client):
        self.__repo_file_clienti = repo_file_clienti
        self.__validare_client = validare_client

    def adaugare_client(self,id_client,nume,cnp):
        client=Client(id_client,nume,cnp)
        self.__validare_client.validare_client(client)
        self.__repo_file_clienti.adaugare_client(client)

    def stergere_client(self,id_client,nume,cnp):
        client= Client(id_client,nume,cnp)
        self.__validare_client.validare_client(client)
        self.__repo_file_clienti.stergere_client(client)

    def cautare_client_id(self,id):
        self.__validare_client.validare_id(id)
        return self.__repo_file_clienti.cautare_client_dupa_id(id)

    def cautare_recursiva_id(self,id):
        self.__validare_client.validare_id(id)
        return self.__repo_file_clienti.cautare_recursiva(id)

    def modificare_client(self,id_client,nume,cnp):
        client = Client(id_client,nume,cnp)
        self.__validare_client.validare_client(client)
        self.__repo_file_clienti.modificare_client(client)

    def get_all_clienti(self):
        return self.__repo_file_clienti.get_all()

    def get_nr_clienti(self):
        nr = 0
        clienti = self.__repo_file_clienti.get_all()
        return len(clienti)

    def random_client(self,numar):
        """
        genereaza random id(1,100),nume din lista_nume,cnp(5000101000000,6000101000000)
        numar:int- de cate ori genereaza random
        """
        lista_nume=['Ana','Georgiana','Matei','Andrei','Sebastian','Mihai','Maria','Irina','Sara','Angela','Elena']
        cnt=0
        random.seed(2)
        while cnt!=numar:
            id_nou=random.randint(1,max(100,numar))
            nume_nou=random.choice(lista_nume)
            cnp_nou=random.randint(5000101000000,6000101000000)
            client=Client(id_nou,nume_nou,cnp_nou)
            try:
                #self.__validare_client(client)
                self.__repo_file_clienti.adaugare_client(client)
                cnt=cnt+1
            except:
                pass

    def combsort(self,arr, key=None, reverse=False):
        def getNextGap(gap):
            # Shrink gap by a factor of 1.3
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

    def combsort_dict(self,dct,key=None, reverse=False, by_key=True):
        def getNextGap(gap):
            # Shrink gap by a factor of 1.3
            gap = (gap * 10) // 13
            return max(1, gap)

        keys = list(dct.keys())
        n = len(keys)
        gap = n
        swapped = True

        while gap != 1 or swapped:
            gap = getNextGap(gap)
            swapped = False

            for i in range(0, n - gap):
                compare_element_1 = keys[i]
                compare_element_2 = keys[i + gap]

                if by_key:
                    compare_element_1 = keys[i]
                    compare_element_2 = keys[i + gap]
                else:
                    compare_element_1 = dct[keys[i]]
                    compare_element_2 = dct[keys[i + gap]]

                if key:
                    compare_element_1 = key(compare_element_1)
                    compare_element_2 = key(compare_element_2)

                comparison_result = compare_element_1 > compare_element_2 if not reverse else compare_element_1 < compare_element_2

                if comparison_result:
                    keys[i], keys[i + gap] = keys[i + gap], keys[i]
                    swapped = True

        if by_key:
            return {k: dct[k] for k in keys}
        else:
            sorted_dict = {k: dct[k] for k in keys}
            return sorted_dict

    """
    # Example usage with sorting dictionary keys:
    my_dict = {'b': 2, 'a': 1, 'c': 3}
    sorted_keys_dict = combsort_dict(my_dict, by_key=True)
    print("Original dictionary:", my_dict)
    print("Sorted dictionary by keys:", sorted_keys_dict)
    
    # Example usage with sorting dictionary values:
    my_dict = {'b': 2, 'a': 1, 'c': 3}
    sorted_values_dict = combsort_dict(my_dict, by_key=False)
    print("\nOriginal dictionary:", my_dict)
    print("Sorted dictionary by values:", sorted_values_dict)

    
    # Example usage:
    my_list = [64, 25, 12, 22, 11]
    sorted_list = combsort(my_list[:], reverse=True)  # Sort in descending order
    print("Original list:", my_list)
    print("Sorted list in descending order:", sorted_list)
    
    # Example usage with key function:
    word_list = ["apple", "banana", "cherry", "date"]
    sorted_word_list = combsort(word_list[:], key=len)  # Sort based on word length
    print("\nOriginal word list:", word_list)
    print("Sorted word list by length:", sorted_word_list)
    """

#inainte: repo_client nu repo_file_client

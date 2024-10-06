class Sort:
    #sorted(iterable, key=None, reverse=False)
    def comb_sort(self,lista):
        shrink_fact = 1.3
        gaps = len(lista)
        swapped = True
        i = 0
        while gaps > 1 or swapped:
            gaps = int(float(gaps) / shrink_fact)
            swapped = False
            i = 0
            while gaps + i < len(lista):
                if lista[i] > lista[i+gaps]:
                    lista[i], lista[i+gaps] = lista[i+gaps], lista[i]
                    swapped = True
                i += 1
        return lista

    def generic_comb(self,lista, reverse = False, key = None):
        pass

    def insertionsort(self,arr, key=None, reverse=False):
        n = len(arr)

        for i in range(1, n):
            current_element = arr[i]
            key_value = current_element if key is None else key(current_element)

            j = i - 1
            while j >= 0 and (key_value < (key(arr[j]) if key else arr[j]) if not reverse else key_value > (key(arr[j]) if key else arr[j])):
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = current_element

        return arr

    def generic_insertion(self,lista,reverse = False, key = None):
        for i in range(1, len(lista)):
            if key == None:
                el = lista[i]
            else: el = key
            j = i - 1
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
            if reverse == False:
                while j >= 0 and el < lista[j]:
                    lista[j + 1] = lista[j]
                    j = j - 1
            else:
                while j >= 0 and el > lista[j]:
                    lista[j + 1] = lista[j]
                    j = j - 1
        # Place key at after the element just smaller than it.
            lista[j + 1] = el

#inserton_sort(self,dictionar,reverse = True, key = nr)


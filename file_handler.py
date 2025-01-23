
'''
    FISIERUL PENTRU FUNCTIILE DE SALVARE A LISTEI IN FISIER / INCARCARE A LISTEI DIN FISIER
'''

import os
from encryption_utils import encrypt_data, decrypt_data

FILE_NAME = "todo_list.enc" # Denumirea fisierului unde se vor afla task-urile criptate
KEY_FILE = "key.key" # Denumirea fisierului unde se va afla cheia de criptare


def save_todo_list(tasks):
    '''
        Cand aplicatia va salva to-do list-ul, trebuie ca lista sa se salveze criptata in fisierul specific.

        Parametrul tasks va fi vectorul cu toate task-urile, un vector de string-uri.
        Trebuie convertit intr-un singur string mare, pentru a putea fi pasat functiei de criptare. Rezultatul 
        va fi un singur string mare cu lista. Acesta trebuie convertit in format binar folosind encode() (deoa-
        rece functia de criptare se asteapta la un parametru de tip string binar).

        Apoi, acel string e pasat functiei de criptare si se obtine string-ul criptat, care trebuie scris in
        format binar in fisierul unde se vor afla task-urile de criptare (definit mai sus).

        WARNING: Atunci cand unesti elementele vectorului intr-un singur string, adauga un caracter special pe
        post de separator intre ele, si tine minte ce caracter ai folosit!
    '''
    pass


def load_todo_list():
    '''
        Aceasta functie trebuie sa converteasca lista de task-uri din format criptat intr-un vector de
        string-uri, folosit de partea de GUI a aplicatiei.

        Prima oara verificam daca exista fisierul unde ar trebui sa se afle task-urile criptate (definit mai
        sus), folosind biblioteca os.

        Daca nu exista, vom returna un vector gol.

        Altfel, vom citi binar continutul fisierului (string-ul criptat), pe care il vom pasa apoi functiei de
        decriptare.
        Rezultatul acesteia va fi un string in format binar. Dupa ce il decodam in format text, folosind decode(),
        va rezulta textul decriptat cu task-urile. Pe acesta, trebuie sa il spargem intr-un vector de string-uri,
        pe care apoi il vom returna.

        WARNING: Foloseste separatorul stabilit mai sus ca sa spargi string-ul mare in elemente ale vectorului!
    '''
    pass

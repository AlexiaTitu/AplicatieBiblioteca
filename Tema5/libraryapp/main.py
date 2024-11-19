
"""
Scrieți o aplicație pentru o bibliotecă. Aplicația stochează:
cărți: <book_id>,<titlu>,<descriere>,<autor>,etc
clienți: <client_id>, <nume>, <CNP>,etc

Creați o aplicație care permite:

gestiunea listei de cărți și clienți
F1: adaugă
F2: șterge
F3: modifică lista de cărți
F4: lista de clienți
F5: căutare carte
F6: căutare clienți
Inchirieri/returnari
F7: Închiriere carte
F8: returnare carte
Rapoarte:
F9: Cele mai inchiriate cărți
F10: Cliei 20% dintre cei mai activi clienți (nume client si numărul de cărți închiriate)
F11: Primi(i) 20% dintre cei mai activi clienți (nume client si numărul de cărți închiriate)




I1: F1, F2, F3, F4, F5, F6
I2: F7, F8
I3: F9, F10, F11

"""



from Tema5.libraryapp.operations.test_bookoperations import test_book_operations
from Tema5.libraryapp.domain.test_bookentity import test_bookentity
from Tema5.libraryapp.domain.test_cliententity import test_cliententity
from Tema5.libraryapp.operations.test_clientoperations import test_client_operations
from Tema5.libraryapp.ui.console import run_console


def main():
    run_console()

def test_all():
   test_book_operations()
   test_bookentity()
   test_cliententity()
   test_client_operations()

test_all()

main()



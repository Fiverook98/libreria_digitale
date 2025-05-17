import func_lib
flag = True
while flag:
        print("""\n Gestione Libreria Personale)
            1. Aggiungi un libro
            2. Cerca un libro
            3. Elenca tutti i libri
            4. Elimina un libro
            5. Modifica dello stato di lettura
            6. Esci""")
        
        choice = input("Scegli un'opzione: ")
        if choice == "1":
            func_lib.add_book()
        elif choice == "2":
            func_lib.search_book()
        elif choice == "3":
            func_lib.list_lib()
        elif choice == "4":
            func_lib.delete_book()
        elif choice == "5":
            func_lib.update_read_status()
        elif choice == '6':
             print("Arrivederci")
             flag = False
        else:
            print(" Scelta non valida, riprova.")



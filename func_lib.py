import json
import merge

FILE_PATH = "my_digital_library/my_book.json"

#carica la libreria
def load_library():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []
    
#salva la libreria modificata
def save_lib(books):
    with open(FILE_PATH, "w") as file:
        json.dump(books, file, indent=4)

#aggiungi un nuovo libro alla libreria
def add_book():
    books = load_library()
    request = ["Title", "Author", "Genre", "Year", "Read Status"]
    book_data = {}

    for quest in request:
        book_data[quest.lower().replace(" ", "_")] = input(f"{quest}: ")

    book_data["year"] = int(book_data["year"])

    books.append(book_data)
    
    #ordinamento automatico all'aggiunta con complessità O(n log n)
    merge.merge_sort(books)

    save_lib(books)

    print(f"Il libro '{book_data['title']}' è stato aggiunto e la libreria è stata ordinata!")


#cerca un libro
def search_book():
    books = load_library()
    choice = input("\nCerca un libro per:\n 1. Titolo\n 2. Anno\n 3. Genere\n\n Scegli pure: ")

    if choice == "1":
        src = input("Inserisci il titolo del libro.").lower()
        found = [book for book in books if book['title'].lower() == src]
    elif choice == '2':
        src = int(input("Inserisci l'anno di pubblicazione."))
        found = [book for book in books if book['year'] == src]
    elif choice == '3':
        src = input("Inserisci il genere che stai cercando").lower()
        found = [book for book in books if book['genere'].lower() == src]
    else:
        print("Scelta non valida")
        return

    if found:
        print("\nLibri Trovati:")
        for book in found:
            print(f">> {book['title']} ({book['author']}) - {book['year']} [{book['genre']}]")
    else:
        print("Nessun libro trovato con il criterio selezionato.")

#restituisci l'intera libreria
def list_lib():
    books = load_library()
    if books:
        print("\nLibreria Personale:")
        for book in books:
            print(f">> {book['title']} ({book['author']}) - {book['year']} [{book['genre']}]")
    else:
        print("La libreria è attualmente vuota.")

#elimina un libro dalla libreria
def delete_book():
    books = load_library()
    choice = input("\nElimina un libro per:\n 1. Titolo\n 2. Anno\n 3. Genere\n\n Scegli pure:")

    if choice == "1":
        src = input("Inserisci il titolo del libro.").lower()
        books = [book for book in books if book['title'].lower() != src]
    elif choice == '2':
        src = int(input("Inserisci l'anno di pubblicazione."))
        books = [book for book in books if book['year'] != src]
    elif choice == '3':
        src = input("Inserisci il genere che stai cercando").lower()
        books = [book for book in books if book['genere'].lower() != src]
    else:
        print("Scelta non valida")
        return
    
    save_lib(books)
    print(f"I libri con '{src}' sono stati eliminati. (Se esistevano)")

#modifica dello stato di lettura
def update_read_status():
    books = load_library()
    title = input("Inserisci il titolo del libro che vuoi aggiornare: ").lower()
    status = ["Da leggere", "In lettura", "Letto"]
    
    for book in books:
        if book['title'].lower() == title:
            new_status = input("A che punto sei con la lettura?\n[Da leggera, In lettura, Letto]>> ")
            if new_status in status:
                book['read_status'] = new_status
                save_lib(books)
                return
            else:
                print("Stato non valido. Riprova.")
                return
            
    print("Libro non trovato.")

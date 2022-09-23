# Implementatin of Student Library System using OOPs where Students can borrow a book from the list of books. 
# And return the book after use.
# Every books quantity is 1. And you can add additional books to the list too.

class Library:
    # Defining constructor : list of books
    def __init__(self, listOfBooks) -> None:
        self.books = listOfBooks

# Displaying the name of available books in the library
    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books: # listing the books
            print(" --> " + book)

# Borrowing book
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f"You have been issued {bookName}. Please return it in 30 days.")
            # removes the bookName with has been borrowed
            self.books.remove(bookName)
            return True  # if the borrowing is successful
        else:
            print("Sorry, this book 'is either not available' or 'has already been issued to' someone else. Please wait until the book is returned.")
            return False  # if the borrowing is unsuccessful

# Returning the book to library( adding the book back to the booklist )
    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it.")


class Student:
    # Requesting the book which the student wants:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(
        ["DSA", "Django", "PythonBeginners", "WebDevelopment"])
    student = Student()  # student is a object
    
    print("\n\n***** Welcome to the Central Library ******\n\n")
    while True:
        welcomeMsg = '''Please choose an action option:
        1. Listing all the books
        2. Reqest a book
        3. Add / Return a book
        4. Exit the Library        
        '''
        print(welcomeMsg)

        choice = int(input("Enter your choice: "))
        if choice == 1:
            centralLibrary.displayAvailableBooks()
            print('\n')

        elif choice == 2:
            centralLibrary.borrowBook(student.requestBook())
            print('\n')

        elif choice == 3:
            centralLibrary.returnBook(student.returnBook())
            print('\n')

        elif choice == 4:
            print("Thanks for choosing Central Library. ")
            exit()

        else:
            print("Invalid Choice")

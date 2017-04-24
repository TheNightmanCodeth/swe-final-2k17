''' Parses books.csv into python structs '''
import csv, os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class BookParser:
    #Dict object keys:
    ISBN = 0
    TITLE = 1
    AUTHOR = 2
    SEMESTER = 3
    CLASS = 4
    EDITION = 5
    PROFESSOR = 6
    CRN = 7
    REQUIRED = 8
    STOCK_NEW = 9
    STOCK_USED = 10
    STOCK_RENT = 11
    STOCK_EBOOK = 12
    PRICE_NEW = 13
    PRICE_USED = 14
    PRICE_RENT = 15
    PRICE_EBOOK = 16
    DESCRIPTION = 17

    #Parses books file and returns a list of dict objects
    def csv_to_dict_list(self):
        books_file_dir = os.path.join(os.getcwd(), 'files/books.csv')
        with open(books_file_dir, 'rb') as cvfile:
            reader = csv.reader(cvfile, delimiter=',')
            books = []
            for book in reader:
                #Remove some weird utf-8 characters from description.
                book[17] = book[17].decode('latin-1')
                books.append(book)
            return books

    #Writes new stock value to book by isbn
    def update_stock(self, isbn, bk_type, to_remove):
        books_file_dir = os.path.join(os.getcwd(), 'files/books.csv')
        read = csv.reader(open(books_file_dir))
        #Save current csv values into array
        books = [book for book in read]
        for book in books:
            if book[0] == isbn:
                #Overwrite the value we want to update in temp array
                if bk_type == 'New':
                    new_stock = int(book[self.STOCK_NEW]) - int(to_remove)
                    book[self.STOCK_NEW] = new_stock
                elif bk_type == 'Rent':
                    new_stock = int(book[self.STOCK_RENT]) - int(to_remove)
                    book[self.STOCK_RENT] = new_stock
                elif bk_type == 'Used':
                    new_stock = int(book[self.STOCK_USED]) - int(to_remove)
                    book[self.STOCK_USED] = new_stock
        writer = csv.writer(open(books_file_dir, 'w'))
        #Overwrite csv data with new list
        writer.writerows(books)

    #Searches through list of books for title match
    def search_by_title(self, title):
        results = []
        books = self.csv_to_dict_list()
        for book in books:
            book_title = book[self.TITLE]
            if title.encode('utf-8').strip() in book_title:
                results.append(book)
        if len(results) < 1:
            return -1
        return results

    #Searches through list of books for ISBN match
    def search_by_isbn(self, isbn):
        results = []
        books = self.csv_to_dict_list()
        for book in books:
            book_isbn = book[self.ISBN]
            if book_isbn == isbn:
                results.append(book)
        if len(results) < 1:
            return -1
        return results

    #Searches through list of books for professor match
    def search_by_prof(self, prof):
        results = []
        books = self.csv_to_dict_list()
        for book in books:
            book_prof = book[self.PROFESSOR]
            if prof is not ' ':
                if prof.encode('utf-8').strip() in book_prof:
                    results.append(book)
        if len(results) < 1:
            return -1
        return results

    #Searches through list of books for class match
    def search_by_class(self, classs):
        results = []
        books = self.csv_to_dict_list()
        for book in books:
            book_class = book[self.CLASS]
            if classs is not None:
                if classs.encode('utf-8').strip() in book_class:
                    results.append(book)
        if len(results) < 1:
            return -1
        return results

    #Returns list of professors for prof. dropdown
    def get_list_of_prof(self):
        results = []
        books = self.csv_to_dict_list()
        results.append('Professor')
        abc = []
        for book in books:
            prof = book[self.PROFESSOR]
            abc.append(prof)
        results.extend(sorted(abc))
        return results

    #Returns list of classes for class dropdown
    def get_list_of_classes(self):
        results = []
        books = self.csv_to_dict_list()
        results.append('Class')
        abc = []
        for book in books:
            classs = book[self.CLASS]
            abc.append(classs)
        results.extend(sorted(abc))
        return results

    #Searches for books by AUTHOR
    def search_by_author(self, author):
        results = []
        books = self.csv_to_dict_list()
        for book in books:
            book_author = book[self.AUTHOR]
            if author in book_author:
                results.append(book)
        if len(results) < 1:
            return -1
        return results

    #searches through list of books for description keywords
    def search_by_desc(self, keyword):
        results = []
        books = self.csv_to_dict_list()
        for book in books:
            book_desc = book[self.DESCRIPTION]
            if keyword is not None:
                if keyword.encode('utf-8').strip() in book_desc:
                    results.append(book)
        if len(results) < 1:
            return -1
        return results

    #Returns list of available types for given book dict
    def types_for_book(self, book):
        types_available = []
        if book[self.STOCK_NEW] is not 0:
            types_available.append('New')
        if book[self.STOCK_USED] is not 0:
            types_available.append('Used')
        if book[self.STOCK_RENT] is not 0:
            types_available.append('Rent')
        if book[self.STOCK_EBOOK] is not 0:
            types_available.append('Ebook')
        return types_available

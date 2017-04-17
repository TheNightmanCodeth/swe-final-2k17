''' Parses books.csv into python structs '''
import csv, os

class BookParser:
    #Dict object keys:
    ISBN = 0
    TITLE = 1
    AUTHOR = 2
    SEMESTER = 3
    CLASS = 4
    EDITION = 5
    PROFESSOR = 6
    CLASS_CODE = 7
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
                books.append(book)
            return books

    #Searches through list of books for title match
    def search_by_title(self, title):
        results = []
        books = self.csv_to_dict_list()
        for book in books:
            book_title = book[self.TITLE]
            if title in book_title:
                results.append(book)
        if len(results) < 1:
            return -1
        return results

''' Parses books.csv into python structs '''
import csv, os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

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

using System;
using System.IO;
using System.Reflection;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.VisualBasic.FileIO;
using KSU_Online_Bookstore.Models;

namespace KSU_Online_Bookstore.Controllers
{
    public class BooksRepositoryController : Controller
    {
        /*
         * Returns list of Book objects.
         */ 
        public List<Book> getBooks()
        {
            //This is the path to the CSV file. For some reason ASP has no ref to proj root? You will need to change this to get it to compile
            string csv_path = @"C:\Users\Joe\Documents\Projects\swe\KSU_Online_Bookstore\assets\books.csv";

            //Here we create a TextFieldParser using the path above to read the csv
            TextFieldParser parer = new TextFieldParser(csv_path);

            //Create empty List of books to populate for return
            List<Book> books = new List<Book>();

            using (TextFieldParser parser = new TextFieldParser(csv_path))
            {
                //The text file is a delimited CSV, and the fields are seperated with a comma
                parser.TextFieldType = FieldType.Delimited;
                parser.SetDelimiters(new string[] { "," });

                while (parser.PeekChars(1) != null)
                {
                    string[] fields = parser.ReadFields();
                    Book book = arrayToBook(fields);
                    books.Add(book);
                }                
            }
            return books;
        }
        
        /*
         * Takes an array of values and returns a list of Book objects
         */ 
        private Book arrayToBook(string[] values)
        {
            //Create empty List of books to populate for return
            Book newBook;

            System.Diagnostics.Debug.WriteLine(values.Length);

            int count = 0;
            string[] thisBook = new string[18];
            do
            {
                //Every 18 values is a book
                for (int i = 0; i < 18; i++)
                {
                    thisBook[i] = values[count];
                    count++;
                }
                
                //Create boolean from required field
                bool req = thisBook[8] == "Required" ? true : false;

                //Create book from value array
                newBook = new Book(thisBook[0], thisBook[1], thisBook[2], thisBook[3], thisBook[4], int.Parse(thisBook[5]), thisBook[6], thisBook[7], req, int.Parse(thisBook[9]), int.Parse(thisBook[10]), int.Parse(thisBook[11]), int.Parse(thisBook[12]), double.Parse(thisBook[13]), double.Parse(thisBook[14]), double.Parse(thisBook[15]), double.Parse(thisBook[16]), thisBook[17]);
            } while (count < values.Length);

            return newBook;
        }
    }
}
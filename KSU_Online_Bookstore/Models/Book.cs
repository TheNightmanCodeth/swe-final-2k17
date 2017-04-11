using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace KSU_Online_Bookstore.Models
{
    //CSV FORMAT:

    /*************************************************************************************************
     * ISBN(STR), TITLE(STR), AUTHOR(STR), SEMESTER(STR), CLASS(STR), SECTION(INT), PROFESSOR(STR),  *
     * CODE(STR), REQUIRED(BOOL), AMT_PURCHASE(INT), AMT_USED(INT), AMT_RENT(INT), AMT_EBOOK(INT),   *
     * PRICE_PURCHASE(INT), PRICE_USED(INT), PRICE_EBOOK(INT), PRICE_RENT(INT), DESC(STR)            *
     *************************************************************************************************/
    public class Book
    {
        public string ISBN, title, author, semester, className, professor, code, description;
        public bool required;
        public int purchase_amt, section, used_amt, rent_amt, ebook_amt;
        public double purchase_price, used_price, ebook_price, rent_price;

        //Constructor
        public Book(string ISBN, string title, string auth, string sem, string className, int sect, string prof, string code, bool req, int purAmt, int useAmt, int renAmt, int eboAmt, double purPri, double usePrice, double eboPrice, double renPrice, string desc)
        {
            this.ISBN = ISBN;
            this.title = title;
            this.author = auth;
            this.description = desc;

            this.semester = sem;
            this.className = className;
            this.section = sect;
            this.professor = prof;
            this.code = code;           

            this.required = req;

            this.purchase_amt = purAmt;
            this.used_amt = useAmt;
            this.rent_amt = renAmt;
            this.ebook_amt = eboAmt;
            this.purchase_price = purPri;
            this.used_price = usePrice;
            this.ebook_price = eboPrice;
            this.rent_price = renPrice;
            //Fuck
        }
    }
}

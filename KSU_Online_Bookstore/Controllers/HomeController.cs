using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace KSU_Online_Bookstore.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            BooksRepositoryController b = new BooksRepositoryController();
            List<Models.Book> books = b.getBooks();
            foreach(Models.Book book in books)
            {
                System.Diagnostics.Debug.WriteLine("Book: " + book.ISBN);
            }
            return View();
        }

        public IActionResult About()
        {
            ViewData["Message"] = "Your application description page.";

            return View();
        }

        public IActionResult Contact()
        {
            ViewData["Message"] = "Your contact page.";

            return View();
        }

        public IActionResult Error()
        {
            return View();
        }
    }
}

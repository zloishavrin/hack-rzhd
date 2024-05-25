using Microsoft.EntityFrameworkCore;
using RzhdAPI.Models;

namespace RzhdAPI
{
    public class ApplicationContext : DbContext
    {
        public DbSet<User> Users { get; set; }

        public ApplicationContext()
        {
            Database.EnsureCreated();
        }
        public ApplicationContext(DbContextOptions<ApplicationContext> options) : base(options)
        {

        }
        public DbSet<RzhdAPI.Models.Articles> Articles { get; set; } = default!;
    }
}

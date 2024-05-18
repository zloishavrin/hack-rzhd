using RzhdAPI.Models;

namespace RzhdAPI.DTO
{
    public class ArticleDTO
    {
        public string Title { get; set; }
        public DateTime Date { get; set; }
        public List<Violation> Violations { get; set; }
    }
}

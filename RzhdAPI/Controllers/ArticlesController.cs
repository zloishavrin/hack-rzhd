using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using NuGet.Common;
using RzhdAPI;
using RzhdAPI.Models;

namespace RzhdAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ArticlesController : ControllerBase
    {
        private readonly ApplicationContext _context;

        public ArticlesController(ApplicationContext context)
        {
            _context = context;
        }

        // GET: api/Articles
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Articles>>> GetArticles()
        {
            return await _context.Articles.ToListAsync();
        }

        [HttpGet("download/{id}")]
        public async Task<ActionResult<Articles>> DownloadArticles([FromHeader] string token, int id)
        {
            if(token == null) { return Unauthorized(); }
            var articles = await _context.Articles.FindAsync(id);

            if (articles == null)
            {
                return NotFound();
            }

            return articles;
        }
        // GET: api/Articles/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Articles>> GetArticles([FromHeader] string token, int id)
        {
            if (token == null) { return Unauthorized(); }
            var articles = await _context.Articles.FindAsync(id);

            if (articles == null)
            {
                return NotFound();
            }

            return articles;
        }

        // PUT: api/Articles/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutArticles(int id, Articles articles)
        {
            if (id != articles.Id)
            {
                return BadRequest();
            }

            _context.Entry(articles).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!ArticlesExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return NoContent();
        }

        // POST: api/Articles
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<Articles>> PostArticles(Articles articles)
        {
            _context.Articles.Add(articles);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetArticles", new { id = articles.Id }, articles);
        }

        // DELETE: api/Articles/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteArticles(int id)
        {
            var articles = await _context.Articles.FindAsync(id);
            if (articles == null)
            {
                return NotFound();
            }

            _context.Articles.Remove(articles);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool ArticlesExists(int id)
        {
            return _context.Articles.Any(e => e.Id == id);
        }
    }
}

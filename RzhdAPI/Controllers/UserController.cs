using Microsoft.AspNetCore.Mvc;
using RzhdAPI.DTO;
using RzhdAPI.Models;

namespace RzhdAPI.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class UserController : ControllerBase
    {
        ApplicationContext _context = new ApplicationContext();

        [HttpPost]
        [Route("login")]
        public async Task<ActionResult> Login([FromBody] UserDTO _userDTO)
        {
            User _user = _context.Users.FirstOrDefault(u => u.Name == _userDTO.Name);
            if (_user != null)
            {
                return Ok(AuthOptions.Token);
            }
            return NotFound();
        }
        [HttpPost]
        [Route("registration")]
        public async Task<ActionResult> Registration([FromBody] UserDTO _userDTO)
        {
            User _user = _context.Users.FirstOrDefault(u => u.Name == _userDTO.Name);
            if (_user != null)
            {
                return Ok(AuthOptions.Token);
            }
            return NotFound();
        }
    }
}

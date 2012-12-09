import webapp2
import jinja2
import os

# This loads up our preferred templating engine, Jinja, instead
#of Google's default App Engine templating system
jinja_environment = jinja2.Environment( 
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

# BaseHandler is the Handler all others derive from
# and common Handler behavior, like rendering templates,
# belongs on it
class BaseHandler(webapp2.RequestHandler):

  # Render can be called by any type of Handler, all it needs
  # is the name of the file in the "views" directory
  # and a dictionary containing values to make available
  # to the template
  def render(self, template_file, template_values=None):
    if template_values is None:
      template_values = {}

    template = jinja_environment.get_template("/views/" + template_file)
    self.response.out.write(template.render(template_values))  

class IndexHandler(BaseHandler):
  def get(self):
    self.render("index.html", {})

routes = [
  ("/", IndexHandler)
]

app = webapp2.WSGIApplication(routes, debug=True)

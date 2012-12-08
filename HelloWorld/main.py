#This tells python that we want access
#to the webapp2 library in this code file
import webapp2

#This is a class that defines a set of
#behaviors for different web requests
class IndexHandler(webapp2.RequestHandler):

  #This is the function that handles GET web 
  #requests (requests for data)
  def get(self):

    #This is how we grab a URL parameter out of the
    #web request, and store it in a variable. We also
    #tell the request object what value we'd like to get
    #back in case it can't find the parameter
    input_string = self.request.get("input", "no input!")

    # We'll be writing between
    # the dotted lines
    # -------------------------------

    output_string = input_string

    # -------------------------------

    #Tell's the server to send back
    #a response whose content is
    #the content of output_string
    self.response.write(output_string)

#This is a list variable where we enumerate
#what URLs we care about, when one of those 
#URLs is requested, like "/", which piece of
#code it goes to for handling
routes = [
  ("/", IndexHandler)
]

#This tells the server to start listening on
#the routes we care about
app = webapp2.WSGIApplication(routes, debug=True)
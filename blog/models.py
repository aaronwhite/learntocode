from google.appengine.ext import db

class BaseModel(db.Model):
  created = db.DateTimeProperty(auto_now_add=True)

class Entry(BaseModel):
  title = db.StringProperty(default="")
  body = db.TextProperty(default="")
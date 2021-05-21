# coding: utf-8
# Eliminar libro

import webapp2
import time
from webapp2_extras import jinja2

from google.appengine.ext import ndb
from model.libro import Libro
from model.escritor import Escritor
from model.editorial import Editorial


class EliminarLibroHandler(webapp2.RequestHandler):
    def get(self):
        libro = Libro.recuperar(self.request)
        libro.key.delete()
        time.sleep(1)
        return self.redirect("/")



app = webapp2.WSGIApplication([
    ('/libros/eliminar', EliminarLibroHandler)
], debug=True)

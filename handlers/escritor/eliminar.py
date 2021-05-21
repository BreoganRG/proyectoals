# coding: utf-8
# Eliminar libro

import webapp2
import time
from webapp2_extras import jinja2

from google.appengine.ext import ndb
from model.libro import Libro
from model.escritor import Escritor
from model.editorial import Editorial


class EliminarEscritorHandler(webapp2.RequestHandler):
    def get(self):
        borrar = True
        escritor = Escritor.recuperar(self.request)
        libros = Libro.query()
        for libro in libros:
            if libro.escritor == escritor.key:
                borrar = False

        if borrar:
            escritor.key.delete()
            time.sleep(1)
            return self.redirect("/escritor/escritores")
        else:
            self.response.write("No puedes borrar un escritor habiendo libros en la biblioteca escritos por este escritor")


app = webapp2.WSGIApplication([
    ('/escritor/eliminar', EliminarEscritorHandler)
], debug=True)

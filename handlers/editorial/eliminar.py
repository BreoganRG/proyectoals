# coding: utf-8
# Eliminar editorial

import webapp2
import time
from webapp2_extras import jinja2

from google.appengine.ext import ndb
from model.libro import Libro
from model.escritor import Escritor
from model.editorial import Editorial


class EliminarEditorialHandler(webapp2.RequestHandler):
    def get(self):
        borrar = True
        editorial = Editorial.recuperar(self.request)
        libros = Libro.query()
        for libro in libros:
            if libro.editorial == editorial.key and borrar:
                borrar = False

        if borrar:
            editorial.key.delete()
            time.sleep(1)
            return self.redirect("/editorial/editoriales")
        else:
            self.response.write(
                "No puedes borrar una editorial habiendo libros en la biblioteca de esta editorial")




app = webapp2.WSGIApplication([
    ('/editorial/eliminar', EliminarEditorialHandler)
], debug=True)

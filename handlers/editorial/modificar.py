# coding: utf-8
# Modificar editorial

import webapp2
import time
from webapp2_extras import jinja2

from google.appengine.ext import ndb
from model.libro import Libro
from model.escritor import Escritor
from model.editorial import Editorial


class ModificarEditorialHandler(webapp2.RequestHandler):
    def get(self):

        editorial = Editorial.recuperar(self.request)

        valoresPlantilla = {
            "editorial": editorial
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("modificarEditorial.html", **valoresPlantilla))

    def post(self):
        editorial = Editorial.get_by_id(int(self.request.get("edEditorial", "")))
        nombre = self.request.get("edNombre", "")
        str_codigoEditorial = self.request.get("edCodigo", "")
        try:
            codigoEditorial = int(str_codigoEditorial)
        except ValueError:
            codigoEditorial = -1

        if codigoEditorial < 0 or not nombre:
            self.response.write("Error en la modificación")
        else:
            editorial.nombre = nombre
            editorial.codigoEditorial = codigoEditorial
            editorial.put()
            time.sleep(1)
            return self.redirect("/editorial/editoriales")

app = webapp2.WSGIApplication([
    ('/editorial/modificar', ModificarEditorialHandler)
], debug=True)

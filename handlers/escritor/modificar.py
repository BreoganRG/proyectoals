# coding: utf-8
# Modificar Escritor

import webapp2
import time
from webapp2_extras import jinja2

from google.appengine.ext import ndb
from model.libro import Libro
from model.escritor import Escritor
from model.editorial import Editorial


class ModificarEscritorHandler(webapp2.RequestHandler):
    def get(self):

        escritor = Escritor.recuperar(self.request)

        valoresPlantilla = {
            "escritor": escritor
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("modificarEscritor.html", **valoresPlantilla))

    def post(self):
        escritor = Escritor.get_by_id(int(self.request.get("edEscritor", "")))
        nombre = self.request.get("edNombre", "")
        apellidos = self.request.get("edApellidos", "")
        str_edad = self.request.get("edEdad", "")
        try:
            edad = int(str_edad)
        except ValueError:
            edad = -1

        if edad < 0 or not nombre or not apellidos:
            self.response.write("Error en la modificación")
        else:
            escritor.nombre = nombre
            escritor.apellidos = apellidos
            escritor.edad = edad
            escritor.put()
            time.sleep(1)
            return self.redirect("/escritor/escritores")

app = webapp2.WSGIApplication([
    ('/escritor/modificar', ModificarEscritorHandler)
], debug=True)

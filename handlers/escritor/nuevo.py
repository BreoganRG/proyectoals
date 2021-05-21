# coding: utf-8
# Nuevo escritor

import webapp2
import time
from webapp2_extras import jinja2

from model.libro import Libro
from model.escritor import Escritor
from model.editorial import Editorial


class NuevoEscritorHandler(webapp2.RequestHandler):
    def get(self):

        escritores = Escritor.query().fetch(50)
        editoriales = Editorial.query().fetch(50)

        valoresPlantilla = {
            "escritores": escritores,
            "editoriales": editoriales
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("nuevoEscritor.html", **valoresPlantilla))

    def post(self):
        nombre = self.request.get("edNombre", "")
        apellidos = self.request.get("edApellidos", "")
        str_edad = self.request.get("edEdad", "")

        try:
            edad = int(str_edad)
        except ValueError:
            edad = -1

        if edad < 0 or not nombre or not apellidos:
            self.response.write("Error wachin")
        else:
            escritor = Escritor(nombre=nombre, apellidos=apellidos, edad=edad)
            escritor.put()
            time.sleep(1)
            return self.redirect("/escritor/escritores")




app = webapp2.WSGIApplication([
    ('/escritor/nuevo', NuevoEscritorHandler)
], debug=True)

# coding: utf-8
# detalle editorial

import webapp2
import time
from webapp2_extras import jinja2

from model.libro import Libro
from model.escritor import Escritor
from model.editorial import Editorial


class DetalleEditorialHandler(webapp2.RequestHandler):
    def get(self):

        editorial = Escritor.recuperar(self.request)



        valoresPlantilla = {
            "editorial": editorial,

        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("editorialDetalle.html", **valoresPlantilla))

    def post(self):
        nombre = self.request.get("edNombre", "")
        apellidos = self.request.get("edApellidos", "")
        str_edad = self.request.get("edEdad", "")
        print (nombre, apellidos, str_edad)
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
            return self.redirect("/")




app = webapp2.WSGIApplication([
    ('/editorial/detalle', DetalleEditorialHandler)
], debug=True)

# coding: utf-8
# Nueva editorial

import webapp2
import time
from webapp2_extras import jinja2

from model.libro import Libro
from model.escritor import Escritor
from model.editorial import Editorial


class NuevoEditorialHandler(webapp2.RequestHandler):
    def get(self):

        escritores = Escritor.query().fetch(50)
        editoriales = Editorial.query().fetch(50)

        valoresPlantilla = {
            "escritores": escritores,
            "editoriales": editoriales
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("nuevoEditorial.html", **valoresPlantilla))

    def post(self):
        nombre = self.request.get("edNombre", "")
        str_codigo = self.request.get("edCodigo", "")
        print (nombre, str_codigo)
        try:
            codigo = int(str_codigo)
        except ValueError:
            codigo = -1

        if codigo < 0 or not nombre:
            self.response.write("Error wachin")
        else:
            editorial = Editorial(nombre=nombre, codigoEditorial=codigo)
            editorial.put()
            time.sleep(1)
            return self.redirect("/editorial/editoriales")


app = webapp2.WSGIApplication([
    ('/editorial/nuevo', NuevoEditorialHandler)
], debug=True)

# coding: utf-8
# Se muestran todas las editoriales

import webapp2
from webapp2_extras import jinja2

from model.libro import Libro
from model.escritor import Escritor
from model.editorial import Editorial


class EditorialesHandler(webapp2.RequestHandler):
    def get(self):
        editoriales = Editorial.query().order(Editorial.nombre)


        valoresPlantilla = {
            "editoriales": editoriales
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("editoriales.html", **valoresPlantilla))


app = webapp2.WSGIApplication([
    ('/editorial/editoriales', EditorialesHandler)
], debug=True)

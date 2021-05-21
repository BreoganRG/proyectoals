# coding: utf-8
# Se muestran todos los escritores

import webapp2
from webapp2_extras import jinja2

from model.libro import Libro
from model.escritor import Escritor
from model.editorial import Editorial


class EscritoresHandler(webapp2.RequestHandler):
    def get(self):
        escritores = Escritor.query().order(Escritor.nombre)


        valoresPlantilla = {
            "escritores": escritores
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("escritores.html", **valoresPlantilla))


app = webapp2.WSGIApplication([
    ('/escritor/escritores', EscritoresHandler)
], debug=True)

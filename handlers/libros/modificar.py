# coding: utf-8
# Modificar libro

import webapp2
import time
from webapp2_extras import jinja2

from google.appengine.ext import ndb
from model.libro import Libro
from model.escritor import Escritor
from model.editorial import Editorial


class ModificarLibroHandler(webapp2.RequestHandler):
    def get(self):

        libro = Libro.recuperar(self.request)



        escritores = Escritor.query()
        editoriales = Editorial.query()

        escritor = Escritor.get_by_id(int(libro.escritor.id()))
        libro.nombreEscritor = escritor.nombre
        libro.apellidosEscritor = escritor.apellidos
        editorial = Editorial.get_by_id(int(libro.editorial.id()))
        libro.nombreEditorial = editorial.nombre

        if  not escritores or not editoriales:
            self.response.write("Debe introducir primero un escritor y una editorial")
        else:
            valoresPlantilla = {
                "escritores": escritores,
                "editoriales": editoriales,
                "libro": libro
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("modificarLibro.html", **valoresPlantilla))

    def post(self):
        libro = Libro.get_by_id(int(self.request.get("edLibro", "")))
        titulo = self.request.get("edTitulo", "")
        escritor = Escritor.get_by_id(int(self.request.get("edEscritor", "")))
        str_ISBN = self.request.get("edISBN", "")
        editorial = Editorial.get_by_id(int(self.request.get("edEditorial", "")))
        print
        try:
            ISBN = int(str_ISBN)
        except ValueError:
            ISBN = -1

        if ISBN < 0 or not titulo or not escritor or not editorial:
            self.response.write("Error wachin")
        else:
            print(libro)
            libro.titulo = titulo
            libro.escritor = escritor.key
            libro.ISBN = ISBN
            libro.editorial = editorial.key
            print(libro)
            libro.put()
            time.sleep(1)
            return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/libros/modificar', ModificarLibroHandler)
], debug=True)

# coding: utf-8
# Nuevo libro

import webapp2
import time
from webapp2_extras import jinja2

from webapp2_extras.users import users
from model.libro import Libro
from model.escritor import Escritor
from model.editorial import Editorial


class NuevoLibroHandler(webapp2.RequestHandler):
    def get(self):

        escritores = Escritor.query()
        editoriales = Editorial.query()

        if  not escritores or not editoriales:
            self.response.write("Debe introducir primero un escritor y una editorial")
        else:
            valoresPlantilla = {
                "escritores": escritores,
                "editoriales": editoriales,
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("nuevoLibro.html", **valoresPlantilla))

    def post(self):
        titulo = self.request.get("edTitulo", "")
        escritor = Escritor.get_by_id(int(self.request.get("edEscritor", "")))
        str_ISBN = self.request.get("edISBN", "")
        editorial = Editorial.get_by_id(int(self.request.get("edEditorial", "")))
        try:
            ISBN = int(str_ISBN)
        except ValueError:
            ISBN = -1

        def comprobarISBN(ISBN):
            if(len(str(ISBN)) != 13 ):
                errorISBN = True
            else:
                errorISBN = False
            return errorISBN

        errorISBN = comprobarISBN(ISBN)

        if not titulo or not escritor or not editorial:
            self.response.write("Error al crear el libro")
        elif errorISBN:
            self.response.write("El ISBN no tiene el formato adecuado")
        else:
            libro = Libro(titulo=titulo, editorial=editorial.key, escritor=escritor.key, ISBN=ISBN)
            libro.put()
            time.sleep(1)
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/libros/nuevo', NuevoLibroHandler)
], debug=True)

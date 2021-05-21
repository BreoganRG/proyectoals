import webapp2
from webapp2_extras import jinja2

from model.libro import Libro
from model.escritor import Escritor
from model.editorial import Editorial
from webapp2_extras.users import users

class MainHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()

        if usr:
            url_usr = users.create_logout_url("/")

        else:
            url_usr = users.create_login_url("/")


        libros = Libro.query().order(Libro.titulo)
        if libros.count() > 0:
            for libro in libros:

                escritor = Escritor.get_by_id(int(libro.escritor.id()))
                libro.nombreEscritor = escritor.nombre
                libro.apellidosEscritor = escritor.apellidos
                libro.escritor = escritor.key
                editorial = Editorial.get_by_id(int(libro.editorial.id()))
                libro.nombreEditorial = editorial.nombre
                libro.editorial = editorial.key
            if usr:
                nickname = usr.nickname()
                valoresPlantilla = {
                    "libros": libros,
                    "escritor": escritor,
                    "editorial": editorial,
                    "url_usr": url_usr,
                    "nickname": nickname,
                    "usr": usr
                }

                jinja = jinja2.get_jinja2(app=self.app)
                self.response.write(jinja.render_template("index.html", **valoresPlantilla))
            else:
                valoresPlantilla = {
                    "libros": libros,
                    "escritor": escritor,
                    "editorial": editorial,
                    "url_usr": url_usr
                }

                jinja = jinja2.get_jinja2(app=self.app)
                self.response.write(jinja.render_template("index.html", **valoresPlantilla))

        else:
            if usr:
                nickname = usr.nickname()
                valoresPlantilla = {
                    "libros": libros,
                    "url_usr": url_usr,
                    "nickname": nickname,
                    "usr": usr
                }

                jinja = jinja2.get_jinja2(app=self.app)
                self.response.write(jinja.render_template("index.html", **valoresPlantilla))
            else:
                valoresPlantilla = {
                    "libros": libros,
                    "url_usr": url_usr
                }

                jinja = jinja2.get_jinja2(app=self.app)
                self.response.write(jinja.render_template("index.html", **valoresPlantilla))



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

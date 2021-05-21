# escritor que pudo haber escrito varios libros

from google.appengine.ext import ndb


class Escritor(ndb.Model):
    nombre = ndb.StringProperty(required=True)
    apellidos = ndb.StringProperty(required=True)
    edad = ndb.IntegerProperty(required=True)
    @staticmethod
    def recuperar(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()

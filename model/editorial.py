# editorial a la que un libro pertenece

from google.appengine.ext import ndb


class Editorial(ndb.Model):
    nombre = ndb.StringProperty(indexed=True)
    codigoEditorial = ndb.IntegerProperty(required=True)

    @staticmethod
    def recuperar(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()

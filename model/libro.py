# libro que ha sido escrito por un escritor y es de una editorial


from google.appengine.ext import ndb
from escritor import Escritor
from editorial import Editorial


class Libro(ndb.Model):
    titulo = ndb.StringProperty(indexed=True)
    escritor = ndb.KeyProperty(kind=Escritor)
    ISBN = ndb.IntegerProperty(required=True)
    editorial = ndb.KeyProperty(kind=Editorial)
    @staticmethod
    def recuperar(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()

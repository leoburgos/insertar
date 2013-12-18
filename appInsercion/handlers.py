__author__ = 'leo'



from django.contrib.sessions.models import Session
from piston.handler import BaseHandler
from appInsercion.models import Foto
from datetime import timedelta, datetime
import json
import redis


class InsertHandler(BaseHandler):

    """
    Handler responsable de la autenticacion de usuarios a aplicaciones externas.
    """
    allowed_methods = ('POST',)

    def create(self, request):
        """
        retorna si un usuario esta autenticado
        recibe un session_id
        """

        vehiculo_id = request.POST.get('vehiculo_id')
        timestamp = request.POST.get('timestamp')
        var1 = request.POST.get('var1')
        var2 = request.POST.get('var2')
        var3 = request.POST.get('var3')
        r = redis.StrictRedis(host='pub-redis-15388.us-east-1-2.3.ec2.garantiadata.com', port=15388, db=0, password='wbW78T6ifVkIJSOA')
        key = vehiculo_id + ':' + timestamp
        value = r.get(key)
        if value == None:
         r.set(key,var1 + '-' + var2 + '-' + var3)
         foto = Foto(idVehiculo=vehiculo_id, var1=var1, var2=var2, var3=var3, fecha=timestamp)
         foto.save()

        return {"gol": vehiculo_id}

from django.db import models

from django.db import models
from  mongoengine import *
import datetime

from djangotoolbox.fields import ListField


class Foto(Document):
    idVehiculo = IntField()
    var1 = StringField(max_length=200)
    var2 = StringField(max_length=200)
    var3 = StringField(max_length=200)
    fecha = DateTimeField(default=datetime.datetime.now)
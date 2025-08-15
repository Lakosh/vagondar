from django.contrib import admin

from django.contrib import admin
from .models import Destination, TariffHistory, TrainEvent, Wagon

admin.site.register(Destination)
admin.site.register(TariffHistory)
admin.site.register(TrainEvent)
admin.site.register(Wagon)

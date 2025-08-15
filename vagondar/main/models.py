from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=100)
    distance_km = models.DecimalField(max_digits=6, decimal_places=4)

    def __str__(self):
        return f"{self.name} | {round(self.distance_km, 3)} км"


def get_tariff_record(destination, date):
    return TariffHistory.objects.filter(
        destination=destination,
        start_date__lte=date
    ).order_by('-start_date').first()


class TrainEvent(models.Model):
    OPERATION_CHOICES = [
        ('arrival', 'Пригон'),
        ('removal', 'Уборка'),
    ]

    operation_type = models.CharField(max_length=10, choices=OPERATION_CHOICES)
    event_date = models.DateField()
    event_time = models.TimeField()
    tariff = models.ForeignKey("TariffHistory", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Автоматически подставляет тариф, если он не выбран
        if not self.tariff and self.destination and self.event_date:
            self.tariff = get_tariff_record(self.destination, self.event_date)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_operation_type_display()} {self.event_date} | {self.event_time}"


class TariffHistory(models.Model):
    start_date = models.DateField()
    tariff = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.tariff} ₸ | {self.start_date}"


class Wagon(models.Model):
    wagon_number = models.CharField(max_length=20)
    event = models.ForeignKey(TrainEvent, on_delete=models.CASCADE, related_name='wagons')
    destination = models.ForeignKey(Destination, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.wagon_number} (событие: {self.event.id}) | {self.destination}"

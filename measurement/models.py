from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)


class Measurment(models.Model):
    sensor_id = models.ForeignKey(Sensor,on_delete=models.CASCADE)
    temperature = models.FloatField()
    date = models.DateTimeField(auto_now=True)


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

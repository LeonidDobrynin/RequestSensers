from rest_framework import serializers

from measurement.models import Sensor, Measurment


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name','description']


class MeasurementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurment
        fields = ['sensor_id', 'temperature']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurment
        fields = ['temperature', 'date']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
# TODO: опишите необходимые сериализаторы

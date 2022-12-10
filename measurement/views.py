from django.forms import model_to_dict
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurment
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementCreateSerializer,MeasurementSerializer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    def post(self, request, *args, **kwargs):
        post_new = Sensor.objects.create(
            name=request.data['name'],
            description=request.data['description']
        )
        return Response({'post':model_to_dict(post_new)})


class SensorUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasureCreate(CreateAPIView):
    queryset = Measurment.objects.all()
    serializer_class = MeasurementCreateSerializer
    def post(self, request, *args, **kwargs):
        post_new = Measurment.objects.create(
            sensor_id=Sensor.objects.get(id=request.data['sensor_id']),
            temperature=request.data['temperature']
        )
        return Response({'post': model_to_dict(post_new)})
# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

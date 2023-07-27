from django.http.response import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from .models import HoraireAlarm, Prof
from datetime import timedelta, datetime
from .seralizers import HoraireSerializer, ProfDetailSerializer


def horaireNext(request):
    start_date = datetime.now().date()
    end_date = start_date + timedelta(days=30)

    data = HoraireAlarm.objects.filter(date__range=(start_date, end_date))

    if data.count() < 1:
        return HttpResponse('no data')

    else:
        if request.method == 'GET':
            serializer = HoraireSerializer(data, many=True)
            return JsonResponse(data={"horaireList": serializer.data}, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = HoraireSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data={"horaireList": serializer.data}, status=201)
            return JsonResponse(serializer.errors, status=400)


def userList(request):

    if request.method == 'GET':
        data = Prof.objects.all()
        serializer = ProfDetailSerializer(data, many=True)
        return JsonResponse(data={'userProfile': serializer}, safe=True)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProfDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data={'userProfile': serializer}, safe=True, status=201)
        return JsonResponse(serializer.errors, status=400)

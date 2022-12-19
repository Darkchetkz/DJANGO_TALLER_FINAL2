from django.shortcuts import render,redirect
from seminarioapp.forms import Form_inscripciones
from .serialiazers import InscripcionesSerializer , InstitucionesSerializer
from .models import Inscripciones, Instituciones
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import Http404
from django.http import JsonResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')

def lis_inscripciones(request):
    reserva = Inscripciones.objects.all()
    data = {'inscripciones': reserva}
    return render(request, 'mos_inscripcion.html', data)

def cre_inscripciones(request):
    form = Form_inscripciones()
    if request.method == 'POST':
        form = Form_inscripciones(request.POST)
        if form.is_valid():
            form.save()
            
        return lis_inscripciones(request)
    data = {'form' : form}
    return render(request, 'agre_inscripcion.html', data)
    

def eli_inscripciones(request,id):
    Ins = Inscripciones.objects.get(id = id)
    Ins.delete()
    return redirect('/')

def Vista_api(request):
    emple = Inscripciones.objects.all()
    data = {'Inscripciones' : list(emple.values('rutP','nombrep','Num_telefono','Fec_inscripcion','hora','Institucion','Est_reserva','Observaciones'))}
    return JsonResponse(data)

def actu_inscripciones(request,id):
    Ins = Inscripciones.objects.get(id = id)
    form = Form_inscripciones(instance=Ins)
    if request.method == 'POST':
        form = Form_inscripciones(request.POST, instance=Ins)
        if form.is_valid():
            form.save()
        return lis_inscripciones(request)
    data = {'form':form}
    return render(request,'agre_inscripcion.html',data)



class Most_Inscripciones(APIView):
    def get(self, request):
        inscripciones = Inscripciones.objects.all()
        serial = InscripcionesSerializer(inscripciones, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscripcionesSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)



class Deta_Inscripciones(APIView):
    def get_object(self, id):
        try:
            return Inscripciones.objects.get(id=id)
        except Inscripciones.DoesNotExist:
            return Http404

    def get(self, request, id):
        inscripciones = self.get_object(id)
        serial = InscripcionesSerializer(inscripciones)
        return Response(serial.data)

    def put(self, request, id):
        inscripciones = self.get_object(id)
        serial = InscripcionesSerializer(inscripciones, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        inscripciones = self.get_object(id)
        inscripciones.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def instituciones_lista (request):
    if request.method == 'GET':
        instituciones = Instituciones.objects.all()
        serial = InstitucionesSerializer(instituciones , many=True)
        return Response(serial.data)

    elif request.method == 'POST':
        serial = InstitucionesSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def instituciones_detalle(request,id):
    try:
        instituciones = Instituciones.objects.get(id = id)
    except instituciones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionesSerializer(institucion)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InstitucionesSerializer(instituciones,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.data, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        instituciones.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



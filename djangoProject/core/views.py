#from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from core.models import SaladeAula
from django.views import View


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('id_user')
        password = request.POST.get('password')

        user = authenticate(request, id_user=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            # o retorno do status 401 é erro de retorno de autenticação, credenciais inválidas
            return JsonResponse({'message': 'Invalid credential'}, status=401)
    else:
        # método solicitado inválido
        return JsonResponse({'message': 'Invalid request method'}, status=400)

class ClassroomCreate(View):
    def post(self, request):
        number = request.POST.get('number')
        capacity = request.POST.get('capacity')
        bloco = request.POST.get('block')

        classroom = SaladeAula.objects.create(number=number, capacity=capacity, block=bloco)
        data = {'number': classroom.number, 'capacity': classroom.capacity, 'block': classroom.block}
        return JsonResponse(data, status=201)

class ClassroomList(View):
    def get(self, request):
        classrooms = SaladeAula.objects.all()
        data = [{'number': classroom.number, 'capacity': classroom.capacity, 'bloco': classroom.block} for classroom in classrooms]
        return JsonResponse(data, safe=False)


class ClassroomDetail(View):
    def get(self, request, classroom_id):
        try:
            classroom = SaladeAula.objects.get(id=classroom_id)
            data = {'number': classroom.number, 'capacity': classroom.capacity, 'bloco': classroom.block}
            return JsonResponse(data)
        except SaladeAula.DoesNotExist:
            return JsonResponse({'message': 'Classroom not found'}, status=404)


class ClassroomUpdate(View):
    def post(self, request, classroom_id):
        try:
            classroom = SaladeAula.objects.get(id=classroom_id)
        except SaladeAula.DoesNotExist:
            return JsonResponse({'message': 'Classroom not found'}, status=404)

        number = request.POST.get('number')
        capacity = request.POST.get('capacity')
        block = request.POST.get('block')

        classroom.number = number
        classroom.capacity = capacity
        classroom.block = block
        classroom.save()

        data = {'number': classroom.number, 'capacity': classroom.capacity, 'block': classroom.block}
        return JsonResponse(data)


class ClassroomDelete(View):
    def post(self, request, classroom_id):
        try:
            classroom = SaladeAula.objects.get(id=classroom_id)
            classroom.delete()
            return JsonResponse({'message': 'Classroom deleted'})
        except SaladeAula.DoesNotExist:
            return JsonResponse({'message': 'Classroom not found'}, status=404)
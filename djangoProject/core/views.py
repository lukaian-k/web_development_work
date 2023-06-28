#from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

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

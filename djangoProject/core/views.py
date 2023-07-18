from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Professor, Sala, Alocacao, Curso
from .serializers import (
    LoginSerializer,
    ProfessorSerializer,
    SalaSerializer,
    AlocacaoSerializer,
    CursoSerializer,
)


@api_view(['POST'])
def login_user(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        serializer.validated_data.pop('password')
        user = serializer.validated_data['id_user']
        return Response({'message': 'Login successful'})
    return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def professor_list(request):
    professores = Professor.objects.all()
    serializer = ProfessorSerializer(professores, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def professor_detail(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    serializer = ProfessorSerializer(professor)
    return Response(serializer.data)


@api_view(['POST'])
def professor_create(request):
    serializer = ProfessorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def sala_list(request):
    salas = Sala.objects.all()
    serializer = SalaSerializer(salas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def sala_detail(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    serializer = SalaSerializer(sala)
    return Response(serializer.data)


@api_view(['POST'])
def sala_create(request):
    serializer = SalaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def curso_list_create(request):
    if request.method == 'GET':
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def alocacao_list(request):
    alocacoes = Alocacao.objects.all()
    serializer = AlocacaoSerializer(alocacoes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def alocacao_detail(request, pk):
    alocacao = get_object_or_404(Alocacao, pk=pk)
    serializer = AlocacaoSerializer(alocacao)
    return Response(serializer.data)

@api_view(['POST'])
def alocacao_create(request):
    serializer = AlocacaoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def alocacao_delete(request, pk):
    try:
        alocacao = Alocacao.objects.get(pk=pk)
    except Alocacao.DoesNotExist:
        return Response({'message': 'Alocação não encontrada'}, status=status.HTTP_404_NOT_FOUND)

    alocacao.delete()
    return Response({'message': 'Alocação excluída com sucesso'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def alocacao_update(request, pk):
    try:
        alocacao = Alocacao.objects.get(pk=pk)
    except Alocacao.DoesNotExist:
        return Response({'message': 'Alocação não encontrada'}, status=status.HTTP_404_NOT_FOUND)

    serializer = AlocacaoSerializer(alocacao, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from .models import Professor, Sala, Alocacao, Curso, User, Horario
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id_user', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate(self, attrs):
        id_user = attrs.get('id_user')
        password = attrs.get('password')

        # Autentique o usuário com base no ID e na senha
        authenticated_user = authenticate(id_user=id_user, password=password)

        if authenticated_user is not None:
            # Se o usuário estiver autenticado, gere ou recupere um token de autenticação para o usuário
            token, _ = Token.objects.get_or_create(user=authenticated_user)
            attrs['token'] = token.key
        else:
            # Se o usuário não estiver autenticado, levante uma exceção de validação
            raise serializers.ValidationError('Login failed. Invalid credentials.')

        return attrs
class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['nome', 'departamento', 'codigo', 'formacao']

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = ['nome', 'capacidade', 'bloco']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['nome']

class AlocacaoSerializer(serializers.ModelSerializer):
    professor = serializers.PrimaryKeyRelatedField(queryset=Professor.objects.all())
    curso = serializers.PrimaryKeyRelatedField(queryset=Curso.objects.all())
    sala = serializers.PrimaryKeyRelatedField(queryset=Sala.objects.all())

    class Meta:
        model = Alocacao
        fields = ['id', 'professor', 'curso', 'horario', 'sala', 'bloco', 'semana']
        read_only_fields = ['id']



    #Logica 1

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'
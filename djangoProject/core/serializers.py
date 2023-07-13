from .models import Professor, Sala, Alocacao, Curso
from rest_framework import serializers
from django.contrib.auth import authenticate
class LoginSerializer(serializers.Serializer):
    id_user = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, attrs):
        id_user = attrs.get('id_user')
        password = attrs.get('password')

        user = authenticate(self.context.get('request'), id_user=id_user, password=password)

        if not user:
            raise serializers.ValidationError('Invalid credential')

        return attrs

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['nome', 'departamento', 'codigo', 'formacao']

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = ['nome']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nome']

class AlocacaoSerializer(serializers.ModelSerializer):
    professor = serializers.PrimaryKeyRelatedField(queryset=Professor.objects.all())
    curso = serializers.PrimaryKeyRelatedField(queryset=Curso.objects.all())
    sala = serializers.PrimaryKeyRelatedField(queryset=Sala.objects.all())

    class Meta:
        model = Alocacao
        fields = ['professor', 'curso', 'horario', 'sala', 'bloco', 'semana']



    #Logica 1


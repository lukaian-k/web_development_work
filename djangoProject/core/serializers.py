from .models import Professor, Sala, Alocacao
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

class AlocacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alocacao
        fields = ['professor', 'curso', 'sala', 'bloco']
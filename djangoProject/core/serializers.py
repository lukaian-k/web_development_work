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
    # Outros campos do serializer

    def validate(self, attrs):
        professor = attrs['professor']
        sala = attrs['sala']
        dia_semana = attrs['dia_semana']
        horario = attrs['horario']
        bloco = attrs['bloco']

        # Verifica se a sala está ocupada no mesmo dia da semana e horário
        if Alocacao.objects.filter(sala=sala, dia_semana=dia_semana, horario=horario, bloco=bloco).exists():
            raise serializers.ValidationError('A sala já está ocupada no mesmo dia e horário')

        # Verifica se o horário escolhido é válido
        if horario not in ['8:00-10:30', '10:30-12:00', '13:30-15:30', '15:30-17:30']:
            raise serializers.ValidationError('Horário inválido')

        return attrs


    #Logica 1


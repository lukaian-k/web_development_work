import json
import pandas as pd

#dicionario1 = {"Professor": "Eurinardo", "Disciplina": "PAA", "Sala": "5", "Bloco": "1A", "Horario": "8:00-10:00", "Semana": "Segunda"}

#with open("teste.json", "w") as arquivo:
    #json.dump(dicionario, arquivo)
    
#with open("teste.json", "r") as arquivo:
    #json_data = arquivo.read()

#dicionario = json.loads(json_data)

#print(dicionario)

r1 = {"Professor": "Eurinardo", "Disciplina": "PAA", "Sala": "5", "Bloco": "1A", "Horario": "8:00-10:00", "Semana": "Segunda"}
r2 = {"Professor": "Tatiane", "Disciplina": "ED", "Sala": "3", "Bloco": "2A", "Horario": "10:00-12:00", "Semana": "Terca"}
r3 = {"Professor": "Rafael Ivo", "Disciplina": "Computação Gráfica", "Sala": "3", "Bloco": "2A", "Horario": "13:30-15:30", "Semana": "Terca"}
r4 = {"Professor": "Eurinardo", "Disciplina": "LFA", "Sala": "1", "Bloco": "1A", "Horario": "08:10-10:00", "Semana": "Terca"}
r5 = {"Professor": "Eurinardo", "Disciplina": "PAA", "Sala": "5", "Bloco": "1A", "Horario": "8:00-10:00", "Semana": "Segunda"}
r6 = {"Professor": "Reuber", "Disciplina": "SO", "Sala": "5", "Bloco": "1A", "Horario": "8:00-10:00", "Semana": "Segunda"}
r7 = {"Professor": "Eurinardo", "Disciplina": "EDA", "Sala": "7", "Bloco": "2A", "Horario": "8:00-10:00", "Semana": "Segunda"}
r8 = {"Professor": "Eurinardo", "Disciplina": "PAA", "Sala": "5", "Bloco": "1A", "Horario": "8:00-10:00", "Semana": "Segunda"}

r9 = {"Professor": "Felipe", "Disciplina": "POO", "Sala": "4", "Bloco": "1A", "Horario": "8:00-10:00", "Semana": "Quarta"}
r10 = {"Professor": "Anderson", "Disciplina": "Algebra Linear", "Sala": "4", "Bloco": "1A", "Horario": "8:00-10:00", "Semana": "Quarta"}
r11 = {"Professor": "Eurinardo", "Disciplina": "EDA", "Sala": "4", "Bloco": "1A", "Horario": "13:30-15:30", "Semana": "Quarta"}
r12 = {"Professor": "Eurinardo", "Disciplina": "PAA", "Sala": "4", "Bloco": "2A", "Horario": "8:00-10:00", "Semana": "Segunda"}
r13 = {"Professor": "Alexandre", "Disciplina": "Lógica", "Sala": "4", "Bloco": "1A", "Horario": "15:30-17:30", "Semana": "Quarta"}
r14 = {"Professor": "Reuber", "Disciplina": "SD", "Sala": "4", "Bloco": "1A", "Horario": "10:00-12:00", "Semana": "Quarta"}

teste = [r1, r2, r3, r4]
teste2 = [r10, r11, r12]
teste3 = [r10, r11, r12, r13, r14]

#retorna_horarios_disponiveis(dicionario5)

df = pd.DataFrame(teste)
df2 = pd.DataFrame(teste2)
df3 = pd.DataFrame(teste3)


def verificar_registro_existente(df, novo_registro):
    registro_existente = df[df.eq(novo_registro).all(axis=1)].shape[0] > 0
    
    if registro_existente: # True
        return 1
    else:
        return 0 # False

def verificar_conflito_sala(df, registro):
    if len(df.loc[(df['Bloco'] == registro['Bloco']) & (df['Sala'] == registro['Sala']) & (df['Semana'] == registro['Semana']) & (df['Horario'] == registro['Horario'])]) == 0:
        return 0
    else:
       return 1
   
def verificar_conflito_horario(df, registro):
    if len(df.loc[(df['Professor'] == registro['Professor']) & (df['Semana'] == registro['Semana']) & (df['Horario'] == registro['Horario'])]) == 0:
        return 1
    else:
        return 0
    
def alocar_novo_registro(df, novo_registro):
    if verificar_registro_existente(df, novo_registro):
        print("Registro ja foi alocado anteriormente.")
    else: 
        if verificar_conflito_sala(df, novo_registro):
            print("A sala já esta sendo utilizada nesse dia e horário.")
        else:
            if verificar_conflito_horario(df, novo_registro):
                print("Aloacando registro.")
                df = pd.concat([df, pd.DataFrame([novo_registro])], ignore_index=True)
                print("Registro alocado com sucesso.")
            else:
                print("O mesmo professor já está ocupado esse horário.")
                
 
def horarios_disponiveis(df, novo_registro):
    filtro = df.loc[(df['Bloco'] == novo_registro['Bloco']) & (df['Sala'] == novo_registro['Sala']) & (df['Semana'] == novo_registro['Semana'])]
    horarios_preenchidos = filtro['Horario'].unique()
    print(f"Horários preenchidos: {horarios_preenchidos}")
    print(f"Horário requerido: {novo_registro['Horario']}")
    horarios_disponiveis = []
    
    horarios = ['8:00-10:00', '10:00-12:00', '13:30-15:30', '15:30-17:30']
    
    for horario in horarios:
        if horario not in horarios_preenchidos:
            horarios_disponiveis.append(horario)
    
    if novo_registro['Horario'] in horarios_disponiveis:
        print("Horário disponível")
    else:
        print("Esse horário não está disponível")
        if len(horarios_disponiveis) == 0:
            print("Não existem horários disponíveis para esse dia")
        else:
            print(f"Horários disponíveis: {horarios_disponiveis}")
        
 
#teste 1 Registro já alocado
#alocar_novo_registro(df, r5) 

#teste 2 Registro já está sendo utilizada
#alocar_novo_registro(df, r6) 

#teste 3 Professor já está ocupado nesse horário
#alocar_novo_registro(df, r7)

#teste 4 Mostrando horários disponíveis
#horarios_disponiveis(df2, r9)

#teste 5 nenhum horário disponível naquele dia
#horarios_disponiveis(df3, r9)


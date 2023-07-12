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
r2 = {"Professor": "Eurinardo", "Disciplina": "PAA", "Sala": "3", "Bloco": "1A", "Horario": "10:00-12:00", "Semana": "Quinta"}
r3 = {"Professor": "Eurinardo", "Disciplina": "PAA", "Sala": "4", "Bloco": "1A", "Horario": "13:30-15:30", "Semana": "Sexta"}
r4 = {"Professor": "Eurinardo", "Disciplina": "PAA", "Sala": "5", "Bloco": "1A", "Horario": "15:30-17:30", "Semana": "Terca"}
r5 = {"Professor": "Reuber", "Disciplina": "PAA", "Sala": "5", "Bloco": "1A", "Horario": "15:30-17:30", "Semana": "Terca"}


banco = [r1, r2, r3, r4]

#retorna_horarios_disponiveis(dicionario5)

df = pd.DataFrame(banco)

def verificar_registro_existente(df, novo_registro):
    registro_existente = df[df.eq(novo_registro).all(axis=1)].shape[0] > 0
    
    if registro_existente: # True
        return 1
    else:
        return 0 # False

def verificar_conflito_sala(df, registro):
    if len(df.loc[(df['Bloco']) == registro['Bloco'] & (df['Sala'] == registro['Sala']) & (df['Semana'] == registro['Semana']) & (df['Horario'] == registro['Horario'])]) == 0:
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
                
        
print(df)

alocar_novo_registro(df, r5)

    

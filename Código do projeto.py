import time
import smtplib
import sqlite3

def tempo():
    time.sleep(2)
    print("Hora de comer")
opcao = True
corrigi = 0

'''def criar_banco():
    # conectando...
    conn = sqlite3.connect('bank.db')
    # definindo um cursor
    cursor = conn.cursor()
    # criando a tabela (schema)
    cursor.execute("""
    CREATE TABLE banco (
            Alimento TEXT NOT NULL,
            Calorias INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT);
    """)
    # desconectando...
    conn.close()'''   #Caso o banco não estiver criado, usar essa função

def inserir_alimento():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    while True:
        # solicitando os dados ao usuário
        alimento = input('Nome do alimento: ')
        Cal = input('Calorias do ' + str(alimento)+ ':')

        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO banco (Alimento, Calorias)
        VALUES (?,?)
        """, (alimento, Cal))
        op = input('Deseja inserir mais alimentos? (Y/n) ')
        if op == 'y' or op == 'Y':
            continue
        else:
            break
    conn.commit()
    conn.close()

while opcao == True:
    print ("Bem vindo ao fitmode, primeiro vamos calcular a quantidade de calorias necessarias.")
    sexo = input("Qual seu sexo? \n1)mulher \n2)homem\n ")
    if sexo == 1:
        print("Bom, faremos algumas perguntas")
        nome = input("Qual o seu nome? ")
        idade = input ("Qual sua idade? ")
        totalCal= input ("Quantas calorias voce ingere em media diariamente(kcal)?: ")
        peso_inicial = input ("Qual o seu peso(kg)?: ")
        altura = input ("Qual a sua altura?(cm): ")
        atividade = input ("Com qual frequencia realiza atividades fisicas:\n 1)Sedentario\n 2)3 a 5 vezes por semana\n 3)atleta\n ")
        if atividade == 1:
            corrigi = 1.2
        elif atividade == 2:
            corrigi = 1.55
        elif atividade == 3:
            corrigi = 1.9
        Calorias =  (655 +(9.6*float(peso_inicial)))+(1.8*float((altura))-(4.7*float(idade)))*corrigi
        peso_perdido = ((float(totalCal) - float(Calorias))*15)/7000
        print ("O peso que voce ira perder, sera de aproximadamente :%f" %peso_perdido + "% do seu peso total")
    else:
        print("Bom, faremos algumas perguntas")
        nome = input("Qual o seu nome? ")
        idade = input ("Qual sua idade? ")
        totalCal= input ("Quantas calorias voce ingere em media diariamente(kcal)?: ")
        peso_inicial = input ("Qual o seu peso(kg)?: ")
        altura = input ("Qual a sua altura?(cm): ")
        atividade = input ("Com qual frequencia realiza atividades fisicas:\n 1)Sedentario\n 2)3 a 5 vezes por semana\n 3)atleta\n ")
        if atividade == 1:
            corrigi = 1.2
        elif atividade == 2:
            corrigi = 1.55
        elif atividade == 3:
            corrigi = 1.9
        Calorias = (66+(13.7*float(peso_inicial)))+((5*float(altura))-(6.8*float(idade)))*corrigi
        peso_perdido = ((float(totalCal)-float(Calorias))*15)/7000
        print ("O peso que voce perdera em duas semanas, sera de aproximadamente : %f "  %peso_perdido+ "% do seu peso total")
    op = input("Deseja: 1.ativar o alarme para refeições /n 2.Receber dicas por email  ")
    if op == '1':
        print("Alarme ativado")
        opcao = False
    elif op == '2':
        arquivo = open('Informações.txt', 'w')
        strin = "Nome: "+ str(nome)+ "\nIdade: "+ str(idade)+ "\nAltura: "+ str(altura)+ "\nPeso inicial: "+ str(peso_inicial)+ "\nPorcentagem de peso perdido em 2 semanas: "+ str(peso_perdido)+ "\n\n"
        arquivo.write(strin)
        info =('1 Coma a cada tres horas 2 varie o cardapio  3 Coma frutas')#INFORMAÇOES para emagrecer

        emailusuario = input('Qual o seu email?: ')

        # Credenciais

        remetente = 'trabalhoesof@gmail.com' #NÃO MUDAR ISSO
        senha = 'restaurante123' #NÃO MUDAR ISSO

        # Informações da mensagem
        destinatario = emailusuario
        assunto = 'Dicas para emagrecer'
        texto = info

        # Preparando a mensagem
        msg = '\r\n'.join([
            'From: %s' % remetente,
            'To: %s' % destinatario,
            'Subject: %s' % assunto,
            '',
            '%s' % texto
        ])

        # Enviando o email
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg)
        server.quit()

        print('Espaço reservado para cadastro de alimentos e suas calorias...')
        time.sleep(3)
        inserir_alimento()


        print("Volte daqui a duas semanas e continue seguindo seus exercícios! ")
        arquivo.close()
        time.sleep(3)
        break
    tempo()

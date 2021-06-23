# TODO: importa usuario criando neste projeto
import usuario as usr 

# TODO: importa os dicinários criados neste projeto
import dict_emprestimo as dtemp 

# TODO: importa o menu criado neste projeto
import menu as im_menu 

# TODO: esta biblioteca serve para limpar o terminal atraves de linha de comando
import os 

# TODO: esta biblioteca serve para criar um timer no terminal
import time 

# TODO: esta biblioteca neste caso serve para deletar uma linha do terminal
import sys

user1 = usr.user.user_1()
user2 = usr.user.user_2()
user3 = usr.user.user_3()
user4 = usr.user.user_4()
empr1 = dtemp.total_emprestimo.emprestimo_1()
empr2 = dtemp.total_emprestimo.emprestimo_2()
empr3 = dtemp.total_emprestimo.emprestimo_3()
empr4 = dtemp.total_emprestimo.emprestimo_4()


# TODO: esta função cria um temporizador no terminal
def timer():
    time.sleep(2) # coloca um temporizador no sistema

# TODO: esta função limpar o terminal
def tlimpa():
    os.system('cls' if os.name == 'nt' else 'clear') # limpa o terminal

# TODO: esta função verifica o score dos usuários e mostras as
#       oções de emprestimo certas para cada usuário
def lista_emprestimo(score):
    if (score >= 0 and score <= 300):
        im_menu.menu.menu_emprestimo2()
    elif (score > 300 and score < 700):
        im_menu.menu.menu_emprestimo3()
    elif (score >= 700 and score <= 1000):
        im_menu.menu.menu_emprestimo4()

# TODO: esta função calcula juros compostos
# fórmula: fv = pv*(1+i)**m
# fv = Future Value 
# pv = Present Value 
# i = Porcentagem de juros
# m = Parcelas
def calc_juros_compostos(valor, parcela, juros):
    # TODO: Montante = fv (furute value)
    porct_juros = juros
    valor_final = valor * ((1 + juros/100)**parcela)
    juros = valor_final - valor
    
    return  print(f''' 
            Valor do emprestimo: R${valor}
            Parcelas: {parcela} meses
            Juro Composto: {porct_juros}% a.m.
            Valor final: R${round(valor_final,2)}
            ''')
            # Juros: R${j}

# TODO: esta funão é usada para deletar a ultima linha do terminal
def delete_last_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

# TODO: esta função executa o projeto e valida as opções
def valida_opcao():
    while (True):
        im_menu.menu.menu_user()
        while (True):
            try:
                opcao = int(input("Escolha uma opção: "))
            except ValueError:
                delete_last_line()
                print("Opção inválida!")
                time.sleep(0.9)
                delete_last_line()
                continue

            mostra_user(opcao)
            
            if (opcao > 5 or opcao < 0):
                delete_last_line()
                print("Opção inválida!")
                time.sleep(0.9)
                delete_last_line()
                continue
            break
        if opcao == 5:
            tlimpa()
            print("Obrigado por usar o sistema.")
            break
        
# TODO: esta função faz todas a validações da escolha do usuário
def valida_opcao2(score_user):
    while(True):
        lista_emprestimo(score_user)
        while (True):
            try:
                opcao2 = int(input("Escolha uma opção: "))
            except ValueError:
                delete_last_line()
                print("Opção inválida!")
                time.sleep(0.9)
                delete_last_line()
                continue

            if (score_user >= 0 and score_user <= 300):
                if opcao2 == 5:
                    tlimpa()
                    break
                elif(opcao2 == 3 or opcao2 == 4):
                    delete_last_line()
                    print("Opção inválida!")
                    time.sleep(0.9)
                    delete_last_line()
                    continue
                elif (opcao2 > 5 or opcao2 < 0):
                    delete_last_line()
                    print("Opção inválida!")
                    time.sleep(0.9)
                    delete_last_line()
                    continue
            elif (score_user > 300 and score_user < 700):
                if opcao2 == 5:
                    tlimpa()    
                    break
                elif(opcao2 == 4):
                    delete_last_line()
                    print("Opção inválida!")
                    time.sleep(0.9)
                    delete_last_line()
                    continue
                elif (opcao2 > 5 or opcao2 < 0):
                    delete_last_line()
                    print("Opção inválida!")
                    time.sleep(0.9)
                    delete_last_line()
                    continue     
            elif (score_user >= 700 and score_user <= 1000):
                if opcao2 == 5:
                    tlimpa()
                    break
                elif (opcao2 > 5 or opcao2 < 0):
                    delete_last_line()
                    print("Opção inválida!")
                    time.sleep(0.9)
                    delete_last_line()
                    continue
            tlimpa()

            opcoes_emprestimo(opcao2, score_user)
            
            while (True):
                try:
                    continuar = str(input("Está certo este emprestimo?(Y/N)"))
                except ValueError:
                    print("Obrigado por fazer o emprestimo.")
                    break
                if (continuar == 'Y' or continuar == 'y'):
                    tlimpa()
                    print("Obrigado por fazer o emprestimo.")
                    break
                elif(continuar == 'N' or continuar == 'n'):
                    tlimpa()
                    break
                else:
                    delete_last_line()
                    print("Opção inválida!")
                    time.sleep(0.9)
                    delete_last_line()
                    continue
        
            if (continuar == 'Y' or continuar == 'y'):
                break
            elif(continuar == 'N' or continuar == 'n'):
                break
        if opcao2 == 5:
            break
        if (continuar == 'Y' or continuar == 'y'):
            break
        
    

# TODO: esta função fornece as opções de emprestimo formatada
def opcoes_emprestimo(opcao, score_user):
    if (opcao == 1):
        if (score_user >= 0 and score_user <= 300):
            print(''' 
                Emprestimo máximo: R$5000,00
                Parcela mínima: 2 meses
                Parcela máxima: 48 meses
                ''')
            while (True):
                try:
                    valor = float(input("Digite um valor: "))
                except ValueError:    
                        delete_last_line()
                        print("Valor inválido!")                    
                        time.sleep(0.9)
                        delete_last_line()
                        continue            
                if (valor > 5000 or valor <= 0):                    
                        delete_last_line()
                        print("Valor inválido!")                    
                        time.sleep(0.9)
                        delete_last_line()                    
                        continue 
                break

            while (True):
                try:
                    parcela = int(input("Quantidade de parcelas: "))

                except ValueError:    
                    delete_last_line()
                    print("Quantidade de parcelas inválidas!")
                    time.sleep(0.9)
                    delete_last_line()
                    continue
                if (parcela < 2 or parcela > 48):
                    delete_last_line()
                    print("Quantidade de parcelas inválidas!")
                    time.sleep(0.9)
                    delete_last_line()
                    continue
                break
            
            juros = 4 # 4%

            calc_juros_compostos(valor, parcela, juros)
            
        elif (score_user > 300 and score_user < 700):
            print(''' 
            Emprestimo máximo: R$10000,00
            Parcela mínima: 2 meses
            Parcela máxima: 60 meses
            ''')
            while (True):
                try:
                    valor = float(input("Digite um valor: "))
                except ValueError:    
                        delete_last_line()
                        print("Valor inválido!")                    
                        time.sleep(0.9)
                        delete_last_line()
                        continue            
                if (valor > 10000 or valor <= 0):                    
                        delete_last_line()
                        print("Valor inválido!")                    
                        time.sleep(0.9)
                        delete_last_line()                    
                        continue 
                break

            while (True):
                try:
                    parcela = int(input("Quantidade de parcelas: "))
                except ValueError:    
                    delete_last_line()
                    print("Quantidade de parcelas inválidas!")
                    time.sleep(0.9)
                    delete_last_line()
                    continue
                if (parcela < 2 or parcela > 60):
                    delete_last_line()
                    print("Quantidade de parcelas inválidas!")
                    time.sleep(0.9)
                    delete_last_line()
                    continue
                break
            
            if (valor == 10000):
                juros = 3 # 3% - diminui 1% acada R$5000,00
            else:
                juros = 4 # 4%
            
            calc_juros_compostos(valor, parcela, juros)
            
        elif (score_user >= 700 and score_user <= 1000):
            print(''' 
            Emprestimo máximo: R$15000,00
            Parcela mínima: 2 meses
            Parcela máxima: 60 meses
            ''')
            while (True):
                try:
                    valor = float(input("Digite um valor: "))
                except ValueError:    
                        delete_last_line()
                        print("Valor inválido!")                    
                        time.sleep(0.9)
                        delete_last_line()
                        continue            
                if (valor > 15000 or valor <= 0):                    
                        delete_last_line()
                        print("Valor inválido!")                    
                        time.sleep(0.9)
                        delete_last_line()                    
                        continue 
                break

            while (True):
                try:
                    parcela = int(input("Quantidade de parcelas: "))
                except ValueError:    
                    delete_last_line()
                    print("Quantidade de parcelas inválidas!")
                    time.sleep(0.9)
                    delete_last_line()
                    continue
                if (parcela < 2 or parcela > 60):
                    delete_last_line()
                    print("Quantidade de parcelas inválidas!")
                    time.sleep(0.9)
                    delete_last_line()
                    continue
                break
            
            # diminui 1% a cada R$5000,00 -> (Suposição)
            if (valor == 15000):
                juros = 2 # 2%
            elif (valor == 10000):
                juros = 3 # 3%
            else:
                juros = 4 # 4%
            
            calc_juros_compostos(valor, parcela, juros)            
    elif (opcao == 2):
        print(f'''
        {empr2["nome"]}
        Valor: {empr2["valor"]}
        Parcelas: {empr2["parcela"]}
        Juros: {empr2["juros"]}
        ''')
    elif (opcao == 3):
        print(f'''
        {empr3["nome"]}
        Valor: {empr3["valor"]}
        Parcelas: {empr3["parcela"]}
        Juros: {empr3["juros"]}
        ''')
    elif (opcao == 4):
        print(f'''
        {empr4["nome"]}
        Valor: {empr4["valor"]}
        Parcelas: {empr4["parcela"]}
        Juros: {empr4["juros"]}
        ''')

# TODO: esta função facilita o acesso para mostrar os users
def mostra_user(opcao):
    if opcao == 1:
        tlimpa()
        print(f'''
        Cliente: {user1["nome"]} {user1["sobrenome"]}
        Score: {user1["score"]}
        ''')
        valida_opcao2(user1["score"])            
    elif opcao == 2:
        tlimpa()
        print(f'''
        Cliente: {user2["nome"]} {user2["sobrenome"]}
        Score: {user2["score"]}
        ''')
        valida_opcao2(user2["score"])
    elif opcao == 3:
        tlimpa()
        print(f'''
        Cliente: {user3["nome"]} {user3["sobrenome"]}
        Score: {user3["score"]}
        ''')
        valida_opcao2(user3["score"])
    elif opcao == 4:
        tlimpa()
        print(f'''
        Cliente: {user4["nome"]} {user4["sobrenome"]}
        Score: {user4["score"]}
        ''')
        valida_opcao2(user4["score"])


# TODO: esta função serve para executar o projeto no arquivo run.py
def projeto():
    valida_opcao()

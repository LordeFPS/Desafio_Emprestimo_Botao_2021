from typing import cast
import usuario as usr
import dict_emprestimo as dtemp
import menu as im_menu
import os
import time

def timer():
    time.sleep(2) # coloca um temporizador no sistema

def tlimpa():
    os.system('cls' if os.name == 'nt' else 'clear') # limpa o terminal

user1 = usr.user.user_1()
user2 = usr.user.user_2()
user3 = usr.user.user_3()
user4 = usr.user.user_4()
empr1 = dtemp.total_emprestimo.emprestimo_1()
empr2 = dtemp.total_emprestimo.emprestimo_2()
empr3 = dtemp.total_emprestimo.emprestimo_3()
empr4 = dtemp.total_emprestimo.emprestimo_4()



# TODO: esta função verifica o saldo dos usuários e mostras as
#       oções de emprestimo certas para cada usuário
def lista_emprestimo(saldo):
    if (saldo < 0):
        im_menu.menu.menu_emprestimo1()
    elif (saldo > 0 and saldo <= 1000):
        im_menu.menu.menu_emprestimo2()
    elif (saldo > 1000 and saldo < 9000):
        im_menu.menu.menu_emprestimo3()
    else:
        im_menu.menu.menu_emprestimo4()

# TODO: esta função fornece as opções de emprestimo formatada
def opcoes_emprestimo(opcao):
    if (opcao == 1):
        print(f'''
        {empr1["nome"]}
        Valor: {empr1["valor"]}
        Parcelas: {empr1["parcela"]}
        Juros: {empr1["juros"]}
        ''')
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

# TODO: esta função faz todas a validações da escolha do usuário
def valida_opcao2(saldo_usuario):
    while (True):
        lista_emprestimo(saldo_usuario)
        
        try:
            opcao2 = int(input("Escolha uma opção: "))
        except ValueError:
            tlimpa()
            print("Opção inválida!")
            continue

        if (saldo_usuario == user1["saldo"]):
            if opcao2 == 5:
                break
            elif(opcao2 == 3 or opcao2 == 4):
                print("Opção inválida!")
                continue
            elif (opcao2 > 5 and opcao2 < 0):
                print("Opção inválida!")
                continue
            elif(opcao2 > 5):
                print("Opção inválida!")
                continue
        elif (saldo_usuario == user2["saldo"] or
            saldo_usuario == user4["saldo"]):
            if opcao2 == 5:
                break
            elif(opcao2 == 2 or opcao2 == 3 or opcao2 == 4):
                print("Opção inválida!")
                continue
            elif (opcao2 > 5 and opcao2 < 0):
                print("Opção inválida!")
                continue
            elif(opcao2 > 5):
                print("Opção inválida!")
                continue
        elif (saldo_usuario == user3["saldo"]):
            if opcao2 == 5:
                break
            elif (opcao2 > 5 and opcao2 < 0):
                print("Opção inválida!")
                continue
        tlimpa()

        opcoes_emprestimo(opcao2)

        continuar = input("Está certo este emprestimo?(Y/N)")

        while (True):
            if (continuar == 'Y' or continuar == 'y'):
                print("Obrigado por fazer o emprestimo.")
                break
            elif(continuar == 'N' or continuar == 'n'):
                tlimpa()
                break
            else:
                print("Opção inválida!")
                break
        if (continuar == 'Y' or continuar == 'y'):
            break
        
# TODO: esta função executa o projeto e valida as opções
def valida_opcao():
    while (True):
        im_menu.menu.menu_user()
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            tlimpa()
            print("Opção inválida!")
            continue
        
        if (opcao == str):
            print("Opção inválida!")
            continue

        if opcao == 1:
            tlimpa()
            
            print(f'''
            Cliente: {user1["nome"]} {user1["sobrenome"]}
            Saldo: {user1["saldo"]}
            ''')
            valida_opcao2(user1["saldo"])
                
        elif opcao == 2:
            tlimpa()
            print(f'''
            Cliente: {user2["nome"]} {user2["sobrenome"]}
            Saldo: {user2["saldo"]}
            ''')
            valida_opcao2(user2["saldo"])

        elif opcao == 3:
            tlimpa()
            print(f'''
            Cliente: {user3["nome"]} {user3["sobrenome"]}
            Saldo: {user3["saldo"]}
            ''')
            valida_opcao2(user3["saldo"])

        elif opcao == 4:
            tlimpa()
            print(f'''
            Cliente: {user4["nome"]} {user4["sobrenome"]}
            Saldo: {user4["saldo"]}
            ''')
            valida_opcao2(user4["saldo"])

        elif (opcao > 5 or opcao < 0):
            tlimpa()
            print("Opção inválida")
            continue

        elif opcao == 5:
            tlimpa()
            print("Obrigado por usar o sistema.")
            break

def projeto():
    valida_opcao()

# TODO: importa usuario criando neste projeto
import usuario as usr

# TODO: importa os dicinários criados neste projeto
import dict_emprestimo as dtemp 

# TODO: esta classe gera os opções de menus necessárias
class menu():
    def menu_emprestimo1():
        print(f'''
        *******************************
        **        Emprestimos        **
        *******************************
        ** 1 - {dtemp.total_emprestimo.emprestimo_1()["nome"]}     **
        ** 5 - Voltar                **
        *******************************
        ''')
    def menu_emprestimo2():
        print(f'''
        *******************************
        **        Emprestimos        **
        *******************************
        ** 1 - {dtemp.total_emprestimo.emprestimo_1()["nome"]}     **
        ** 2 - {dtemp.total_emprestimo.emprestimo_2()["nome"]}     **
        ** 5 - Voltar                **
        *******************************
        ''')

    def menu_emprestimo3():
        print(f'''
        *******************************
        **        Emprestimos        **
        *******************************
        ** 1 - {dtemp.total_emprestimo.emprestimo_1()["nome"]}     **
        ** 2 - {dtemp.total_emprestimo.emprestimo_2()["nome"]}     **
        ** 3 - {dtemp.total_emprestimo.emprestimo_3()["nome"]}     **
        ** 5 - Voltar                **
        *******************************
        ''')
    
    def menu_emprestimo4():
        print(f'''
        *******************************
        **        Emprestimos        **
        *******************************
        ** 1 - {dtemp.total_emprestimo.emprestimo_1()["nome"]}     **
        ** 2 - {dtemp.total_emprestimo.emprestimo_2()["nome"]}     **
        ** 3 - {dtemp.total_emprestimo.emprestimo_3()["nome"]}     **
        ** 4 - {dtemp.total_emprestimo.emprestimo_4()["nome"]}     **
        ** 5 - Voltar                **
        *******************************
        ''')
    
    def menu_user():
        print(f'''
        **********************
        **     Usuários     **
        **********************
        ** 1 - {usr.user.user_1()["nome"]}        **
        ** 2 - {usr.user.user_2()["nome"]}       **
        ** 3 - {usr.user.user_3()["nome"]}      **
        ** 4 - {usr.user.user_4()["nome"]}      **
        ** 5 - Sair         **
        **********************
        ''')
    



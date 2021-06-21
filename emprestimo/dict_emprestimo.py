# TODO: Esta classe serve como opções cadastro de emprestimos
#       e com possivel conexao com o DB

class total_emprestimo():
    def emprestimo_1():
        dict_1 = {
            "nome" : "Emprestimo: 10000",
            "valor" : 10000,
            "parcela" : "24x",
            "juros" : "Sem juros"
        }
        return dict_1

    def emprestimo_2():
        dict_2 = {
            "nome" : "Emprestimo: 50000",
            "valor" : 50000,
            "parcela" : "24x ou 36x",
            "juros" : "Sem juros"
        }
        return dict_2

    def emprestimo_3():
        dict_3 = {
            "nome" : "Emprestimo: 100000",
            "valor" : 100000,
            "parcela" : "48x",
            "juros" : "Sem juros"
        }
        return dict_3

    def emprestimo_4():
        dict_4 = {
            "nome" : "Emprestimo: 150000",
            "valor" : 150000,
            "parcela" : "48x",
            "juros" : "%0.1 ao ano"
            
        }
        return dict_4

    def emprestimo_full():
        dict_full = {
            "emprestimo_1" : total_emprestimo.emprestimo_1(),
            "emprestimo_2" : total_emprestimo.emprestimo_2(),
            "emprestimo_3" : total_emprestimo.emprestimo_3(),
            "emprestimo_4" : total_emprestimo.emprestimo_4()
        }
        return dict_full

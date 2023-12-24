from conta import Conta
    
if __name__ == "__main__":
    conta = Conta('123-4', 'João', 120.0, 1000.0)
    type(conta)

    print(conta.numero)
    print(conta.titular)

    conta.deposita(50.0)
    conta.extrato()
    conta.saca(20.0)
    conta.extrato()
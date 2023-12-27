# POO COM PYTHON

PROGRAMAÇÃO ORIENTADA A OBJETOS

## Conceito

| Termo      | Significado                                                                                                        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ |
| Classe     | Estrutura que define um tipo de objeto; modelo para criar instâncias (objetos); contém atributos e métodos         |
| Objeto     | Instância de uma classe; possui atributos (dados) e métodos (comportamentos) definidos pela classe.                |
| Atributo   | Característica que define um objeto em uma classe; representa dados específicos associados a uma instância         |
| Método     | Função associada a uma classe ou objeto; define comportamentos específicos que objetos dessa classe podem realizar |
| Construtor | Método especial (**init**) chamado automaticamente ao criar uma instância; inicializa atributos                    |
| Composição | Quando a existência de uma classe depende de outra classe dizemos que Esta associação chamamos de Composição       |
| Decoradores | Funções ou classes que modificam o comportamento de outras funções ou métodos.São aplicados usando a sintaxe @decorador acima da definição da função a ser decorada.|

### Exemplo:

'''python


    class Conta: # Classe Conta
        def __init__(self, numero, titular, saldo, limite): # Construtor __init__
            self.numero = numero # Atributo
            self.titular = titular
            self.saldo = saldo
            self.limite = limite

        def deposita(self, valor): # Método depositar()
            self.saldo += valor # Atributo

    conta = Conta('123-4', 'João', 120.0, 1000.0) # Instanciando uma classe
    type(conta)
    print(conta.numero)
    print(conta.titular)
    conta.deposita(50.0)
    '''

## Principais Métodos Especiais

| Método        | Funão                                                                         |
| ------------- | ----------------------------------------------------------------------------- |
| '**init**'    | Método construtor, chamado ao criar uma nova instância                        |
| '**str**'     | Retorna uma representação de string do objeto (para str(obj))                 |
| '**repr**'    | Retorna a representação "oficial" do objeto (para repr(obj))                  |
| '**len**'     | Retorna o comprimento do objeto (para len(obj))                               |
| '**getitem**' | Permite a indexação do objeto (para obj[indice])                              |
| '**setitem**' | Permite a atribuição de valor por índice (para obj[indice] = valor)           |
| "**delitem**" | Permite a exclusão de um item por índice (para del obj[indice]).              |
| '**iter**'    | Retorna um iterador para o objeto (para iter(obj))                            |
| '**next**'    | Utilizado para iteração (para next(iterador))                                 |
| '**eq**'      | Define o comportamento de igualdade (para obj1 == obj2)                       |
| '**ne**'      | Define o comportamento de desigualdade (para obj1 != obj2)                    |
| '**lt**'      | Define o comportamento de "menor que" (para obj1 < obj2)                      |
| '**le**'      | Define o comportamento de "menor ou igual que" (para obj1 <= obj2)            |
|  '**gt**'      | Define o comportamento de "maior que" (para obj1 > obj2)                      |
| '**ge**'      | Define o comportamento de "maior ou igual que" (para obj1 >= obj2)            |
| '**call**'    | Permite que uma instância da classe seja chamada como uma função (para obj()) |

## Encapsulamento
Um dos pilares da POO, o Encapsulamento, segundo o qual procuramos esconder de clientes (usuários de uma classe) todas as informação que não são necessárias ao uso da classe.

Por exemplo, suponha que precisássemos criar uma classe para armazenar informações de funcionários de uma empresa, como ilustrado no exemplo abaixo.
    
    class Funcionario:
        def __init__(self, nome, cargo, valor_hora_trabalhada):
            self.nome = nome
            self.cargo = cargo
            self.valor_hora_trabalhada = valor_hora_trabalhada
            self.horas_trabalhadas = 0
            self.salario = 0

        def registra_hora_trabalhada(self):
            self.horas_trabalhadas += 1

        def calcula_salario(self):
            self.salario = self.horas_trabalhadas * self.valor_hora_trabalhada
O problema no código acima surge pela possibilidade do usuário poder modificar dados como _salario_ sem o uso da correta função _calcula_salario()_. Para isso, podemos restringir a visibilidade de variáveis e métodos de uma classe, por meio de convenções de nome (uso do __ ) e de outros recursos como decoradores (@property).

    @property
        def salario(self): 
            return self.__salario

        @salario.setter
        def salario(self, novo_salario): 
            raise ValueError("Impossivel alterar salario diretamente. Use a funcao calcula_salario().")
1. Criamos uma propriedade salario
2. Restringimos acesso à propriedade salário e instruímos os clientes a alterarem o valor da variável salario usando a função calcula_salario().
3. Uma tentativa de alterar a propriedade salario sem usar a função calcula_salario() resulta em um erro.

Python nos permite também criar variáveis ou métodos que são visíveis somente na classe e em classes dela derivadas. A convenção é que variáveis ou métodos cujo nome começa com _ (um underscore apenas) são visíveis em uma hierarquia de classes, ou seja, na classe base e nas classes derivadas, mas não devem ser acessados fora destes casos.
## Herança
## Polimorfismo

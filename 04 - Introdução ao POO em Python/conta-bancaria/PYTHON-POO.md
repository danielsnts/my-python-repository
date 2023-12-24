# POO COM PYTHON
PROGRAMAÇÃO ORIENTADA A OBJETOS 
## Conceito
| Termo | Significado |
| ----- | ----------- |
| Classe |Estrutura que define um tipo de objeto; modelo para criar instâncias (objetos); contém atributos e métodos |
| Objeto |Instância de uma classe; possui atributos (dados) e métodos (comportamentos) definidos pela classe.|
| Atributo | Característica que define um objeto em uma classe; representa dados específicos associados a uma instância |
| Método | Função associada a uma classe ou objeto; define comportamentos específicos que objetos dessa classe podem realizar |
| Construtor| Método especial (__init__) chamado automaticamente ao criar uma instância; inicializa atributos |
| Composição | Quando a existência de uma classe depende de outra classe  dizemos  que Esta  associação chamamos de Composição |

### Exemplo:
'''python
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

conta = Conta('123-4', 'João', 120.0, 1000.0)
    type(conta)

    print(conta.numero)
    print(conta.titular)

    conta.deposita(50.0)
 '''

## Principais Métodos Especiais
| Método | Funão |
| ----- | ----------- |
| __init__ | Método construtor, chamado ao criar uma nova instância |
| __str__ | Retorna uma representação de string do objeto (para str(obj)) |
| __repr__ | Retorna a representação "oficial" do objeto (para repr(obj)) |
| __len__ | Retorna o comprimento do objeto (para len(obj)) |
| __getitem__ | Permite a indexação do objeto (para obj[indice]) |
| __setitem__ | Permite a atribuição de valor por índice (para obj[indice] = valor) |
| __delitem__ | Permite a exclusão de um item por índice (para del obj[indice]).
| __iter__ | Retorna um iterador para o objeto (para iter(obj)) |
| __next__ | Utilizado para iteração (para next(iterador)) |
| __eq__ | Define o comportamento de igualdade (para obj1 == obj2) |
| __ne__ | Define o comportamento de desigualdade (para obj1 != obj2) |
| __lt__ | Define o comportamento de "menor que" (para obj1 < obj2) |
| __le__ | Define o comportamento de "menor ou igual que" (para obj1 <= obj2) |
| __gt__ | Define o comportamento de "maior que" (para obj1 > obj2) |
| __ge__ | Define o comportamento de "maior ou igual que" (para obj1 >= obj2) |
| __call__ | Permite que uma instância da classe seja chamada como uma função (para obj()) |
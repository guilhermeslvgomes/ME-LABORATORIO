from calculadora import somar, subtrair, multiplicar, dividir, historico

def setup_function():
    # garantindo que o "historico" esteja vazio antes de cada teste
    historico.clear()


def test_somar():
    assert somar(2, 3) == 5
    assert historico[-1] == "2 + 3 = 5"


def test_subtrair():
    assert subtrair(5, 2) == 3
    assert historico[-1] == "5 - 2 = 3"


def test_multiplicar():
    assert multiplicar(4, 3) == 12
    assert historico[-1] == "4 * 3 = 12"


def test_dividir():
    assert dividir(10, 2) == 5
    assert historico[-1] == "10 / 2 = 5.0"


def test_divisao_por_zero():
    assert dividir(10, 0) == "Erro: divisão por zero!"


def test_historico_varias_operacoes():
    somar(1, 1)
    subtrair(5, 3)

    assert len(historico) == 2
test_jogo.py
from jogo_sorte import jogar

def test_jogo():
    resultados = [jogar() for _ in range(10)]
    assert True in resultados, "Nenhuma vitória em 10 tentativas!"

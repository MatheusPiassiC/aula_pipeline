from script import soma

def test_soma_numeros_positivos():
    assert soma(2, 3) == 5

def test_soma_com_numero_negativo():
    assert soma(-2, 5) == 3

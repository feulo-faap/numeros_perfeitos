import perfeitos

def test_6_perfeito():
    assert perfeitos.eh_perfeito(6) #Act

def test_8_n_perfeito():
    assert not perfeitos.eh_perfeito(8) #Act

def test_10_n_perfeito():
    numero = 10 #Arrange
    resultado = perfeitos.eh_perfeito(numero) #Act
    assert resultado == False
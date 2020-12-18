def MinMax(temperaturas):
	print("A menor temperatura do mês, foi: ", mínima(temperaturas), "C.")
	print("A maior temperatura do mês, foi: ", máxima(temperaturas), "C.")


def máxima(temps):
	max = temps[0]
	i = 1
	while i < len(temps):
		if temps[i] > max: 
			max = temps[i]
		i = i + 1
	return max

def mínima(temps):
	min = temps[0]
	i = 1
	while i < len(temps):
		if temps[i] < min: 
			min = temps[i]
		i = i + 1
	return min

def teste_pontual(temp, valor_esperado):
	valor_calculado = mínima(temp)
	if valor_calculado != valor_esperado:
		print("Valor errado para array", temp)
		print(f"O valor esperado era: {valor_esperado}. Valor calculado: {valor_calculado}")
	
def testa_mínima():
	print("Iniciando os testes")
	teste_pontual([0], 0)
	teste_pontual([0, 0, 0, 0, 0], 0)
	teste_pontual([1, 2, 3, 4, 5, 6, 7, 8, 9], 1)
	teste_pontual([1, -1, -14, -15, -22], -22)

MinMax([22, 33, 23, 22, 26, 28])
from Calculadora import Calculadora

calc = Calculadora()
calc.valorA = 40
calc.valorB = 20
calc.operacao = '+'

calc.mostrarResultado()
resultado = calc.calcular()
print(f"Resultado: {resultado}")

calc.operacao = '-'
calc.mostrarResultado()
resultado = calc.calcular()
print(f"resultado: {resultado}")

calc.operacao = '*'
calc.mostrarResultado()
resultado = calc.calcular()
print(f"resultado: {resultado}")

calc.operacao = '/'
calc.mostrarResultado()
resultado = calc.calcular()
print(f"resultado: {resultado}")


calc.valorB = 0
try:
    resultado = calc.calcular()
except SystemExit as e:
    print("tentativa de divisão por 0 detectada")
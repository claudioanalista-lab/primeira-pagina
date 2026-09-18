#FORMAS OBRIGATORIAS
#1 - Círculo
#2 - Triangulo
#3 - Quadrado
#4 - Retangulo
#5 - Paralelogramo
#6 - Losango
#7 - Trapezio

PI = 3.141591

def calcular_area_circulo(raio):
    return PI * (raio ** 2)

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_quadrado(lado):
    return lado ** 2

def calcular_area_retangulo(base, altura):
    return base * altura

def calcular_area_paralelogramo(base, altura):
    return base * altura

def calcular_area_losango(diagonal_maior, diagonal_menor):
    return (diagonal_maior * diagonal_menor) / 2

def calcular_area_trapezio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2

def main():
    while True:
        print("\n=== CALCULADORA DE ÁREAS DE FORMAS GEOMÉTRICAS ===")
        print("1 - Círculo")
        print("2 - Triângulo")
        print("3 - Quadrado")
        print("4 - Retângulo")
        print("5 - Paralelogramo")
        print("6 - Losango")
        print("7 - Trapézio")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção (0-7): ")

        if opcao == '1':
            raio = float(input("Digite o raio do círculo: "))
            area = calcular_area_circulo(raio)
            print(f"A área do círculo é: {area:.2f}")
        elif opcao == '2':
            base = float(input("Digite a base do triângulo: "))
            altura = float(input("Digite a altura do triângulo: "))
            area = calcular_area_triangulo(base, altura)
            print(f"A área do triângulo é: {area:.2f}")
        elif opcao == '3':
            lado = float(input("Digite o lado do quadrado: "))
            area = calcular_area_quadrado(lado)
            print(f"A área do quadrado é: {area:.2f}")
        elif opcao == '4':
            base = float(input("Digite a base do retângulo: "))
            altura = float(input("Digite a altura do retângulo: "))
            area = calcular_area_retangulo(base, altura)
            print(f"A área do retângulo é: {area:.2f}")
        elif opcao == '5':
            base = float(input("Digite a base do paralelogramo: "))
            altura = float(input("Digite a altura do paralelogramo: "))
            area = calcular_area_paralelogramo(base, altura)
            print(f"A área do paralelogramo é: {area:.2f}")
        elif opcao == '6':
            d_maior = float(input("Digite a diagonal maior do losango: "))
            d_menor = float(input("Digite a diagonal menor do losango: "))
            area = calcular_area_losango(d_maior, d_menor)
            print(f"A área do losango é: {area:.2f}")
        elif opcao == '7':
            b_maior = float(input("Digite a base maior do trapézio: "))
            b_menor = float(input("Digite a base menor do trapézio: "))
            altura = float(input("Digite a altura do trapézio: "))
            area = calcular_area_trapezio(b_maior, b_menor, altura)
            print(f"A área do trapézio é: {area:.2f}")
        elif opcao == '0':
            print("Saindo do programa... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

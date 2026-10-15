def sumar(num1: float, num2: float) -> float:
    """
    Sumar dos números

    :param num1: primer número a sumar
    :param num2: segundo número a sumar
    
    :return: resultado de la suma
    """
    res = num1 + num2
    return res

def restar(num1: float, num2: float) -> float:
    """
    Restar dos números

    :param num1: primer número a restar
    :param num2: segundo número a restar
    
    :return: resultado de la resta
    """
    res = num1 - num2
    return res

def multiplicar(num1: float, num2: float) -> float:
    """
    Multiplicar dos números
    
    :param num1: primer número de la multiplicación
    :param num2: segundo número de la multiplicación
        
    :return: resultado de la multiplicación
    """
    res = num1 * num2
    return res

def dividir(num1: float, num2: float) -> float:
    """
    Dividir dos números
        
    :param num1: primer número de la división
    :param num2: segundo número de la división
            
    :return: resultado de la división
    """

    if num2 == 0:
        print("No se puede realizar la operación")
        print(f"División: {dividir}")
    res = num1 / num2
    return res

def main():
    num1: float = float(input(""))
    num2: float = float(input(""))
    print(f"Suma: {sumar(num1,num2):.1f}")
    print(f"Resta: {restar(num1,num2):.1f}")
    print(f"Multiplicación: {multiplicar(num1,num2):.1f}")
    print(f"División: {dividir(num1, num2):.1f}")

if __name__ == "__main__":
    main()
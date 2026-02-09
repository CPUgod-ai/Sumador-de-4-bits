# COMPUERTAS LOGICAS 

def AND(a, b):
    # devuelve True solo si a y b son True
    return a and b

def OR(a, b):
    # Simula la compuerta OR:
    # devuelve True si al menos uno es True
    return a or b
def NOT(a):
    # Simula la compuerta NOT:
    # invierte el valor logico
    return not a


def XOR(a, b):
    return OR(
        AND(a, NOT(b)),      # Caso: a = 1 y b = 0
        AND(NOT(a), b)       # Caso: a = 0 y b = 1
    )

# HALF ADDER 
# Suma dos bits sin acarreo de entrada

def half_adder(a, b):
    # La suma se obtiene con XOR
    suma = XOR(a, b)

    # El acarreo se obtiene con AND
    carry = AND(a, b)

    # Retorna suma y acarreo
    return suma, carry

#  FULL ADDER 
# Suma dos bits considerando acarreo de entrada

def full_adder(a, b, cin):
    # Se suma primero a y b
    s1, c1 = half_adder(a, b)

    # Luego se suma el resultado con el acarreo de entrada
    s2, c2 = half_adder(s1, cin)

    # El acarreo final es la OR de los acarreos anteriores
    cout = OR(c1, c2)

    # Retorna la suma final y el acarreo de salida
    return s2, cout


# -SUMADOR DE 4 BITS 
# A y B son listas de 4 bits (False = 0, True = 1)

def sumador_4_bits(A, B, cin=False):
    # Lista donde se almacenara el resultado
    S = [False, False, False, False]

    # Acarreo inicial
    carry = cin

    # Se comienza desde el bit menos significativo
    S[3], carry = full_adder(A[3], B[3], carry)

    # Se continua con los siguientes bits
    S[2], carry = full_adder(A[2], B[2], carry)
    S[1], carry = full_adder(A[1], B[1], carry)
    S[0], carry = full_adder(A[0], B[0], carry)

    # Se retorna el resultado y el acarreo final
    return S, carry


def complemento_a_2(B):
    # PASO 1: Invertir bits (NOT). El 0 se vuelve 1 y el 1 se vuelve 0.
    Bn = [
        NOT(B[0]),
        NOT(B[1]),
        NOT(B[2]),
        NOT(B[3])
    ]

    # Representación del número 1 en binario (4 bits)
    uno = [False, False, False, True]

    # PASO 2: Sumar 1 al número invertido para obtener el Complemento a 2
    R, _ = sumador_4_bits(Bn, uno)

    return R


# ---------------- RESTADOR DE 4 BITS ----------------
# A - B = A + (complemento a 2 de B)

def restador_4_bits(A, B):
    # Se calcula el complemento a 2 de B
    Bc = complemento_a_2(B)

    # Se suma A con el complemento a 2 de B
    R, carry = sumador_4_bits(A, Bc)

    # Se retorna el resultado de la resta
    return R, carry


#   TABLA DE VERDAD 
# Tabla de verdad del Full Adder (bloque base)

def tabla_verdad_full_adder():
    print("\nTABLA DE VERDAD - FULL ADDER")
    print("A B Cin | S Cout")
    print("----------------")

    # Valores posibles para los bits
    valores = [False, True]

    # Se recorren todas las combinaciones posibles
    for a in valores:
        for b in valores:
            for cin in valores:
                # Se calcula la salida del full adder
                s, cout = full_adder(a, b, cin)

                # Se imprime la combinacion
                print(
                    int(a), int(b), int(cin),
                    " | ",
                    int(s), int(cout)
                )

if __name__ == "__main__":

    # Definicion de numeros binarios de 4 bits
    # False = 0, True = 1
    A = [False, True, False, True]   # 0101
    B = [False, False, True, True]   # 0011

    # Se calcula la suma
    suma, carry_s = sumador_4_bits(A, B)

    # Se calcula la resta
    resta, carry_r = restador_4_bits(A, B)

    # Se muestran los resultados
    print("A =", A)
    print("B =", B)
    print("Suma =", suma, "Carry =", carry_s)
    print("Resta =", resta, "Carry =", carry_r)

    # Se muestra la tabla de verdad al final
    tabla_verdad_full_adder()

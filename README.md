# 🔢 Sumador y Restador Binario de 4 Bits

Este proyecto implementa un **sumador y un restador binario de 4 bits** en Python,
simulando el comportamiento de **circuitos de electrónica digital**.

La lógica del programa se construye **exclusivamente utilizando las compuertas
AND, OR y NOT**, respetando estrictamente la restricción académica del ejercicio.

---

## 📌 Restricción principal

Durante la implementación **NO se utilizan**:
- Operadores aritméticos (`+`, `-`)
- XOR nativo
- Comparaciones (`==`, `<`, `>`)
- Operadores binarios propios de Python

La lógica del circuito usa únicamente:
- AND
- OR
- NOT

---

## 🧠 ¿Cómo funciona el programa?

### ➕ Suma binaria
- La suma se realiza **bit a bit**, iniciando desde el bit menos significativo.
- Cada operación se lleva a cabo mediante un **Full Adder**.
- El **acarreo** se transfiere al siguiente bit, como en un circuito real.

### ➖ Resta binaria
- La resta se implementa utilizando el **complemento a 2**.
- Se invierten los bits del segundo número (NOT).
- Se suma 1 al resultado.
- Finalmente, se suma este valor al primer número usando el mismo sumador de 4 bits.

---

## 🧩 Descripción general del código

El código está organizado de forma modular, representando bloques de un circuito digital:

- **Compuertas lógicas**: funciones AND, OR y NOT.
- **XOR lógico**: construido únicamente con compuertas básicas.
- **Half Adder**: suma dos bits sin considerar acarreo de entrada.
- **Full Adder**: suma dos bits teniendo en cuenta el acarreo.
- **Sumador de 4 bits**: encadena cuatro Full Adders.
- **Complemento a 2**: permite realizar la resta binaria.
- **Restador de 4 bits**: reutiliza el sumador para calcular A − B.
- **Tabla de verdad**: se muestra la tabla de verdad del Full Adder.

Los bits se representan de la siguiente manera:
- `False` → 0
- `True` → 1

---

## ▶️ Cómo compilar / ejecutar el programa

> Python no se compila, se **ejecuta directamente**.

### Requisitos
- Tener **Python 3** instalado.

### Pasos para ejecutar

1. Abrir una terminal o consola.
2. Ubicarse en la carpeta donde se encuentra el archivo usando el comando `cd`.

Ejemplo en Windows:

```bash
cd Documents
cd ProyectoLogica

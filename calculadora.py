#!/usr/bin/env python3
"""
Calculadora Completa - Resuelve operaciones matemáticas básicas y avanzadas
Autor: GitHub Copilot
"""

import math
import re
from typing import Union, List, Tuple

class Calculadora:
    """Clase para realizar cálculos matemáticos complejos"""
    
    def __init__(self):
        self.historial = []
        self.variables = {}
    
    # ==================== OPERACIONES BÁSICAS ====================
    def sumar(self, *numeros) -> float:
        """Suma múltiples números"""
        resultado = sum(numeros)
        self.registrar_operacion(f"Suma: {' + '.join(map(str, numeros))} = {resultado}")
        return resultado
    
    def restar(self, a: float, b: float) -> float:
        """Resta dos números"""
        resultado = a - b
        self.registrar_operacion(f"Resta: {a} - {b} = {resultado}")
        return resultado
    
    def multiplicar(self, *numeros) -> float:
        """Multiplica múltiples números"""
        resultado = 1
        for num in numeros:
            resultado *= num
        self.registrar_operacion(f"Multiplicación: {' × '.join(map(str, numeros))} = {resultado}")
        return resultado
    
    def dividir(self, a: float, b: float) -> float:
        """Divide dos números"""
        if b == 0:
            raise ValueError("❌ Error: No se puede dividir entre cero")
        resultado = a / b
        self.registrar_operacion(f"División: {a} ÷ {b} = {resultado}")
        return resultado
    
    def modulo(self, a: float, b: float) -> float:
        """Obtiene el residuo de la división"""
        if b == 0:
            raise ValueError("❌ Error: Módulo entre cero no permitido")
        resultado = a % b
        self.registrar_operacion(f"Módulo: {a} % {b} = {resultado}")
        return resultado
    
    # ==================== OPERACIONES AVANZADAS ====================
    def potencia(self, base: float, exponente: float) -> float:
        """Calcula base elevada a exponente"""
        resultado = base ** exponente
        self.registrar_operacion(f"Potencia: {base}^{exponente} = {resultado}")
        return resultado
    
    def raiz_cuadrada(self, numero: float) -> float:
        """Calcula la raíz cuadrada"""
        if numero < 0:
            raise ValueError("❌ Error: No se puede calcular raíz cuadrada de números negativos")
        resultado = math.sqrt(numero)
        self.registrar_operacion(f"Raíz cuadrada: √{numero} = {resultado}")
        return resultado
    
    def raiz_n(self, numero: float, n: float) -> float:
        """Calcula la raíz n-ésima"""
        if numero < 0 and n % 2 == 0:
            raise ValueError("❌ Error: Raíz par de número negativo no permitida")
        resultado = numero ** (1/n)
        self.registrar_operacion(f"Raíz {n}: {numero}^(1/{n}) = {resultado}")
        return resultado
    
    def factorial(self, n: int) -> int:
        """Calcula el factorial de n"""
        if n < 0:
            raise ValueError("❌ Error: No existe factorial de números negativos")
        resultado = math.factorial(n)
        self.registrar_operacion(f"Factorial: {n}! = {resultado}")
        return resultado
    
    # ==================== TRIGONOMETRÍA ====================
    def seno(self, angulo: float, en_grados: bool = True) -> float:
        """Calcula el seno de un ángulo"""
        rad = math.radians(angulo) if en_grados else angulo
        resultado = math.sin(rad)
        unidad = "grados" if en_grados else "radianes"
        self.registrar_operacion(f"Seno: sin({angulo}°) = {resultado}")
        return resultado
    
    def coseno(self, angulo: float, en_grados: bool = True) -> float:
        """Calcula el coseno de un ángulo"""
        rad = math.radians(angulo) if en_grados else angulo
        resultado = math.cos(rad)
        self.registrar_operacion(f"Coseno: cos({angulo}°) = {resultado}")
        return resultado
    
    def tangente(self, angulo: float, en_grados: bool = True) -> float:
        """Calcula la tangente de un ángulo"""
        rad = math.radians(angulo) if en_grados else angulo
        resultado = math.tan(rad)
        self.registrar_operacion(f"Tangente: tan({angulo}°) = {resultado}")
        return resultado
    
    # ==================== ESTADÍSTICA ====================
    def promedio(self, *numeros) -> float:
        """Calcula el promedio de números"""
        if not numeros:
            raise ValueError("❌ Error: Debes proporcionar al menos un número")
        resultado = sum(numeros) / len(numeros)
        self.registrar_operacion(f"Promedio: {resultado}")
        return resultado
    
    def mediana(self, *numeros) -> float:
        """Calcula la mediana"""
        if not numeros:
            raise ValueError("❌ Error: Debes proporcionar al menos un número")
        sorted_nums = sorted(numeros)
        n = len(sorted_nums)
        if n % 2 == 0:
            resultado = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
        else:
            resultado = sorted_nums[n//2]
        self.registrar_operacion(f"Mediana: {resultado}")
        return resultado
    
    def desviacion_estandar(self, *numeros) -> float:
        """Calcula la desviación estándar"""
        if len(numeros) < 2:
            raise ValueError("❌ Error: Se necesitan al menos 2 números")
        media = sum(numeros) / len(numeros)
        varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
        resultado = math.sqrt(varianza)
        self.registrar_operacion(f"Desviación estándar: {resultado}")
        return resultado
    
    # ==================== LOGARITMOS ====================
    def logaritmo_natural(self, numero: float) -> float:
        """Calcula el logaritmo natural (ln)"""
        if numero <= 0:
            raise ValueError("❌ Error: El logaritmo solo funciona con números positivos")
        resultado = math.log(numero)
        self.registrar_operacion(f"Logaritmo natural: ln({numero}) = {resultado}")
        return resultado
    
    def logaritmo_base10(self, numero: float) -> float:
        """Calcula el logaritmo en base 10"""
        if numero <= 0:
            raise ValueError("❌ Error: El logaritmo solo funciona con números positivos")
        resultado = math.log10(numero)
        self.registrar_operacion(f"Logaritmo base 10: log({numero}) = {resultado}")
        return resultado
    
    def logaritmo(self, numero: float, base: float) -> float:
        """Calcula el logaritmo en cualquier base"""
        if numero <= 0 or base <= 0:
            raise ValueError("❌ Error: El logaritmo solo funciona con números positivos")
        if base == 1:
            raise ValueError("❌ Error: La base no puede ser 1")
        resultado = math.log(numero, base)
        self.registrar_operacion(f"Logaritmo base {base}: log({numero}) = {resultado}")
        return resultado
    
    # ==================== UTILIDADES ====================
    def valor_absoluto(self, numero: float) -> float:
        """Calcula el valor absoluto"""
        resultado = abs(numero)
        self.registrar_operacion(f"Valor absoluto: |{numero}| = {resultado}")
        return resultado
    
    def redondear(self, numero: float, decimales: int = 0) -> float:
        """Redondea a n decimales"""
        resultado = round(numero, decimales)
        self.registrar_operacion(f"Redondeo: {numero} → {resultado}")
        return resultado
    
    def convertir_a_porcentaje(self, numero: float, total: float) -> float:
        """Calcula el porcentaje"""
        if total == 0:
            raise ValueError("❌ Error: El total no puede ser cero")
        resultado = (numero / total) * 100
        self.registrar_operacion(f"Porcentaje: {numero}/{total} = {resultado}%")
        return resultado
    
    # ==================== HISTORIAL ====================
    def registrar_operacion(self, operacion: str):
        """Registra una operación en el historial"""
        self.historial.append(operacion)
    
    def ver_historial(self):
        """Muestra el historial de operaciones"""
        if not self.historial:
            print("\n📋 El historial está vacío\n")
            return
        print("\n" + "="*50)
        print("📋 HISTORIAL DE OPERACIONES")
        print("="*50)
        for i, op in enumerate(self.historial, 1):
            print(f"{i}. {op}")
        print("="*50 + "\n")
    
    def limpiar_historial(self):
        """Limpia el historial"""
        self.historial.clear()
        print("✅ Historial limpiado")


# ==================== INTERFAZ DE USUARIO ====================
def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("🧮 CALCULADORA COMPLETA - MENÚ PRINCIPAL")
    print("="*60)
    print("1.  ➕ Suma")
    print("2.  ➖ Resta")
    print("3.  ✖️  Multiplicación")
    print("4.  ➗ División")
    print("5.  🔢 Módulo")
    print("6.  ⬆️  Potencia")
    print("7.  √ Raíz cuadrada")
    print("8.  ∛ Raíz n-ésima")
    print("9.  ! Factorial")
    print("10. 📐 Seno")
    print("11. 📐 Coseno")
    print("12. 📐 Tangente")
    print("13. 📊 Promedio")
    print("14. 📊 Mediana")
    print("15. 📊 Desviación estándar")
    print("16. ln Logaritmo natural")
    print("17. log Logaritmo base 10")
    print("18. log Logaritmo (cualquier base)")
    print("19. || Valor absoluto")
    print("20. ≈ Redondear")
    print("21. % Porcentaje")
    print("22. 📋 Ver historial")
    print("23. 🗑️  Limpiar historial")
    print("0.  ❌ Salir")
    print("="*60)


def obtener_numeros(cantidad: int = 1, prompt: str = "Ingresa un número: ") -> List[float]:
    """Obtiene números del usuario"""
    numeros = []
    for i in range(cantidad):
        while True:
            try:
                if cantidad > 1:
                    num = float(input(f"{prompt} ({i+1}/{cantidad}): "))
                else:
                    num = float(input(prompt))
                numeros.append(num)
                break
            except ValueError:
                print("❌ Error: Ingresa un número válido")
    return numeros


def main():
    """Función principal"""
    calc = Calculadora()
    
    print("\n🎉 Bienvenido a la CALCULADORA COMPLETA")
    print("✨ Diseñada para resolver todo tipo de operaciones matemáticas\n")
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()
        
        try:
            if opcion == "0":
                print("\n👋 ¡Hasta luego! Gracias por usar la calculadora.\n")
                break
            
            elif opcion == "1":
                print("\n➕ SUMA")
                n = int(input("¿Cuántos números deseas sumar?: "))
                nums = obtener_numeros(n)
                print(f"✅ Resultado: {calc.sumar(*nums)}\n")
            
            elif opcion == "2":
                print("\n➖ RESTA")
                a, b = obtener_numeros(2, "Número")
                print(f"✅ Resultado: {calc.restar(a, b)}\n")
            
            elif opcion == "3":
                print("\n✖️  MULTIPLICACIÓN")
                n = int(input("¿Cuántos números deseas multiplicar?: "))
                nums = obtener_numeros(n)
                print(f"✅ Resultado: {calc.multiplicar(*nums)}\n")
            
            elif opcion == "4":
                print("\n➗ DIVISIÓN")
                a, b = obtener_numeros(2, "Número")
                print(f"✅ Resultado: {calc.dividir(a, b)}\n")
            
            elif opcion == "5":
                print("\n🔢 MÓDULO")
                a, b = obtener_numeros(2, "Número")
                print(f"✅ Resultado: {calc.modulo(a, b)}\n")
            
            elif opcion == "6":
                print("\n⬆️  POTENCIA")
                base, exp = obtener_numeros(2, "Valor")
                print(f"✅ Resultado: {calc.potencia(base, exp)}\n")
            
            elif opcion == "7":
                print("\n√ RAÍZ CUADRADA")
                num = obtener_numeros(1)[0]
                print(f"✅ Resultado: {calc.raiz_cuadrada(num)}\n")
            
            elif opcion == "8":
                print("\n∛ RAÍZ N-ÉSIMA")
                num, n = obtener_numeros(2, "Valor")
                print(f"✅ Resultado: {calc.raiz_n(num, n)}\n")
            
            elif opcion == "9":
                print("\n! FACTORIAL")
                num = int(obtener_numeros(1)[0])
                print(f"✅ Resultado: {calc.factorial(num)}\n")
            
            elif opcion == "10":
                print("\n📐 SENO")
                angulo = obtener_numeros(1, "Ángulo en grados")[0]
                print(f"✅ Resultado: {calc.seno(angulo)}\n")
            
            elif opcion == "11":
                print("\n📐 COSENO")
                angulo = obtener_numeros(1, "Ángulo en grados")[0]
                print(f"✅ Resultado: {calc.coseno(angulo)}\n")
            
            elif opcion == "12":
                print("\n📐 TANGENTE")
                angulo = obtener_numeros(1, "Ángulo en grados")[0]
                print(f"✅ Resultado: {calc.tangente(angulo)}\n")
            
            elif opcion == "13":
                print("\n📊 PROMEDIO")
                n = int(input("¿Cuántos números?: "))
                nums = obtener_numeros(n)
                print(f"✅ Resultado: {calc.promedio(*nums)}\n")
            
            elif opcion == "14":
                print("\n📊 MEDIANA")
                n = int(input("¿Cuántos números?: "))
                nums = obtener_numeros(n)
                print(f"✅ Resultado: {calc.mediana(*nums)}\n")
            
            elif opcion == "15":
                print("\n📊 DESVIACIÓN ESTÁNDAR")
                n = int(input("¿Cuántos números?: "))
                nums = obtener_numeros(n)
                print(f"✅ Resultado: {calc.desviacion_estandar(*nums)}\n")
            
            elif opcion == "16":
                print("\nln LOGARITMO NATURAL")
                num = obtener_numeros(1)[0]
                print(f"✅ Resultado: {calc.logaritmo_natural(num)}\n")
            
            elif opcion == "17":
                print("\nlog LOGARITMO BASE 10")
                num = obtener_numeros(1)[0]
                print(f"✅ Resultado: {calc.logaritmo_base10(num)}\n")
            
            elif opcion == "18":
                print("\nlog LOGARITMO (CUALQUIER BASE)")
                num, base = obtener_numeros(2, "Valor")
                print(f"✅ Resultado: {calc.logaritmo(num, base)}\n")
            
            elif opcion == "19":
                print("\n|| VALOR ABSOLUTO")
                num = obtener_numeros(1)[0]
                print(f"✅ Resultado: {calc.valor_absoluto(num)}\n")
            
            elif opcion == "20":
                print("\n≈ REDONDEAR")
                num = obtener_numeros(1)[0]
                dec = int(input("¿Cuántos decimales?: "))
                print(f"✅ Resultado: {calc.redondear(num, dec)}\n")
            
            elif opcion == "21":
                print("\n% PORCENTAJE")
                parte, total = obtener_numeros(2, "Valor")
                print(f"✅ Resultado: {calc.convertir_a_porcentaje(parte, total)}%\n")
            
            elif opcion == "22":
                calc.ver_historial()
            
            elif opcion == "23":
                calc.limpiar_historial()
            
            else:
                print("❌ Opción no válida. Intenta de nuevo.\n")
        
        except ValueError as e:
            print(f"{e}\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")


if __name__ == "__main__":
    main()

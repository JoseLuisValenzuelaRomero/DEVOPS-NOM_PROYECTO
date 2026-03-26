class Calculator:
    def sum(self, a: int, b: int) -> int:
        return a + b

    def subtract(self, a: int, b: int) -> int:
        return a - b

    def multiply(self, a: int, b: int) -> int:
        return a * b

    def divide(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b

if __name__ == "__main__":
    calc = Calculator()
    print("Suma:", calc.sum(2, 3))
    print("Resta:", calc.subtract(5, 2))
    print("Multiplicación:", calc.multiply(4, 5))
    print("División:", calc.divide(10, 2))
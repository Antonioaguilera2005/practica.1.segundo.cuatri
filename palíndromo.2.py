class Palíndromo():
    def __init__(self, palabra):
        self.palabra = palabra

    def esPalindromo(self):
        palabra = self.palabra.replace(" ","").lower()
        return palabra == palabra[::-1]
    def resultado(self):
        if self.esPalindromo():
            return f"La palabra {self.palabra} es un palíndromo"
        else:
            return f"La palabra {self.palabra} no es un palíndromo"
    
    def test(self):
        return str(self.esPalindromo()) + "\n" + self.palabra.upper()

    def __str__(self):
        return self.resultado()

def main():
    palindromo = Palíndromo(input("Por favor, ingrese una palabra: "))
    print(f" >>> {palindromo.test()}")
    print(f" {palindromo.resultado()}")


main()    
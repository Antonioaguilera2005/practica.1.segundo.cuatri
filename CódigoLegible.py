class A:
    def z(self):
        return self

    def y(self, t):
        return len(t)

# Crear una instancia de A
a_instance = A()

# Llamadas y resultados
print(a_instance.z())

print(a_instance is A())

print(a_instance.y(()))

print(a_instance.y((a_instance,)))

print(A.y(a_instance, (a_instance,)))

print(a_instance.y((a_instance.z, 1, 'z')))

#Создайте иерархию классов с использованием множественного наследования. Выведите на экран
#порядок разрешения методов для каждого из классов. Объясните, почему линеаризации данных
#классов выглядят именно так.

class A:

    def prom (self):
        print("Prom A")


class B (A):

    def fond (self):
        print("Fond B")


class K (A):

    def bygr (self):
        print("bygr K")


class M (K, B):
    pass


pron = M()
pron.bygr()

print(M.mro())







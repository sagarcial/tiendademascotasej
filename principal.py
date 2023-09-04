from tienda import *

t=Tienda()
t.agregar_animales(Perro("boxer", 2,5))
t.agregar_animales(Perro("chiguagua", 2,1))
t.agregar_animales(Gato("angora", 2,0.5))
t.agregar_animales(Gato("persa", 2, 0.7))
t.agregar_animales(Gato("criollo", 12,3.5))
t.agregar_animales(Pez("golden", 0.5, 0.1))
t.agregar_animales(Pez("telescopio", 0.5, 0.1))
t.agregar_animales(Pez("coridora", 0.5, 0.01))
t.agregar_animales(Ave("loro", 1.0, 0.5))
t.agregar_animales(Ave("perico", 1.0, 0.5))
t.agregar_animales(Ave("cacatuas", 1.0, 0.5))

for i in range(5):
    a=t.entregar_animales()
    print(a.saludar(), a.mostrar_informacion())

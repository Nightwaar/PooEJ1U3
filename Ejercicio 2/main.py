import csv
from clasehelado import helados
from clasesabores import sabores
from manejahelados import manhe
from manejasabores import mansab


if __name__ == "__main__":
    hela=manhe()
    sabor=mansab()
    sabor.cargar()
    sabor.mostrar()
    print("""
          1.Agregar helado
          2.Mostrar
          3.Mostrar cantidad de gramos vendidos por sabor
          4.Mostrar sabores vendidos por tamaño de helado
          5.Dinero recaudado por tipo de helado
          6.Mostrar helados mas pedidos
          """)
    opc=int(input("Ingrese opcion"))
    while opc != 7:
        if opc==1:
            hela.carga()
        elif opc == 2:
            hela.mostrar()
        elif opc==5:
            print(hela.recaudado())
        elif opc == 6:
            hela.saboresvendidos()
        
        print("""
1.Agregar helado
2.Mostrar
3.Mostrar cantidad de gramos vendidos por sabor
4.Mostrar sabores vendidos por tamaño de helado
5.Dinero recaudado por tipo de helado
6.Mostrar helados mas pedidos
""")
        opc=int(input("Ingrese opcion"))
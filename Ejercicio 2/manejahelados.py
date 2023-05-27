from clasehelado import helados
class manhe:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def carga(self):
        sabor=[]
        print("""
100 gramos - $300 
150 gramos - $400
250 gramos - $600
500 gramos - $1000
1000 gramos - $2000""")
        peso = float(input("Ingrese el peso que quiere:"))
        if peso == 100:
            precio=300
        elif peso == 150:
            precio=400
        elif peso == 250:
            precio= 600
        elif peso ==500:
            precio=1000
        elif peso == 1000:
            precio= 2000
        n=int(input("Ingrese la cantidad de sabores:"))
        for i in range(n):
            ingrese= input("Ingrese el sabor {}".format(i+1))
            sabor.append(ingrese)
        self.__lista.append(helados(precio,peso,sabor))
        # for i in range(3):
        #     sabor = input("Ingrese el sabor, ingrese no si no desea agregar mas")
        #     if sabor == "no":
        #         return
        #     self.agregarsabor(sabor,1)
        print(self.__lista)
    def mostrar(self):
        for i in range(len(self.__lista)):
            print("Helado: N°{}".format(i+1))
            print(self.__lista[i])
    def recaudado(self):
        dinero= int("0")
        for i in self.__lista:
            dinero += i.mostrarprecio()
        return f"El total recaudado es: {dinero}"
    def saboresvendidos(self):
        sabores=[]
        for i in range(len(self.__lista)):
            
class helados:
    __peso= float('0')
    __precio = float('0')
    __sabor=list
    def __init__(self,precio,peso,sabor):
        self.__peso = peso
        self.__precio = precio
        self.__sabor=[]
        if sabor != None:
            self.agregarsabor(sabor,1)
    def __str__(self):
        return f"El precio es: {self.__precio} el peso es: {self.__peso} y los sabores son: {self.__sabor}"
    def agregarsabor(self,sabor,cantidad):
        for i in range(cantidad):
            self.__sabor.append(sabor)
    def mostrarpeso(self):
        return self.__peso
    def mostrarprecio(self):
        return self.__precio
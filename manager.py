# Archivo manager.py
from particula import Particula
import json


class Manager:

    def __init__(self):
        self.__particulas = []

    def agregarInicio(self, particula: Particula):
        self.__particulas.insert(0, particula)

    def agregarFinal(self, particula: Particula):
        self.__particulas.append(particula)

    def imprimir(self):
        for particula in self.__particulas:
            print(particula)

    def __str__(self):
        return "".join(
            str(particula) for particula in self.__particulas
        )

    def sortById(self):
        array = []

        for particula in self.__particulas:
            array.append(particula)

        array.sort(key=particula.__id, reverse=False)

        return "".join(
            str(particula) for particula in array
        )

    def sortBySpeed(self):
        array = []
        
        for particula in self.__particulas:
            array.append(particula)

        array.sort(key=particula.velocidad, reverse=False)

        return "".join(
            str(particula) for particula in array
        )
    
    def sortByDistance(self):
        array = []
        
        for particula in self.__particulas:
            array.append(particula)

        array.sort(key=particula.distancia, reverse=True)

        return "".join(
            str(particula) for particula in array
        )
        
    def __len__(self):
        return len(self.__particulas)
    
    def __iter__(self):
        self.cont = 0
        return self
    
    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, "w") as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, "r") as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except: 
            return 0
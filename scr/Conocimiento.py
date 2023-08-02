#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 23:24:57 2022

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: Sistemas Expertos
Alumnos: Rios Campusano Beckham Alejandro
         Garduño Sanchez Bladimir Axley
Profesor: M. en C. Edith Cristina Herrera Luna
Descripción: Conocimiento del sistema experto
    
@author: alebe
"""

from experta import *

class Turismo(KnowledgeEngine):
    destino = None
    lugres = None
    descripcion = None
    
    @Rule(AND(AND(Fact(frio="True"), Fact(naturaleza="True")), Fact(aventura="True")))
    def frioNaturalezaAventura(self):
        self.destino = "Estado de México."
        self.lugares = "Marquesa, Parque Nacional de Iztacihuatl, Valle de bravo, "
        self.lugares += "Parque dos aguas, Ixtapan de la sal."
        self.descripcion = "Estos lugares son caracterizados por las actividades a "
        self.descripcion += "realizar dentro de ellos como lo son: rapel, caminata, "
        self.descripcion += "senderismo, etc. Disfrutando de la naturaleza y un clima agradable."
        
    @Rule(AND(AND(Fact(frio="True"), Fact(naturaleza="True")), Fact(arqueologia="True")))
    def frioNaturalezaArqueologia(self):
        self.destino = "Estado de México."
        self.lugares = "Sin Lugares en el Estado de México."
        self.descripcion = "El Estado de México no cuenta con atracciones que cumplan con "
        self.descripcion += "estas condiciones."
    
    @Rule(AND(AND(Fact(frio="True"), Fact(naturaleza="True")), Fact(religioso="True")))
    def frioNaturalezaReligioso(self):
        self.destino = "Estado de México."
        self.lugares = "Sin Lugares en el Estado de México."
        self.descripcion = "El Estado de México no cuenta con atracciones que cumplan con "
        self.descripcion += "estas condiciones."
    
    @Rule(AND(AND(Fact(frio="True"), Fact(pueblo="True")), Fact(aventura="True")))
    def frioPuebloAventura(self):
        self.destino = "Estado de México."
        self.lugares = "Malinalco, Metepec, Valle de Bravo, Tlalmanalco."
        self.descripcion = "Definidos como pueblos mágicos del Estado de México con un clima "
        self.descripcion += "templado y regularmente lluvioso. Ricos en cultura por la conservación"
        self.descripcion += " a sus tradiciones y principios antiguos."
    
    @Rule(AND(AND(Fact(frio="True"), Fact(pueblo="True")), Fact(arqueologia="True")))
    def frioPuebloArqueologia(self):
        self.destino = "Estado de México."
        self.lugares = "Sin Lugares en el Estado de México."
        self.descripcion = "El Estado de México no cuenta con atracciones que cumplan con "
        self.descripcion += "estas condiciones."
    
    @Rule(AND(AND(Fact(frio="True"), Fact(pueblo="True")), Fact(religioso="True")))
    def frioPuebloReligioso(self):
        self.destino = "Estado de México."
        self.lugares = "Catedral de Toluca"
        self.descripcion = "Dentro del Estado de México se cuenta solo con este atractivo con estas "
        self.descripcion += "caracteristicas. Sin embargo encontraremos una gran variedad catolica."
        
    @Rule(AND(AND(Fact(calor="True"), Fact(naturaleza="True")), Fact(aventura="True")))
    def calorNaturalezaAventura(self):
        self.destino = "Estado de México."
        self.lugares = "Parque ecologico Xochitla, Ex-Hacienda Panoaya, Presa la cocha, Arcos del sitio."
        self.descripcion ="Estos lugares son destinos familiares, llenos de actividades "
        self.descripcion += "recreativas en donde podras disfrutar de la naturaleza bajo el sol."
        
    @Rule(AND(AND(Fact(calor="True"), Fact(naturaleza="True")), Fact(arquelogia="True")))
    def calorNaturalezaArqueologia(self):
        self.destino = "Estado de México."
        self.lugares = "San Juan Teotihuacan, Tenayuca, Malinalco."
        self.descripcion = "Lugares con distitos atractivos arqueologicos, gastronomicos, culturales "
        self.descripcion += "y tipicos de la región llenos de historia."
    
    @Rule(AND(AND(Fact(calor="True"), Fact(naturaleza="True")), Fact(religioso="True")))
    def calorNaturalezaReligioso(self):
        self.destino = "Estado de México."
        self.lugares = "Chalma, Cerro de la Virgen de Fátima."
        self.descripcion ="Estos destinos comparten la religión catolica, rodeado de "
        self.descripcion += "patrimonio natural y festividades."
        
    @Rule(AND(AND(Fact(calor="True"), Fact(pueblo="True")), Fact(aventura="True")))
    def calorPuebloAventura(self):
        self.destino = "Estado de México."
        self.lugares = "Tepotzotlan."
        self.descripcion = "Cuenta con Arcos del sitio que es un lugar en donde podras "
        self.descripcion += "hacer varias activiades y gozar de la gastronomia del lugar."
        
    @Rule(AND(AND(Fact(calor="True"), Fact(pueblo="True")), Fact(arqueologia="True")))
    def calorPuebloArqueologia(self): 
       self.destino = "Estado de México."
       self.lugares = "Sin Lugares en el Estado de México."
       self.descripcion = "El Estado de México no cuenta con atracciones que cumplan con "
       self.descripcion += "estas condiciones."
   
    @Rule(AND(AND(Fact(calor="True"), Fact(pueblo="True")), Fact(religioso="True")))
    def calorPuebloReligioso(self):
        self.destino = "Estado de México."
        self.lugares = "Catedral de Texcoco, la Iglesia de la Merced"
        self.descripcion ="Estos destinos comparten patrimonio religioso tangible"
        self.descripcion += " y festividades catolicas."
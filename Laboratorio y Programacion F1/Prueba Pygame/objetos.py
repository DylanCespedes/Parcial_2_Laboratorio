import pygame
import colores
import random

############################### OBJETOS #########################################

def crear_malo(x, y, ancho, alto):

    imagenes_comida_mala = ["CD.png", "zapato.png", "herradura.png", "avion.png"]
    imagen_comida_mala = pygame.image.load(random.choice(imagenes_comida_mala))
    imagen_comida_mala = pygame.transform.scale(imagen_comida_mala, (ancho, alto))
    rect_comida_mala = imagen_comida_mala.get_rect()
    rect_comida_mala.x = x
    rect_comida_mala.y = y
    dict_comida_mala = {}
    dict_comida_mala["surface"] = imagen_comida_mala
    dict_comida_mala["rect"] = rect_comida_mala
    dict_comida_mala["visible"] = True
    dict_comida_mala["speed"] = random.randrange(10, 20, 1)

    return dict_comida_mala

def update(lista_comida_mala):
    for objeto in lista_comida_mala:
        rect_comida_mala = objeto["rect"]
        rect_comida_mala.y = rect_comida_mala.y + objeto["speed"]

def actualizar_pantalla(lista_comida_mala, personaje, window):
    for objeto in lista_comida_mala:
        if(personaje["rect"].colliderect(objeto["rect"])):
            personaje["vida"] -= 1
            restar_objeto(objeto)
        
        if(objeto["rect"].x > 580):
            restar_objeto(objeto)
        window.blit(objeto["surface"], objeto["rect"])

    font = pygame.font.SysFont("Pou", 50)
    text = font.render("Vidas: {0}".format(personaje["vidas"]), True, (255, 0, 0))
    window.blit(text, (550,0))

def crear_lista_objetos(cantidad):
    lista_objetos = []
    for i in range(cantidad):
        y = random.randrange(-1000, 0, 60)
        x = random.randrange(0, 740, 60)
        objeto = crear_malo(x, y, 60, 60)
        lista_objetos.append(objeto)
    return lista_objetos

cantidad_imagen = 4
lista_objetos = crear_lista_objetos(cantidad_imagen)

def restar_objeto(objeto):
    y = random.randrange(-1000, 0, 60)
    x = random.randrange(0, 740, 60)
    objeto["rect"].x = random.randrange(0, 740, 60)
    objeto["rect"].y = random.randrange(-1000, 0, 60)

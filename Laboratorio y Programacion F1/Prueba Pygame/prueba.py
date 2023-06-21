import pygame
import comida
import objetos
import colores
import personaje

import random
import sys

ANCHO_PANTALLA = 772
ALTO_PANTALLA = 697

posicion_fondo = (0, 0)

pygame.init()

window = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("POU - FOOD DROP")

#Clase Titulo y boton para crear un menu principal y un menu de pausa

class Titulo:
    def __init__(self, x, y, texto):
        self.x = x
        self.y = y
        self.texto = texto

    def dibujar(self, pantalla):
        fuente = pygame.font.SysFont("Pou", 48)
        texto_render = fuente.render(self.texto, True, colores.BLANCO)
        texto_rect = texto_render.get_rect(center=(self.x, self.y))
        pantalla.blit(texto_render, texto_rect)

#Clase texto
class Boton:
    def __init__(self, x, y, ancho, alto, texto):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, colores.BLANCO, self.rect)
        fuente = pygame.font.SysFont("Pou", 35)
        texto_render = fuente.render(self.texto, True, colores.NEGRO)
        texto_rect = texto_render.get_rect(center=self.rect.center)
        pantalla.blit(texto_render, texto_rect)

    def verificar_click(self, pos):
        if self.rect.collidepoint(pos):
            return True
        return False

#Botones del menu
boton_jugar = Boton(270, 200, 200, 50, "Jugar")
boton_salir = Boton(270, 300, 200, 50, "Salir")
botones = [boton_jugar, boton_salir]

#Botones del menu de pausa

boton_volver_menu = Boton(250, 300, 270, 50, "Volver al menu")
botones_pausa = [boton_volver_menu]

#TIMER
timer = pygame.USEREVENT
pygame.time.set_timer(timer, 100)

#tamanio del personaje

player = personaje.crear(ANCHO_PANTALLA/2,ALTO_PANTALLA-100,100,100)

#tamanio de la lista al aparecer comida

lista_comida = comida.crear_lista_comida(15)

#tamanio de la lista al aparecer comida mala

lista_comida_mala = objetos.crear_lista_objetos(15)

#Fondo de nivel

nivel_1 = pygame.image.load("Food Drip Pou nivel 1.jpg")
nivel_1 = pygame.transform.scale(nivel_1,(772, 697))

nivel_actual = nivel_1
     
#Musica
musica_fondo = pygame.mixer.Sound('Musiquita Pou.mp3')

volumen = 0.1

musica_fondo.set_volume(volumen)

#Reloj de juego
clock = pygame.time.Clock()

bandera_correr = True

while bandera_correr:
    
    titulo = Titulo(ANCHO_PANTALLA // 2, 100, "Pou - FOOD DRIP")

    musica_fondo.stop()

    lista_evento = pygame.event.get()

    for evento in lista_evento:
        for evento in lista_evento:
            if evento.type == pygame.QUIT:
                bandera_correr = False   

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    pos = pygame.mouse.get_pos()
                    for boton in botones:
                        if boton.verificar_click(pos):
                            if boton == boton_jugar:
                                print("Comenzando...")
                                pygame.time.set_timer(timer, 100)
                                en_pausa = False

                                musica_fondo.play(-1)

                                while bandera_correr:
                                    lista_evento = pygame.event.get()

                                    for evento in lista_evento:
                                        if evento.type == pygame.QUIT:
                                            bandera_correr = False

                                        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                                            en_pausa = not en_pausa

                                            musica_fondo.stop()

                                            titulo = Titulo(ANCHO_PANTALLA // 2, 100, "Pausa")
                                            
                                            for evento in lista_evento:
                                                for evento in lista_evento:
                                                    if evento.type == pygame.QUIT:
                                                        bandera_correr = False

                                                    elif evento.type == pygame.MOUSEBUTTONDOWN:
                                                        if evento.button == 1:
                                                            for boton in botones_pausa:
                                                                if boton.verificar_click(pos):
                                                                    if boton == boton_volver_menu:
                                                                        print("Volviendo al menu")



                                            window.fill(colores.VERDE)
                                            titulo.dibujar(window)
                                            for boton in botones_pausa:
                                                boton.dibujar(window)
                                            pygame.display.flip()

                                    if not en_pausa:
                                        if evento.type == pygame.USEREVENT and evento.type == timer:
                                            if evento.type == timer:
                                                comida.update(lista_comida)

                                

                                        lista_teclas = pygame.key.get_pressed()
            
                                        if lista_teclas[pygame.K_LEFT]:
                                            personaje.update(player, -20)

                                        if lista_teclas[pygame.K_RIGHT]:
                                            personaje.update(player, 20)

                                        window.fill(colores.NEGRO)
                                        window.blit(nivel_1,(posicion_fondo))
                                        personaje.actualizar_pantalla(player, window)
                                        comida.actualizar_pantalla(lista_comida,player,window)
                                        objetos.actualizar_pantalla(lista_comida_mala, player, window)
                                        pygame.display.flip()
                                        clock.tick(30)

                            elif boton == boton_salir:
                                pygame.quit()
                                sys.exit()
    
    window.fill(colores.VERDE)
    titulo.dibujar(window)
    for boton in botones:
        boton.dibujar(window)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
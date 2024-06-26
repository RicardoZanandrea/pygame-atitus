import pygame
import random
import os
from tkinter import simpledialog
import game_funcions as gf
from ui_functions import start

pygame.init()
resources = {
    'relogio': pygame.time.Clock(),
    'icone': pygame.image.load("recursos/icone.png"),
    'lebron': pygame.image.load("recursos/lebron.png"),
    'fundo': pygame.image.load("recursos/fundo.png"),
    'fundoStart': pygame.image.load("recursos/fundoStart.png"),
    'fundoDead': pygame.image.load("recursos/fundoDead.png"),
    'missile': pygame.image.load("recursos/missile.png"),
    'trophy': pygame.image.load("recursos/trophy.png"),
    'missileSound': pygame.mixer.Sound("recursos/missile.wav"),
    'explosaoSound': pygame.mixer.Sound("recursos/explosao.wav"),
    'tela': pygame.display.set_mode((800, 600)),
    'branco': (255, 255, 255),
    'preto': (0, 0, 0),
    'fonte': pygame.font.SysFont(None, 55),
    'fonteStart': pygame.font.SysFont(None, 75),
    'fonteMorte' : pygame.font.SysFont("arialblack",100),
}

start(resources)
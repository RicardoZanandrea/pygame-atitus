import pygame
import random
import os
from tkinter import simpledialog
import funcoes

pygame.init()

relogio = pygame.time.Clock()
icone  = pygame.image.load("recursos/icone.png")
lebron = pygame.image.load("recursos/lebron.png")
fundo = pygame.image.load("recursos/fundo.png")
fundoStart = pygame.image.load("recursos/fundoStart.png")
fundoDead = pygame.image.load("recursos/fundoDead.png")
missile = pygame.image.load("recursos/missile.png")
trophy = pygame.image.load("recursos/trophy.png")

tamanho = (800,600)
tela = pygame.display.set_mode( tamanho ) 
pygame.display.set_caption("King James")
pygame.display.set_icon(icone)
missileSound = pygame.mixer.Sound("recursos/missile.wav")
explosaoSound = pygame.mixer.Sound("recursos/explosao.wav")
fonte = pygame.font.SysFont("arialblack",28)
fonteStart = pygame.font.SysFont("arialblack",55)
fonteMorte = pygame.font.SysFont("arialblack",100)
pygame.mixer.music.load("recursos/soundtrack.mp3")

branco = (255,255,255)
preto = (0, 0 ,0 )


def jogar(nome):
    pygame.mixer.Sound.play(missileSound)
    pygame.mixer.music.play(-1)
    posicaoXPersona = 250
    posicaoYPersona = 380
    movimentoXPersona  = 0
    posicaoXTrophy = 150
    posicaoYTrophy = -200
    velocidadeTrophy = 1
    posicaoXMissile = 400
    posicaoYMissile = -200
    velocidadeMissile = 1
    pontos = 0
    larguraPersona = 155
    alturaPersona = 219
    larguraTrophy  = 140
    alturaTrophy  = 155
    larguraMissel  = 50
    alturaMissel  = 250
    dificuldade  = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 10
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
                movimentoXPersona = -10
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 0
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
                movimentoXPersona = 0
                
        posicaoXPersona = posicaoXPersona + movimentoXPersona                   
        
        if posicaoXPersona < 0 :
            posicaoXPersona = 10
        elif posicaoXPersona > 500:
            posicaoXPersona = 490
            

        tela.fill(branco)
        tela.blit(fundo, (0,0) )
        #pygame.draw.circle(tela, preto, (posicaoXPersona,posicaoYPersona), 40, 0 )
        tela.blit( lebron, (posicaoXPersona, posicaoYPersona) )
        
        posicaoYTrophy = posicaoYTrophy + velocidadeTrophy
        if posicaoYTrophy > 600:
            posicaoYTrophy = -240
            pontos = pontos + 1
            velocidadeTrophy = velocidadeTrophy + 1
            posicaoXTrophy = random.randint(0,800)
            pygame.mixer.Sound.play(missileSound)
            
            
        tela.blit( trophy, (posicaoXTrophy, posicaoYTrophy) )
        
        texto = fonte.render(nome+"- Pontos: "+str(pontos), True, branco)
        tela.blit(texto, (10,10))
        
        pixelsPersonaX = list(range(posicaoXPersona, posicaoXPersona+larguraPersona))
        pixelsPersonaY = list(range(posicaoYPersona, posicaoYPersona+alturaPersona))
        pixelsTrophyX = list(range(posicaoXTrophy, posicaoXTrophy + larguraTrophy))
        pixelsTrophyY = list(range(posicaoYTrophy, posicaoYTrophy + alturaTrophy))
        
        #print( len( list( set(pixelsTrophyX).intersection(set(pixelsPersonaX))   ) )   )
        if  len( list( set(pixelsTrophyY).intersection(set(pixelsPersonaY))) ) > dificuldade:
            if len( list( set(pixelsTrophyX).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                dead(nome, pontos)
        
    
        
        pygame.display.update()
        relogio.tick(60)


def dead(nome, pontos):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)
    
    jogadas  = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8")
        jogadas = eval(arquivo.read())
        arquivo.close()
    except:
        arquivo = open("historico.txt","w",encoding="utf-8")
        arquivo.close()
 
    jogadas[nome] = pontos   
    arquivo = open("historico.txt","w",encoding="utf-8") 
    arquivo.write(str(jogadas))
    arquivo.close()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                jogar(nome)

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)
        tela.fill(branco)
        tela.blit(fundoDead, (0,0))
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        textoStart = fonteStart.render("RESTART", True, branco)
        tela.blit(textoStart, (400,482))
        textoEnter = fonte.render("Press enter to continue...", True, branco)
        tela.blit(textoEnter, (60,482))
        pygame.display.update()
        relogio.tick(60)


def ranking():
    estrelas = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8" )
        estrelas = eval(arquivo.read())
        arquivo.close()
    except:
        pass
    
    nomes = sorted(estrelas, key=estrelas.get,reverse=True)
    print(estrelas)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    start()

        tela.fill(preto)
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        textoStart = fonteStart.render("BACK TO START", True, branco)
        tela.blit(textoStart, (330,482))
        
        
        posicaoY = 50
        for key,nome in enumerate(nomes):
            if key == 13:
                break
            textoJogador = fonte.render(nome + " - "+str(estrelas[nome]), True, branco)
            tela.blit(textoJogador, (300,posicaoY))
            posicaoY = posicaoY + 30

            
        
        pygame.display.update()
        relogio.tick(60)


def start():
    nome = simpledialog.askstring("Iron Man","Nome Completo:")
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)
                elif buttonRanking.collidepoint(evento.pos):
                    ranking()

        tela.fill(branco)
        tela.blit(fundoStart, (0,0))
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        buttonRanking = pygame.draw.rect(tela, preto, (35,50,200,50),0,30)
        textoRanking = fonte.render("Ranking", True, branco)
        tela.blit(textoRanking, (90,50))
        textoStart = fonteStart.render("START", True, branco)
        tela.blit(textoStart, (330,482))

        
        
        pygame.display.update()
        relogio.tick(60)

start()
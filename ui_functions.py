import pygame
from tkinter import simpledialog
import game_funcions as gf

def ranking(resources):
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
                    start(resources)

        resources['tela'].fill(resources['preto'])
        buttonStart = pygame.draw.rect(resources['tela'], resources['preto'], (35,482,750,100),0)
        textoStart = resources['fonteStart'].render("BACK TO START", True, resources['branco'])
        resources['tela'].blit(textoStart, (330,482))
        
        
        posicaoY = 50
        for key,nome in enumerate(nomes):
            if key == 13:
                break
            textoJogador = resources['fonte'].render(nome + " - "+str(estrelas[nome]), True, resources['branco'])
            resources['tela'].blit(textoJogador, (300,posicaoY))
            posicaoY = posicaoY + 30

            
        
        pygame.display.update()
        resources['relogio'].tick(60)

def start(resources):
    nome = simpledialog.askstring("Iron Man","Nome Completo:")
    pygame.display.set_caption("King James")
    pygame.display.set_icon(resources['icone'])
    pygame.mixer.music.load("recursos/soundtrack.mp3")
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    gf.jogar(nome, resources)
                elif buttonRanking.collidepoint(evento.pos):
                    ranking(resources)

        resources['tela'].fill(resources['branco'])
        resources['tela'].blit(resources['fundoStart'], (0,0))
        buttonStart = pygame.draw.rect(resources['tela'], resources['preto'], (35,482,750,100),0)
        textoStart = resources['fonteStart'].render("START", True, resources['branco'])
        resources['tela'].blit(textoStart, (330,482))
        buttonRanking = pygame.draw.rect(resources['tela'], resources['preto'], (35,50,200,50),0,30)
        textoRanking = resources['fonte'].render("Ranking", True, resources['branco'])
        resources['tela'].blit(textoRanking, (90,50))

        pygame.display.update()
        resources['relogio'].tick(60)
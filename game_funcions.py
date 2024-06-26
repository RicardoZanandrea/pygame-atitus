import pygame
import random

def jogar(nome, resources):
    pygame.mixer.Sound.play(resources['missileSound'])
    pygame.mixer.music.play(-1)
    posicaoXPersona = 250
    posicaoYPersona = 380
    movimentoXPersona = 0
    posicaoXTrophy = 150
    posicaoYTrophy = -200
    velocidadeTrophy = 1
    posicaoXMissile = 400
    posicaoYMissile = -200
    velocidadeMissile = 1
    pontos = 0
    larguraPersona = 155
    alturaPersona = 219
    larguraTrophy = 140
    alturaTrophy = 155
    larguraMissel = 50
    alturaMissel = 250
    dificuldade = 0

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

        posicaoXPersona += movimentoXPersona

        if posicaoXPersona < 0:
            posicaoXPersona = 10
        elif posicaoXPersona > 500:
            posicaoXPersona = 490
            
        resources['tela'].fill(resources['branco'])
        resources['tela'].blit(resources['fundo'], (0, 0))
        resources['tela'].blit(resources['lebron'], (posicaoXPersona, posicaoYPersona))

        posicaoYTrophy += velocidadeTrophy
        if posicaoYTrophy > 600:
            posicaoYTrophy = -240
            pontos += 1
            velocidadeTrophy += 1
            posicaoXTrophy = random.randint(0, 800)
            pygame.mixer.Sound.play(resources['missileSound'])

        resources['tela'].blit(resources['trophy'], (posicaoXTrophy, posicaoYTrophy))

        texto = resources['fonte'].render(f"{nome}- Pontos: {str(pontos)}", True, resources['branco'])
        resources['tela'].blit(texto, (10, 10))

        pixelsPersonaX = list(range(posicaoXPersona, posicaoXPersona + larguraPersona))
        pixelsPersonaY = list(range(posicaoYPersona, posicaoYPersona + alturaPersona))
        pixelsTrophyX = list(range(posicaoXTrophy, posicaoXTrophy + larguraTrophy))
        pixelsTrophyY = list(range(posicaoYTrophy, posicaoYTrophy + alturaTrophy))

        if len(list(set(pixelsTrophyY).intersection(set(pixelsPersonaY)))) > dificuldade:
            if len(list(set(pixelsTrophyX).intersection(set(pixelsPersonaX)))) > dificuldade:
                dead(nome, pontos, resources)

        pygame.display.update()
        resources['relogio'].tick(60)


def dead(nome, pontos, resources):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(resources['explosaoSound'])

    jogadas = {}
    try:
        with open("historico.txt", "r", encoding="utf-8") as arquivo:
            jogadas = eval(arquivo.read())
    except FileNotFoundError:
        pass

    jogadas[nome] = pontos
    with open("historico.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(str(jogadas))

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                jogar(nome, resources)

        resources['tela'].fill(resources['branco'])
        resources['tela'].blit(resources['fundoDead'], (0, 0))
        buttonStart = pygame.draw.rect(resources['tela'], resources['preto'], (35, 482, 750, 100), 0)
        textoStart = resources['fonteStart'].render("RESTART", True, resources['branco'])
        resources['tela'].blit(textoStart, (535, 520))
        textoEnter = resources['fonte'].render("Press enter to continue...", True, resources['branco'])
        resources['tela'].blit(textoEnter, (60, 482))
        pygame.display.update()
        resources['relogio'].tick(60)
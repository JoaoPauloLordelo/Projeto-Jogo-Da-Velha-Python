import pygame as pg
from random import randint
from time import sleep
pergunta = 's'

while pergunta == 's':
    pg.init()
    tela = pg.display.set_mode((559, 800))
    pg.display.set_caption("Jogo da Velha")

    fonte = pg.font.Font(None, size = 30)
    cor = (255, 255, 255)

    imagemC = pg.image.load("img/C.png")
    imagemX = pg.image.load("img/X.png")

    areasClicadas = []
    areasMaquina = []
    def verificarVitoria(lista: list[pg.Rect], i):
        global vencedor 

        for c in lista:
            lContadores = [1,1]
            for j in lista:
                if c.left == j.left and c != j:
                    lContadores[0]+= 1
                if c.top == j.top and c != j:
                    lContadores[1]+= 1
            if 3 in lContadores:
                vencedor = i
                return True,vencedor
            elif (listaDeAreas[0] in lista and listaDeAreas[4] in lista and listaDeAreas[8] in lista) or (listaDeAreas[2] in lista and listaDeAreas[4] in lista and listaDeAreas[6] in lista):
                vencedor = i
                return True,vencedor
    
    def verificarColisao(colisao: pg.Rect):
        mpos = pg.mouse.get_pos()
        mColisao = colisao.collidepoint(mpos)
        if mColisao:
            mbp = pg.mouse.get_pressed()
            if mbp[0]:
                if colisao not in areasClicadas and colisao not in areasMaquina:
                    areasClicadas.append(colisao)
        else:
            return None
    
    listaDeAreas = [pg.Rect(50,50, 150,150),
                    pg.Rect(205,50, 150,150),
                    pg.Rect(360,50, 150,150),
                    pg.Rect(50,203, 150,150),
                    pg.Rect(205,203, 150,150),
                    pg.Rect(360,203, 150,150),
                    pg.Rect(50,356, 150,150),
                    pg.Rect(205,356, 150,150),
                    pg.Rect(360,356, 150,150)]

    rodando = True
    while rodando:
        tela.fill(cor)

        for j in listaDeAreas:
            verificarColisao(j)

        for zona in areasClicadas:
            tela.blit(imagemC, (zona.x, zona.y))

        pg.draw.lines(tela,(0,0,0),True,[(202,50),(202,505)],5)
        pg.draw.lines(tela,(0,0,0),True,[(357,50),(357,505)],5)
        pg.draw.lines(tela,(0,0,0),True,[(50,200),(509,200)],5)
        pg.draw.lines(tela,(0,0,0),True,[(50,355),(509,355)],5)

        if verificarVitoria(areasClicadas, "humano") or verificarVitoria(areasMaquina, "maquina"):
            text = fonte.render("A janela fechará automaticamente em 5 segundos",True,"Black")
            text2 = fonte.render(f"Vencedor: {vencedor}",True,"Black")
            tela.blit(text, (35,600))
            tela.blit(text2, (190,650))
            rodando = False

        if len(areasClicadas) + len(areasMaquina) == 9 and (not verificarVitoria(areasClicadas, "humano" and not verificarVitoria(areasMaquina, "maquina") )):
            text = fonte.render("A janela fechará automaticamente em 5 segundos",True,"Black")
            text2 = fonte.render(f"Empate",True,"Black")
            tela.blit(text, (35,600))
            tela.blit(text2, (230,650))
            rodando = False
        
        if rodando and len(areasMaquina) == len(areasClicadas) - 1: 
            if len(areasClicadas) + len(areasMaquina) < 9:
                n = randint(0,8)
                while listaDeAreas[n] in areasClicadas or listaDeAreas[n] in areasMaquina:
                    n = randint(0,8)
                areasMaquina.append(listaDeAreas[n])  
        
        for maq in areasMaquina:
            tela.blit(imagemX, (maq.x, maq.y))
        
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                rodando = False
        
        pg.display.flip()

    sleep(5)
    pg.quit()
    
    try:
        pergunta = input("Quer jogar novamente (s/n)").lower()
        while pergunta[0] not in "sn":
            print("Valor inválido")
            pergunta = input("Quer jogar novamente (s/n)").lower()
    except ValueError:
        print("Valor inválido")
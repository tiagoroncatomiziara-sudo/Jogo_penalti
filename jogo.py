
import pygame
import pgzrun
import random
from pgzero.actor import Actor
from PIL import Image
from pathlib import Path

WIDTH = 900
HEIGHT = 700

jogadores_canhotos = [
    "jogador_haaland",
    "jogador_lamine",
    "jogador_messi",
    "jogador_olise",
    "jogador_raphinha"
]

jogadores_destros = [
    "jogador_cristiano",
    "jogador_fenomeno",
    "jogador_kane",
    "jogador_kvara",
    "jogador_mbappe",
    "jogador_neymar",
    "jogador_rodrygo",
    "jogador_dembele",
    "jogador_ronaldinho",
    "jogador_vini",
    "jogador_belligham"
]


# Redimensionar imagens
def redimensionar(actor, tamanho):
    actor._surf = pygame.transform.scale(
        actor._surf, tamanho
    )

def posicionar_jogador():

    if player.image in jogadores_canhotos:
        player.pos = (740, 560)
    if player.image in jogadores_destros:
        player.pos = (250, 560)
    
# Criar atores
menu = Actor("menu_p1", (800, 500))
estadio = Actor("estadio_barcelona", (480, 350))
golkeeper = Actor("goleiro_joan", (560, 400))
player = Actor("jogador_cristiano", (250, 580))
bol = Actor("bola_trionda", (1050, 905))
erro = Actor("erro", (520, 140))
gol = Actor("gol", (980, 460))
        
# Aplicar os tamanhos
def redimensionar_imagens():
    redimensionar(golkeeper, (130, 170))
    redimensionar(player, (160, 230))
    redimensionar(bol, (75, 75))
    redimensionar(estadio, (700, 500))
    redimensionar(erro, (300, 200))
    redimensionar(gol, (300, 200))
    redimensionar(menu, (700, 500))
redimensionar_imagens()
player1_goleiro = ""
player2_goleiro = ""
player1 = ""
player2 = ""

alternadas = False

player1_chutou = False
player2_chutou = False

player1_escolheu = False
player2_escolheu = False

player1_goleiro_escolhido = False
player2_goleiro_escolhido = False


rodadas = 1

p1_gols = 0
p2_gols = 0

p1_cobrancas = 0
p2_cobrancas = 0

MAX_PENALTIS = 5

modo = "menu"
chute = ""
pulo = ""
nomes_jogador_1 = ""
nomes_jogador_2 = ""
def escolha_jogador(key):
    global player1, player2, player2_goleiro, player1_goleiro, nomes_jogador_1, nomes_jogador_2
    global player1_escolheu, player2_escolheu, player1_goleiro_escolhido, player2_goleiro_escolhido
    global goleiro_escolhido, modo, rodadas

    jogadores = {
        keys.K_0: "jogador_cristiano", 
        keys.K_8: "jogador_fenomeno",
        keys.K_1: "jogador_haaland",
        keys.K_9: "jogador_kane",
        keys.K_2: "jogador_kvara",
        keys.A: "jogador_lamine",
        keys.K_3: "jogador_mbappe",
        keys.B: "jogador_messi",
        keys.K_4: "jogador_neymar",
        keys.C: "jogador_olise",
        keys.K_5: "jogador_raphinha",
        keys.D: "jogador_vini",
        keys.K_6: "jogador_rodrygo",
        keys.K_7: "jogador_dembele",
        keys.E: "jogador_ronaldinho",
        keys.F: "jogador_belligham"
    }

    nomes_jogadores = {
        "jogador_cristiano": "Cristiano Ronaldo",
        "jogador_fenomeno": "Ronaldo Fenomeno",
        "jogador_haaland": "Haaland",
        "jogador_kane": "Harry Kane",
        "jogador_kvara": "Kvaratskhelia",
        "jogador_lamine": "Lamine Yamal",
        "jogador_mbappe": "Mbappe",
        "jogador_messi": "Lionel Messi",
        "jogador_neymar": "Neymar Jr",
        "jogador_olise": "Michael Olise",
        "jogador_raphinha": "Raphinha",
        "jogador_vini": "Vinicius Jr",
        "jogador_rodrygo": "Rodrygo",
        "jogador_dembele": "Ousmane Dembele",
        "jogador_ronaldinho": "Ronaldinho Gaucho",
        "jogador_belligham": "Jude Bellingham"
    }

    goleiros = {
        keys.K_1: "goleiro_joan",
        keys.K_2: "goleiro_neuer",
        keys.K_3: "goleiro_cortois",
        keys.K_4: "goleiro_alisson",
        keys.K_5: "goleiro_raya",
        keys.K_6: "goleiro_safonov",
        keys.K_7: "goleiro_donaruma"
    }

    estadios = {
        keys.K_1: "estadio_psg",
        keys.K_2: "estadio_barcelona",
        keys.K_3: "estadio_real",
        keys.K_4: "estadio_liverpool",
        keys.K_5: "estadio_arsenal",
        keys.K_6: "estadio_bayer",
        keys.K_7: "estadio_city"
    }

    # P1 escolhe
    if not player1_escolheu:
        if key not in jogadores:
            return

        player1 = jogadores[key]
        player1_escolheu = True
        menu.image = "menu_p2"

    # P2 escolhe
    elif not player2_escolheu:
        if key not in jogadores:
            return

        player2 = jogadores[key]
        player2_escolheu = True
        menu.image = "menu_gol_p1"

    # p1 escolhe goleiro
    elif not player1_goleiro_escolhido:
        if key not in goleiros:
            return

        player1_goleiro = goleiros[key]
        player1_goleiro_escolhido = True
        menu.image = "menu_gol_p2"
        
    # p2 escolhe goleiro
    elif not player2_goleiro_escolhido:
        if key not in goleiros:
            return

        player2_goleiro = goleiros[key]
        player2_goleiro_escolhido = True
        menu.image = "menu_estadio"
    elif player2_goleiro_escolhido:
        if key not in estadios:
            return
        estadio.image = estadios[key]
        modo = "jogo"
        rodadas = 1

        
        player.image = player1
        golkeeper.image = player2_goleiro

        
        bol.pos = (1050, 905)
        posicionar_jogador()
        golkeeper.pos = (560, 400)

        tocar_musica_torcida()
        nomes_jogador_1 = nomes_jogadores[player1]
        nomes_jogador_2 = nomes_jogadores[player2]
        
    redimensionar_imagens()
def tocar_musica_menu():
    music.play("som_menu")
    music.set_volume(0.6)
def tocar_musica_torcida():
    music.stop()
    music.play("som_torcida")
    music.set_volume(0.6)
def tocar_musica_resultado():
    music.stop()
    music.play("som_resultado")
    music.set_volume(0.6)
def resetar_jogo():
    global chute, pulo, rodadas

    chute = ""
    pulo = ""

    bol.pos = (1050, 905)
    golkeeper.pos = (560, 400)

    if rodadas == 1:
        rodadas = 2
        player.image = player2
        golkeeper.image = player1_goleiro
    else:
        rodadas = 1
        player.image = player1
        golkeeper.image = player2_goleiro
    redimensionar_imagens()
    posicionar_jogador()
def reiniciar_partida():
    global player1, player2
    global player1_goleiro, player2_goleiro
    global player1_escolheu, player2_escolheu
    global player1_goleiro_escolhido, player2_goleiro_escolhido
    global rodadas
    global p1_gols, p2_gols
    global p1_cobrancas, p2_cobrancas
    global chute, pulo, modo

    # Apagar jogadores e goleiros anteriores
    player1 = ""
    player2 = ""
    player1_goleiro = ""
    player2_goleiro = ""

    # Liberar todas as escolhas novamente
    player1_escolheu = False
    player2_escolheu = False
    player1_goleiro_escolhido = False
    player2_goleiro_escolhido = False

    # Zerar placar e cobranças
    p1_gols = 0
    p2_gols = 0
    p1_cobrancas = 0
    p2_cobrancas = 0

    # Reiniciar variáveis
    rodadas = 1
    chute = ""
    pulo = ""

    # Restaurar imagens
    menu.image = "menu_p1"
    player.image = "jogador_cristiano"
    golkeeper.image = "goleiro_joan"
    estadio.image = "estadio_barcelona"

    # Restaurar posições
    posicionar_jogador()
    golkeeper.pos = (560, 400)
    bol.pos = (1050, 905)

    # Voltar ao menu
    modo = "menu"

    redimensionar_imagens()
    tocar_musica_menu()
def pulo_direcao():
    global pulo
    pulo = random.choice(["esquerda", "centro", "direita"])
    if pulo == "esquerda":
        golkeeper.pos = (390, 400)
    elif pulo == "direita":
        golkeeper.pos = (680, 400)
    elif pulo == "centro":
        golkeeper.pos = (560, 400)
def verificar_gol():
    global chute, pulo
    if chute == "":
        return

    if chute == pulo:
        erro.draw()
        
    elif chute != pulo:
        gol.draw() 

def finalizar_cobranca():
    global p1_gols, p2_gols
    global p1_cobrancas, p2_cobrancas
    global modo, chute, alternadas

    if chute == "":
        return

    if rodadas == 1:
        if p1_cobrancas >= MAX_PENALTIS:
            return

        p1_cobrancas += 1

        if chute != pulo:
            p1_gols += 1

    else:
        if p2_cobrancas >= MAX_PENALTIS:
            return

        p2_cobrancas += 1

        if chute != pulo:
            p2_gols += 1

    # Encerrar somente depois de 5 cobranças de cada jogador
    if p1_cobrancas == MAX_PENALTIS and p2_cobrancas == MAX_PENALTIS:
        modo = "resultado"
        if p1_gols == p2_gols:
            p1_gols = 0 
            p1_cobrancas = 0
            p2_gols = 0
            p2_cobrancas = 0
            alternadas = True
        tocar_musica_resultado()
        return

    resetar_jogo()
def draw():
    global modo, p1_gols, p2_gols, p1_cobrancas, p2_cobrancas
    if modo == "menu":
        menu.draw()
    elif modo == "jogo":
        estadio.draw()
        golkeeper.draw()
        player.draw()
        bol.draw()
        verificar_gol()
        # Placar e cobranças
        screen.draw.text(
                f"{nomes_jogador_1}: {p1_gols} ({p1_cobrancas}/5)",
            center=(150, 35),
            fontsize=28,
            color="white",
            owidth=2,
            ocolor="black"
        )
        screen.draw.text("A:esquerda W:centro D:direita", center=(150, 55), fontsize=20, color="white", owidth=2, ocolor="black")
        screen.draw.text(
            f"{nomes_jogador_2}: {p2_gols} ({p2_cobrancas}/5)",
            center=(650, 35),
            fontsize=28,
            color="white",
            owidth=2,
            ocolor="black"
        )
        screen.draw.text("Setas:esquerda centro direita", center=(650, 55), fontsize=20, color="white", owidth=2, ocolor="black")
    
    elif modo == "resultado":
        estadio.draw()

        screen.draw.text(
            f"{nomes_jogador_1}: {p1_gols}  X  {p2_gols} :{nomes_jogador_2}",
            center=(370, 150),
            fontsize=45,
            color="yellow",
            owidth=2,
            ocolor="black"
        )

        if p1_gols > p2_gols:
            mensagem = nomes_jogador_1 + " VENCEU!"
            # Mensagem do resultado
            screen.draw.text(
                mensagem,
                center=(370, 180),
                fontsize=55,
                color="red",
                owidth=2,
                ocolor="black"
            )
            screen.draw.text(
            "PRESSIONE ENTER PARA JOGAR NOVAMENTE",
            center=(370, 230),
            fontsize=25,
            color="white",
            owidth=2,
            ocolor="black"
            )
        elif p2_gols > p1_gols:
            mensagem = nomes_jogador_2 + " VENCEU!"
            # Mensagem do resultado
            screen.draw.text(
                mensagem,
                center=(370, 180),
                fontsize=55,
                color="red",
                owidth=2,
                ocolor="black"
            )
            screen.draw.text(
            "PRESSIONE ENTER PARA JOGAR NOVAMENTE",
            center=(370, 230),
            fontsize=25,
            color="white",
            owidth=2,
            ocolor="black"
            )       

        elif alternadas == True:
            mensagem = "Disputa alternadas!"
            estadio.draw()
            player.draw()
            golkeeper.draw()
            bol.draw()


        

def on_key_down(key):
    global chute, modo

    if modo == "menu":
        escolha_jogador(key)
        return

    elif modo == "resultado":
        if key == keys.RETURN:
            reiniciar_partida()
        return

    elif modo == "jogo":

        if chute != "":
            return

        # PLAYER 1 - Q, W, E
        if rodadas == 1:

            if p1_cobrancas >= MAX_PENALTIS:
                return

            if key == keys.A:
                chute = "esquerda"

            elif key == keys.W:
                chute = "centro"

            elif key == keys.D:
                chute = "direita"

            else:
                return

        # PLAYER 2 - SETAS
        elif rodadas == 2:

            if p2_cobrancas >= MAX_PENALTIS:
                return

            if key == keys.LEFT:
                chute = "esquerda"

            elif key == keys.UP:
                chute = "centro"

            elif key == keys.RIGHT:
                chute = "direita"

            else:
                return

        # Executar o chute
        if chute != "":
            bol.pos = (1050, 735)
            if player.image in jogadores_canhotos:
                player.pos = (560, 500)

            elif player.image in jogadores_destros:
                player.pos = (420, 500)
            pulo_direcao()

            if chute == "esquerda":
                bol.pos = (840, 735)

            elif chute == "direita":
                bol.pos = (1200, 735)

            clock.schedule(finalizar_cobranca, 1.0)




tocar_musica_menu()
pgzrun.go()

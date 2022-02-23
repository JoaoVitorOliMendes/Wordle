import random
import colorama
import unidecode
import wasabi
from turtle import color
from colorama import Fore
from typing import List
from estado_letras import EstadoLetras
from wordle import Wordle


from wordle import Wordle
from wasabi import msg

def main():
    print("Bem vindo ao WordleBR!")

    lista_palavra_secreta = gerar_palavra_secreta("data/palavras_formatadas.txt")

    palavra_secreta = random.choice(list(lista_palavra_secreta))

    wordle = Wordle(palavra_secreta)

    while wordle.tentar_denovo:
        x = input("\nDigite seu palpite: ")

        if(len(x) > wordle.TAMANHO_PALAVRA):
            print(f"\nA palavra pode ter no máximo {wordle.TAMANHO_PALAVRA} letras.")
            continue
        if(len(x) < wordle.TAMANHO_PALAVRA):
            print(f"\nA palavra tem que ter no mínimo {wordle.TAMANHO_PALAVRA} letras.")
            continue
        if(x == "SAIR"):
            print("\nObrigado por jogar, jogue novamente mais tarde!")
            continue
        wordle.tentativas(x)
        a = wordle.tentar(x)
        if wordle.foi_descoberto:
            print(Fore.GREEN + f"\nPalavra Secreta: {wordle.palavraSecreta}")
            msg.good("\nVocê ganhou!")
            continue
        mostrar_resultados(wordle)

    if not wordle.foi_descoberto:
        msg.fail(f"Você perdeu, a palavra secreta era {wordle.palavraSecreta}")
        print("Obrigado por jogar, jogue novamente mais tarde!")

def mostrar_resultados(wordle: Wordle):
    print(f"\nVocê tem {wordle.tentativas_restantes} tentativas restantes")
    for palavra in wordle.tentativa:
        resultado = wordle.tentar(palavra)
        resultado = colorir_resultado(resultado)
        print(resultado)
    for _ in range(wordle.tentativas_restantes):
        print(" ".join(["_"] * wordle.TAMANHO_PALAVRA))

def colorir_resultado(resultado: List[EstadoLetras]):
    resultado_colorido = []
    for letra in resultado:
        if letra.posicao_correta:
            cor = Fore.GREEN
        elif letra.existe_na_palavra:
            cor = Fore.LIGHTYELLOW_EX
        else:
            cor = ""
        letra_colorida = cor + letra.letra + Fore.RESET
        resultado_colorido.append(letra_colorida)
    return " ".join(resultado_colorido)

def gerar_palavra_secreta(caminho: str):
    set_palavras = set()
    with open(caminho, "r", encoding='utf8') as arquivo:
        for linha in arquivo.readlines():
            palavra = unidecode.unidecode(linha.strip().upper())
            set_palavras.add(palavra)
    return set_palavras

if __name__ == "__main__":
    main()

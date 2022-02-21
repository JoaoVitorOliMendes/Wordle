from asyncio.windows_events import NULL
from unittest import result
from estado_letras import EstadoLetras

class Wordle:

    MAX_TENTATIVAS = 6
    TAMANHO_PALAVRA = 5

    def __init__(self, palavraSecreta: str):
        self.palavraSecreta: str = palavraSecreta.upper()
        self.tentativa = []
        pass

    @property
    def foi_descoberto(self):
        return len(self.tentativa) > 0 and self.tentativa[-1] == self.palavraSecreta

    @property
    def tentar_denovo(self):
        return self.tentativas_restantes > 0 and not self.foi_descoberto

    @property
    def tentativas_restantes(self) -> int :
        return self.MAX_TENTATIVAS - len(self.tentativa)

    def tentativas(self, palavra: str):
        palavra = palavra.upper()
        self.tentativa.append(palavra)

    def tentar(self, palavra: str):
        palavra_array = list(palavra.upper())
        secreta_temp = list(self.palavraSecreta.upper())
        resultado = [NULL] * 5

        for i in range(len(palavra_array)):
            letra = palavra_array[i]
            letraEstado = EstadoLetras(letra)
            if letra == secreta_temp[i]:
                letraEstado.posicao_correta = True
                secreta_temp[i] = ""
                resultado[i] = letraEstado
        
        for i in range(len(palavra_array)):
            letra = palavra_array[i]
            letraEstado = EstadoLetras(letra)
            if letra in secreta_temp:
                letraEstado.existe_na_palavra = True
                secreta_temp[secreta_temp.index(letra)] = ""
            if resultado[i] == 0:
                resultado[i] = letraEstado

        return resultado
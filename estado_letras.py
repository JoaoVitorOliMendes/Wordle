class EstadoLetras:
    def __init__(self, letra: str):
        self.letra: str = letra
        self.existe_na_palavra: bool = False
        self.posicao_correta: bool = False

    def __repr__(self):
        return f"[{self.letra} existe_na_palavra: {self.existe_na_palavra} posicao_correta: {self.posicao_correta}]"
import unidecode

def main():
    arquivo_input = "palavras.txt"
    arquivo_output = "palavras_formatadas.txt"
    palavras_com_5_letras = []
    with open(arquivo_input, "r") as input:
        for line in input.readlines():
            palavra = unidecode.unidecode(line.strip())
            if len(palavra) == 5:
                palavras_com_5_letras.append(palavra)
    with open(arquivo_output, "w") as output:
        for palavra in palavras_com_5_letras:
            output.write(palavra + '\n')
    print(f"Existem {len(palavras_com_5_letras)} palavras com 5 letras neste dicionario")

if __name__ == "__main__":
    main()

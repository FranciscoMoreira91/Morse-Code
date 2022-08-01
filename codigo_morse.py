alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
codigo_morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
       '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--', '....-',
       '.....', '-....', '--...', '---..', '----.', '-----']
def cifrar(txt):
    # transformar as letras
    morse = ""
    for l in txt:
        index = alpha.find(l)
        if index >= 0:
            morse += codigo_morse[index]
        else:
            morse += l+" "
    return morse.strip()
def decifrar(txt):
    texto = ""
    morse = txt.strip().split(" ")
    for l in morse:
        index = codigo_morse.index(l)
        if index >= 0:
            texto += alpha[index]
        else:
            texto += " "
    return texto
m_a = ""
while m_a != "M" and m_a != "A":
    m_a = input("Pretende introduzir em morse ou alfabeto? (M/A) ").upper()
    if m_a == "A":
        txt = input("Mensagem a codificar: ").upper()
        print()
        print('Morse: ', cifrar(txt))
    elif m_a == "M":
        txt = input("Mensagem a descodificar: ")
        print()
        print('Conversão para texto: ', decifrar(txt))

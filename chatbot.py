print("🤖 Chatbot Python iniciado!")
print("Digite 'sair' para encerrar.\n")

while True:
    mensagem = input("Você: ").lower()

    if mensagem == "sair":
        print("Chatbot: Até logo!")
        break

    elif "oi" in mensagem or "olá" in mensagem:
        print("Chatbot: Olá! Como posso te ajudar?")

    elif "python" in mensagem:
        print("Chatbot: Python é uma ótima linguagem para automação e IA!")

    elif "nome" in mensagem:
        print("Chatbot: Eu sou um chatbot simples em Python.")

    else:
        print("Chatbot: Desculpa, ainda estou aprendendo.")

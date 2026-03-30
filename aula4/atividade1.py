'''
Crie um script que solicite o usuário e a senha do estudante. Enquanto o estudante não digitar  usuário e a senha corretamente, 
o programa deve continuar solicitando as credenciais. Quando o usuário digitá-las corretamente, o programa deve imprimir a mensagem 
de "Bem-vindo" e terminar. O usuário e a senha deve ser fixo (padrão).
usuário = admin
senha = admin123

diferente: !=

'''

while True:
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    if usuario == "admin" and senha == "admin123":
        print("Bem-vindo ao sistema!")
        break
    else:
        print("Usuário ou senha inválidos!")

        
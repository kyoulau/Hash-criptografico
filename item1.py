##Otavio Murilo
##Laura dos Santos

import getpass
import hashlib

def hash_senha(senha): 
    return hashlib.sha256(senha.encode()).hexdigest()

def verificar_cadastro(nome, usuarios):
    with open(usuarios, "r") as arquivo:
        for linha in arquivo:
            if nome in linha:
                return True
    return False  



while True:  ##Menu inicial
    print("===========")
    print("1. Entrar com um perfil existente")
    print("2. Criar um novo perfil")
    print("3. Sair")
    print("===========")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Informe seu nome: ")
        senha = getpass.getpass("Informe sua senha: ")

        with open("usuarios.txt", "r") as arquivo:
            usuarios = arquivo.readlines()
            registro = False
            for linha in usuarios:
                dados = linha.strip().split(",")
                if nome == dados[0] and hash_senha(senha) == dados[1]:
                    registro = True
                    print("Autenticação bem-sucedida.")
                    break

            if not registro:
                print("Usuário ou senha inválidos. Por favor, tente novamente.")
                continue  # Retorna ao inicio

    elif opcao == "2":
        nome = input("Informe seu nome: ")
        senha = getpass.getpass("Informe sua senha: ")
        
        if len(nome)  > 4 or len(senha) >  4:
            print("Nome e senha devem ter 4 caracteres.")
            continue
        senha_hash = hash_senha(senha)

        if verificar_cadastro(nome, "usuarios.txt"):
            print("Nome de usuário já cadastrado")                
        else:   
            with open("usuarios.txt", "a") as arquivo:    
                arquivo.write(f"{nome},{senha_hash}\n")
            print("Usuário registrado com sucesso")      
    elif opcao == "3":
        print("Programa encerrado")
        break

    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

##Otavio Murilo
##Laura dos Santos

import getpass
import hashlib
import os
import time
from termcolor import colored

def crack_senha():
    try:
        with open("usuarios.txt", "r") as f:
            for line in f:
                username, password_hash = line.strip().split(",")
                start_time = time.time() 
                with open("wordlist.txt", "r") as wordlist:
                    for password in wordlist:
                        password = password.strip()
                        guess_hash = hashlib.sha256(password.encode()).hexdigest()
                        if guess_hash == password_hash:
                            end_time = time.time()  
                            print(f"[+] Senha do usuario '{username}' e: {password}")
                            print(f"[*] Tempo para quebrar: {end_time - start_time:.2f} seconds")
                            break
                    else:
                        print("[-] Falha em tentar adivinhar senha para usuario '{}'".format(username))

    except Exception as exc:
        print('There was a problem: %s' % (exc))



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
    print("3. Quebrar senhas")
    print("4. Sair")
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
        print("Tentando adivinhar as senhas..")
        crack_senha()
    elif opcao == "4":
        print("Programa encerrado")
        break

    else:
        print("Opção inválida. Por favor, escolha 1, 2, 3 ou 4.")

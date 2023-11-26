#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:17:37 2023

@author: caroline
"""

import hashlib

class PasswordManager:
    def __init__(self, user_password_file, stored_password_file):
        self.user_password_file = user_password_file
        self.stored_password_file = stored_password_file

    def read_password_from_file(self, file_path="/Exercicio3/senha_guardada.txt"):
        with open(file_path, 'r') as file:
            return file.read().strip()

    def hash_password(self, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def check_password(self, user_password):
        stored_password = self.read_password_from_file(self.stored_password_file)
        hashed_stored_password = self.hash_password(stored_password)
        hashed_user_password = self.hash_password(user_password)
        return hashed_user_password == hashed_stored_password

if __name__ == "__main__":
    password_manager = PasswordManager("senha_digitada.txt", "senha_guardada.txt")

    # Ler a senha diretamente do arquivo
    with open(password_manager.user_password_file, 'r') as file:
        senha_digitada = file.read().strip()

    # Branch 1: Apresentar ao usuário a senha presente no arquivo de texto
    if password_manager.check_password(senha_digitada):
        print("Senha correta!")
    else:
        print("Senha incorreta")
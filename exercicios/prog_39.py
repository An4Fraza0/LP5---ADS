#  Crie um algoritmo que peça ao usuário para digitar uma senha e verifique se a senha é "1234".

senha = input("digite uma senha: ")
print("acesso permitido" if senha == "1234" else "acesso negado, senha incorreta.")
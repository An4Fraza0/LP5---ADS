# Crie uma nova versão do algoritmo 66, aplicando o conceito de módulos e dividindo as responsabilidades, receberemos agora não somente o nome, mas simularemos um sistema de cadastro de alunos, esta nova versão deve atender as novas funcionalidade a seguir:
# Cada aluno cadastrado deve ter atrelado a seus dados pessoais (nome, e-mail, data de nascimento, matricula), no caso de matricula você deve gerar uma matricula unica para cada aluno cadastrado.
# Cada um dos dados do aluno devem ser validade de forma o código não quebre ao serem informados valores incorretos.
# Para atualizar qualquer dado do aluno você deve localiza-lo utilizando de sua matricula para isso. Valide de forma que o sistema não quebre ao ser inserido uma matricula invalida.
# Para remover um aluno deve-se realizar esta ação usando de sua matricula, o sistema não pode quebrar ao ser inserido uma matricula errada.
# Ao listar todos os alunos mostre cada um de forma organizada e separada.
# Crie uma funcionalidade de mostre os dados de um aluno especifico usando apenas de sua matricula para isso.

import re
from datetime import datetime

# Módulo de validação e manipulação de alunos
def validar_nome(nome):
    """Valida o nome do aluno: não vazio e apenas letras e espaços."""
    if not nome or not nome.strip():
        return False, "nome não pode ser vazio."
    if not re.match(r'^[A-Za-zÀ-ÿ\s]+$', nome):
        return False, "o nome deve conter apenas letras e espaços."
    return True, nome.strip()

def validar_email(email):
    """Valida o e-mail: formato básico com '@' e domínio."""
    if not email or not email.strip():
        return False, "e-mail não pode ser vazio."
    # Validação simples
    if re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
        return True, email.strip().lower()
    return False, "e-mail inválido. use formato usuario@dominio.com"

def validar_data_nascimento(data_str):
    """Valida data de nascimento: formato DD/MM/AAAA, não futura, idade plausível (entre 0 e 120 anos)."""
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
    except ValueError:
        return False, "data inválida. use formato DD/MM/AAAA."

    hoje = datetime.now()
    idade = hoje.year - data.year - ((hoje.month, hoje.day) < (data.month, data.day))

    if data > hoje:
        return False, "data de nascimento não pode ser futura."
    if idade < 0 or idade > 120:
        return False, "idade inválida. deve estar entre 0 e 120 anos."
    return True, data_str

def gerar_matricula(contador):
    """Gera matrícula única no formato 'A0001' (A + número com 4 dígitos)."""
    return f"A{contador:04d}"

# Módulo de gerenciamento dos alunos
def cadastrar_aluno(alunos, proximo_id):
    """Solicita os dados do aluno, valida e cadastra."""
    print("\n--- cadastro de aluno ---")
    while True:
        nome = input("nome: ")
        valido, nome = validar_nome(nome)
        if valido:
            break
        print(f"erro: {nome}")

    while True:
        email = input("e-mail: ")
        valido, email = validar_email(email)
        if valido:
            break
        print(f"erro: {email}")

    while True:
        data_nasc = input("data de nascimento (DD/MM/AAAA): ")
        valido, data_nasc = validar_data_nascimento(data_nasc)
        if valido:
            break
        print(f"erro: {data_nasc}")

    matricula = gerar_matricula(proximo_id)
    alunos[matricula] = {
        "nome": nome,
        "email": email,
        "data_nascimento": data_nasc,
        "matricula": matricula
    }
    print(f"\naluno cadastrado com sucesso! matrícula: {matricula}")
    return proximo_id + 1

def listar_alunos(alunos):
    """Exibe todos os alunos cadastrados de forma organizada."""
    if not alunos:
        print("\nenhum aluno cadastrado.")
        return
    print("\n--- lista de alunos ---")
    for mat, dados in alunos.items():
        print(f"matrícula: {dados['matricula']}")
        print(f"nome: {dados['nome']}")
        print(f"e-mail: {dados['email']}")
        print(f"data de nascimento.: {dados['data_nascimento']}")
        print("-" * 30)

def buscar_aluno_por_matricula(alunos, matricula):
    """Retorna o dicionário do aluno ou None se não encontrado."""
    return alunos.get(matricula)

def exibir_aluno(aluno):
    """Exibe os dados de um único aluno."""
    print(f"\nmatrícula: {aluno['matricula']}")
    print(f"nome: {aluno['nome']}")
    print(f"e-mail: {aluno['email']}")
    print(f"data de nascimento: {aluno['data_nascimento']}")

def atualizar_aluno(alunos):
    """Localiza aluno por matrícula e permite atualizar seus dados."""
    if not alunos:
        print("\nnenhum aluno cadastrado.")
        return
    matricula = input("\ndigite a matrícula do aluno a ser atualizado: ").strip()
    aluno = buscar_aluno_por_matricula(alunos, matricula)
    if not aluno:
        print("matrícula não encontrada.")
        return

    print("\n--- atualizar dados ---")
    print("deixe em branco para manter o valor atual.")
    # Nome
    novo_nome = input(f"nome [{aluno['nome']}]: ").strip()
    if novo_nome:
        valido, nome = validar_nome(novo_nome)
        if valido:
            aluno['nome'] = nome
        else:
            print(f"erro: {nome}. campo mantido.")
    # E-mail
    novo_email = input(f"e-mail [{aluno['email']}]: ").strip()
    if novo_email:
        valido, email = validar_email(novo_email)
        if valido:
            aluno['email'] = email
        else:
            print(f"erro: {email}. campo mantido.")
    # Data de nascimento
    nova_data = input(f"data de nascimento [{aluno['data_nascimento']}]: ").strip()
    if nova_data:
        valido, data = validar_data_nascimento(nova_data)
        if valido:
            aluno['data_nascimento'] = data
        else:
            print(f"erro: {data}. campo mantido.")

    print("\ndados atualizados com sucesso!")

def remover_aluno(alunos):
    """Remove um aluno pela matrícula."""
    if not alunos:
        print("\nnenhum aluno cadastrado.")
        return
    matricula = input("\ndigite a matrícula do aluno a ser removido: ").strip()
    if matricula in alunos:
        confirm = input(f"tem certeza que deseja remover o aluno {alunos[matricula]['nome']}? (s/N): ").strip().lower()
        if confirm == 's':
            del alunos[matricula]
            print("aluno removido com sucesso.")
        else:
            print("operação cancelada.")
    else:
        print("matrícula não encontrada.")

def aluno_especifico(alunos):
    """Exibe os dados de um aluno específico pela matrícula."""
    if not alunos:
        print("\nnenhum aluno cadastrado.")
        return
    matricula = input("\ndigite a matrícula do aluno: ").strip()
    aluno = buscar_aluno_por_matricula(alunos, matricula)
    if aluno:
        exibir_aluno(aluno)
    else:
        print("matrícula não encontrada.")

# Módulo principal com menu interativo
def main():
    alunos = {}
    proximo_id = 1
    while True:
        print("\n" + "="*40)
        print("sistema de cadastro de alunos")
        print("="*40)
        print("1 - cadastrar aluno")
        print("2 - listar todos os alunos")
        print("3 - atualizar aluno")
        print("4 - remover aluno")
        print("5 - exibir aluno específico")
        print("0 - sair")
        opcao = input("\nescolha uma opção: ").strip()

        if opcao == "1":
            proximo_id = cadastrar_aluno(alunos, proximo_id)
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            atualizar_aluno(alunos)
        elif opcao == "4":
            remover_aluno(alunos)
        elif opcao == "5":
            aluno_especifico(alunos)
        elif opcao == "0":
            print("\nencerrando sistema...")
            break
        else:
            print("\nopção inválida... tente novamente.")

if __name__ == "__main__":
    main()
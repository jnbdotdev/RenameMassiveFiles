import os
import re
from os import listdir, rename
from pathlib import Path
from tkinter import filedialog as fd


def get_file_name():
    file = fd.askopenfilename()
    return file
def get_files():
    files = fd.askopenfiles()
    file_array = []
    for file in files:
        print("File: ", file.name)
        file_array.append(str(file.name))

    return file_array
def get_all_files():
    dir = fd.askdirectory()
    files = listdir(dir)
    file_array = []
    for file in files:
        print(f'File: {str(dir)}/{str(file)}')
        file_array.append(f'{str(dir)}/{str(file)}')

    return file_array

def filter_file_name(file_path):
    file_name = ""+Path(file_path).stem+Path(file_path).suffix

    return file_name
def increment_name(file_to_increment, increment=1, position="last", suffix=""):
    """
    Renomeia um arquivo incrementando um número no nome, mantendo zeros à esquerda.

    Parâmetros:
    - file: Caminho do arquivo original.
    - increment: Valor a ser somado aos números encontrados (padrão: 1).
    - position: Define qual número alterar ("last", "first", "middle", "all").

    Retorna:
    - Novo caminho do arquivo.
    """

    print("\nNome do arquivo:", filter_file_name(file_to_increment))

    file_path = Path(file_to_increment)
    file_parent_folder = file_path.parent
    file_name = file_path.stem
    file_suffix = file_path.suffix

    # Encontrar todos os números no nome do arquivo
    matches = list(re.finditer(r'\d+', file_name))

    if not matches:
        # Se não houver número, adicionar "01" ao final
        new_file_name = file_name + '01'
        print("\nNão havia números no nome. Adicionado '01'.")
    else:
        # Escolher qual(is) número(s) alterar
        if position == "first":
            indexes = [0]
        elif position == "last":
            indexes = [-1]
        elif position == "middle" and len(matches) > 1:
            indexes = [len(matches) // 2]  # Pega o índice do meio
        elif position == "all":
            indexes = list(range(len(matches)))  # Altera todos os números
        else:
            indexes = [-1]  # Default: último número

        # Criar novo nome do arquivo com os números alterados
        new_file_name = file_name
        for i in indexes:
            match = matches[i]
            number = match.group()  # Número original (ex: "002")
            new_number = str(int(number) + increment).zfill(len(number))  # Mantém zeros à esquerda

            # Substituir o número no nome do arquivo
            new_file_name = new_file_name[:match.start()] + new_number + suffix + new_file_name[match.end():]

        print(f"\nNúmero(s) alterado(s): {str(new_file_name)}")

    new_file = file_parent_folder / f"{new_file_name}{file_suffix}"

    rename(file_to_increment, new_file)

    return str(filter_file_name(new_file))
def replace_chars(files_to_replace, replace_method = "universal"):
    new_files = []
    os.system('cls')
    if replace_method == "universal":
        char_x = input("Caractere a ser trocado: ")
        char_y = input("Caractere para trocar: ")

        for file in files_to_replace:
            print("\nArquivo: ", filter_file_name(file))
            file_path = Path(file)

            file_parent_folder = file_path.parent
            file_name = file_path.stem
            file_suffix = file_path.suffix

            new_file_name = file_name.replace(char_x, char_y)

            new_file = file_parent_folder / f"{new_file_name}{file_suffix}"

            rename(file, new_file)
            new_files.append(filter_file_name(new_file))
            print('Arquivo renomeado: ', filter_file_name(new_file))

    elif replace_method == "selective":
        os.system('cls')
        for file in files_to_replace:
            print("\nArquivo: ", filter_file_name(file))
            file_path = Path(file)

            file_parent_folder = file_path.parent
            file_name = file_path.stem
            file_suffix = file_path.suffix

            char_x = input("Caractere a ser trocado: ")
            char_y = input("Caractere para trocar: ")

            new_file_name = file_name.replace(char_x, char_y)

            new_file = file_parent_folder / f"{new_file_name}{file_suffix}"

            rename(file, new_file)
            new_files.append(filter_file_name(new_file))
            print('Arquivo renomeado: ', filter_file_name(new_file))
    else:
        print('Método inválido selecionado.')

    return str(new_files)
def increment_files (files_to_increment):

    new_files = []

    print('\n<=====< Informe os parâmetros >=====>\n')
    increment_value = int(input('Valor a incrementar: '))
    print('\n-----------------------------------')
    print('\nPosição do número:\n\n[1] - Início\n[2] - Meio\n[3] - Fim\n')
    position_option = int(input('Informe a posição: '))
    print('\n-----------------------------------')
    print('\nDigite um sufixo caso queira utilizar algum. Se não, não insira nenhum valor.\n')
    sufix_option = input('Sufixo: ')
    print('\n<================<>================>')

    os.system('cls')

    position_value = "last"

    match position_option:
        case 1:
            position_value = "first"
        case 2:
            position_value = "middle"
        case 3:
            position_value = "last"


    for file in files_to_increment:
        new_file = increment_name(file, int(increment_value), str(position_value), str(sufix_option))
        new_files.append(str(new_file))

    return str(new_files)
def remove_final_spaces(files):

    for file in files:
        print("\nArquivo: ", filter_file_name(file))
        file_path = Path(file)

        file_parent_folder = file_path.parent
        file_name = file_path.stem
        file_suffix = file_path.suffix
        # Remove o espaço no final, se houver
        new_file_name = file_name.rstrip()

        new_file = file_parent_folder / f"{new_file_name}{file_suffix}"
        print('Arquivo atualizado: ', filter_file_name(new_file))
        rename(file, new_file)

def menu_operation_log():
    print("\n\n<======< MENU >======>\n\nSelecione a operação que você deseja realizar:\n\n[1] - Incrementar valor\n[2] - Substituir caracteres\n[3] - Remover espaço fantasma\n\n<=========<x>=========>\n")
def menu_target_log():
    print("\n\n<======< MENU >======>\n\nSelecione quais arquivos que você deseja alterar:\n\n[1] - Selecionar manualmente\n[2] - Todos os arquivos\n\n<=========<x>=========>\n")
def console_log():
    os.system('cls')
    print('--project: RENAME MASSIVE <')
    menu_operation_log()
    operation = int(input('Digite uma das opções: '))
    os.system('cls')
    menu_target_log()
    target = int(input('Digite uma das opções: '))
    os.system('cls')

    target_files = Path.home()

    if target == 1:
        target_files = get_files()
    elif target == 2:
        target_files = get_all_files()
    else:
        print('Opção de arquivo inválida.')

    if operation == 1:
        increment_files(target_files)
    elif operation == 2:
        print('\n<=====< Informe os parâmetros >=====>\n')
        print('\nMétodos de substituição:\n\n[1] - Universal\n[2] - Seletivo\n')
        method_option = int(input('Informe a opção: '))
        print('\n<================<>================>')
        method_value = "universal"

        match method_option:
            case 1:
                method_value = "universal"
            case 2:
                method_value = "selective"

        replace_chars(target_files, method_value)
    elif operation == 3:
        remove_final_spaces(target_files)
    else:
        print('Opção de operação inválida.')

    print('\nOperação finalizada.')

console_log()
import os

def create_folders():
    """ Cria diretórios necessários para o projeto """
    folders = ["../data", "../logs", "../outputs"]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"📂 Criado diretório: {folder}")

if __name__ == "__main__":
    create_folders()

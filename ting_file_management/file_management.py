import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            raise ValueError("Formato inválido")

        with open(path_file, "r") as file:
            return file.read().splitlines()

    except (FileNotFoundError, ValueError) as e:
        print(
            f"Arquivo {path_file} não encontrado"
            if isinstance(e, FileNotFoundError)
            else str(e),
            file=sys.stderr,
        )
        return None

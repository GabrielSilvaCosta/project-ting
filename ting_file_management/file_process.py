import sys
from ting_file_management.file_management import txt_importer


def is_already_processed(queue_instance, file_path):
    return any(
        isinstance(item, dict) and item.get("nome_do_arquivo") == file_path
        for item in getattr(queue_instance, "items", [])
    )


def process(path_file, queue_instance):
    try:
        if is_already_processed(queue_instance, path_file):
            print(f"Arquivo {path_file} já foi processado. Ignorando.")
            return

        file_content = txt_importer(path_file)
        metadata = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file_content),
            "linhas_do_arquivo": file_content,
        }
        queue_instance.enqueue(metadata)
        print(metadata)

    except Exception as e:
        print(f"Erro ao processar {path_file}: {str(e)}")


def remove(queue_instance):
    try:
        removed = queue_instance.dequeue()
        print(f"Arquivo {removed.get('nome_do_arquivo')} removido com sucesso")

    except IndexError:
        print("Não há elementos")

    except Exception as e:
        print(f"Erro ao remover arquivo: {str(e)}")


def file_metadata(queue_instance, position):
    try:
        file_info = queue_instance.search(position)
        print(
            {
                "nome_do_arquivo": file_info.get("nome_do_arquivo"),
                "qtd_linhas": file_info.get("qtd_linhas"),
                "linhas_do_arquivo": file_info.get("linhas_do_arquivo"),
            }
        ) if isinstance(file_info, dict) else print(
            "Posição inválida", file=sys.stderr
        )

    except IndexError:
        print("Posição inválida", file=sys.stderr)

    except Exception as e:
        print(f"Erro ao obter metadados do arquivo: {str(e)}", file=sys.stderr)

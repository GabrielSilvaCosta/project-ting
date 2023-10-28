from ting_file_management.file_management import txt_importer


def is_already_processed(queue_instance, file_path):
    if hasattr(queue_instance, "items") and isinstance(
        queue_instance.items, list
    ):
        for item in queue_instance.items:
            if (
                isinstance(item, dict)
                and item.get("nome_do_arquivo") == file_path
            ):
                return True
    return False


def process(path_file, queue_instance):
    try:
        if is_already_processed(queue_instance, path_file):
            print(f"Arquivo {path_file} já foi processado. Ignorando.")
            return

        file_content = txt_importer(path_file)
        queue_instance.enqueue(file_content)

        file_metadata = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file_content),
            "linhas_do_arquivo": file_content,
        }
        print(file_metadata)

    except Exception as e:
        print(f"Erro ao processar {path_file}: {str(e)}")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""

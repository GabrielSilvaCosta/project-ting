def exists_word(word, instance):
    return [
        {
            "palavra": word,
            "arquivo": file_info["nome_do_arquivo"],
            "ocorrencias": [
                {"linha": line_number}
                for line_number, line_content in enumerate(
                    file_info["linhas_do_arquivo"], 1
                )
                if word.lower() in line_content.lower()
            ],
        }
        for file_info in instance.items
        if any(
            word.lower() in line.lower()
            for line in file_info["linhas_do_arquivo"]
        )
    ]


def search_by_word(word, instance):
    return [
        {
            "palavra": word,
            "arquivo": file_info["nome_do_arquivo"],
            "ocorrencias": [
                {
                    "linha": line_number,
                    "conteudo": line_content.strip(),
                }
                for line_number, line_content in enumerate(
                    file_info["linhas_do_arquivo"], 1
                )
                if word.lower() in line_content.lower()
            ],
        }
        for file_info in instance.items
        if any(
            word.lower() in line.lower()
            for line in file_info["linhas_do_arquivo"]
        )
    ]

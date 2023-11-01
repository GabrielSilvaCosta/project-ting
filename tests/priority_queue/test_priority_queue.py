from ting_file_management.priority_queue import PriorityQueue
import pytest


def create_mock_data(qtd_linhas):
    return [
        {
            "nome_do_arquivo": f"arquivo{index+1}.txt",
            "qtd_linhas": qtd,
            "linhas_do_arquivo": [f"linha{i+1}" for i in range(qtd)],
        }
        for index, qtd in enumerate(qtd_linhas)
    ]


def test_basic_priority_queueing():
    mock_qtd_linhas = [9, 4, 2, 5, 7, 11, 3]
    mock_data = create_mock_data(mock_qtd_linhas)

    priority_queue = PriorityQueue()

    [priority_queue.enqueue(data) for data in mock_data]

    assert len(priority_queue) == len(mock_data)
    assert priority_queue.search(6) == mock_data[5]

    [priority_queue.dequeue() for _ in range(len(mock_data))]

    assert len(priority_queue) == 0
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(6)
        priority_queue.search(7)

"""Testes da ordenação pública de chamados por prioridade."""

from chamados import ordenar_chamados


def test_ordenar_chamados_por_prioridade_alta_media_baixa() -> None:
    chamados = [
        {
            "id": 1,
            "nome": "Chamado baixa",
            "prioridade": "baixa",
            "status": "status-original-1",
        },
        {
            "id": 2,
            "nome": "Chamado alta",
            "prioridade": "alta",
            "status": "status-original-2",
        },
        {
            "id": 3,
            "nome": "Chamado média",
            "prioridade": "média",
            "status": "status-original-3",
        },
    ]

    assert ordenar_chamados(chamados) == [chamados[1], chamados[2], chamados[0]]


def test_ordenar_chamados_rejeita_prioridade_desconhecida() -> None:
    chamados = [
        {
            "id": 11,
            "nome": "Chamado inválido",
            "prioridade": "urgente",
            "status": "status-original-11",
        }
    ]

    try:
        ordenar_chamados(chamados)
    except ValueError as exc:
        assert str(exc) == "Prioridade inválida para o chamado com id 11."
    else:
        raise AssertionError("Esperava ValueError para prioridade desconhecida.")


def test_ordenar_chamados_rejeita_varias_prioridades_desconhecidas() -> None:
    chamados = [
        {
            "id": 21,
            "nome": "Chamado inválido 1",
            "prioridade": "urgente",
            "status": "status-original-21",
        },
        {
            "id": 22,
            "nome": "Chamado inválido 2",
            "prioridade": "crítico",
            "status": "status-original-22",
        },
    ]

    try:
        ordenar_chamados(chamados)
    except ValueError as exc:
        assert str(exc) == "Prioridades inválidas para os chamados com ids 21, 22."
    else:
        raise AssertionError("Esperava ValueError para múltiplas prioridades desconhecidas.")


def test_ordenar_chamados_lista_vazia_retorna_lista_vazia() -> None:
    assert ordenar_chamados([]) == []


def test_ordenar_chamados_preserva_ordem_entre_prioridades_iguais() -> None:
    chamados = [
        {
            "id": 31,
            "nome": "Primeiro média",
            "prioridade": "média",
            "status": "status-original-31",
        },
        {
            "id": 32,
            "nome": "Segundo média",
            "prioridade": "média",
            "status": "status-original-32",
        },
        {
            "id": 33,
            "nome": "Terceiro alta",
            "prioridade": "alta",
            "status": "status-original-33",
        },
    ]

    assert ordenar_chamados(chamados) == [chamados[2], chamados[0], chamados[1]]

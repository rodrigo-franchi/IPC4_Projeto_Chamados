"""Operações públicas para gestão de chamados."""


def ordenar_chamados(chamados: list[dict[str, object]]) -> list[dict[str, object]]:
	"""Retorna chamados ordenados por prioridade: alta, média e baixa."""
	ordem_prioridade = {"alta": 0, "média": 1, "baixa": 2}
	ids_invalidos: list[int] = []

	for chamado in chamados:
		prioridade = chamado.get("prioridade")
		if prioridade not in ordem_prioridade:
			ids_invalidos.append(int(chamado["id"]))

	if ids_invalidos:
		if len(ids_invalidos) == 1:
			raise ValueError(f"Prioridade inválida para o chamado com id {ids_invalidos[0]}.")
		ids_formatados = ", ".join(str(id_invalido) for id_invalido in ids_invalidos)
		raise ValueError(f"Prioridades inválidas para os chamados com ids {ids_formatados}.")

	return sorted(chamados, key=lambda chamado: ordem_prioridade[chamado["prioridade"]])

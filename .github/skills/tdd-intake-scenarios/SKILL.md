---
name: tdd-intake-scenarios
description: "Levante variações comportamentais relevantes para uma lista inicial de cenários TDD. Use para identificar casos básicos, limites, falhas e preservação de comportamento existente, sem concretizar todos em testes."
argument-hint: "Informe o comportamento desejado; opcionalmente, inclua regras e casos já conhecidos."
user-invocable: true
---

# Coletar lista inicial de cenários

## Entrada aceita

Comportamento desejado e, se disponíveis, regras confirmadas, exemplos ou casos já conhecidos. Uma descrição parcial é suficiente para iniciar uma lista preliminar.

## Procedimento

1. Liste brevemente cenários comportamentais: caso básico, variações importantes, limites, falhas esperadas e comportamento existente que não deve regredir quando relevante.
2. Diferencie casos confirmados de perguntas abertas. Priorize a utilidade da lista, não exaustividade.
3. Não converta cada item em um teste executável; somente o cenário escolhido na skill `tdd-intake-next-test` será concretizado primeiro.
4. Quando faltarem regras para determinar o resultado esperado de um cenário, registre a lacuna em vez de propor uma resposta.

## Restrições

- Não misture cenários com decisões de implementação.
- Não invente códigos de erro, limites, tipos aceitos ou comportamento de recuperação.
- Não escreva código ou testes.

## Saída obrigatória

Retorne somente este bloco, mantendo os rótulos e valores de status:

```yaml
status: FECHADO # Valores permitidos: FECHADO, PENDENTE
`FECHADO` significa que há pelo menos um cenário útil e as incertezas estão identificadas; a lista não precisa estar completa. Use `PENDENTE` apenas se nem um cenário útil puder ser descrito.
item: lista_de_cenarios
dado: "1. cenário — confirmado/pergunta; 2. cenário — confirmado/pergunta"
evidencia: "usuário | caminho e referência no repositório | nenhuma"
pendencia: "nenhuma | pergunta objetiva sobre a regra que impede definir um resultado esperado"
```

Na saída real, escreva `dado:` sem espaço inicial antes do rótulo. `FECHADO` significa que há pelo menos um cenário útil e as incertezas estão identificadas; a lista não precisa estar completa. Use `PENDENTE` apenas se nem um cenário útil puder ser descrito.

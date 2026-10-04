---
name: tdd-intake-next-test
description: "Escolha um único cenário para o próximo ciclo TDD a partir de uma lista inicial. Use para priorizar o menor teste de comportamento que forneça feedback útil, sem gerar a suíte inteira."
argument-hint: "Forneça comportamento desejado e cenários conhecidos."
user-invocable: true
---

# Selecionar o próximo teste

## Entrada aceita

Comportamento desejado e uma lista inicial de cenários. Se não houver lista, derive até três opções curtas do comportamento declarado, sem inventar regras.

## Procedimento

1. Escolha exatamente um cenário pequeno, significativo e com resultado observável.
2. Prefira o caso mais simples que exercite o comportamento central e permita feedback rápido; não otimize cobertura total nesta decisão.
3. Mantenha os demais cenários como próximos itens, sem transformá-los em testes.
4. Se nenhum resultado esperado puder ser determinado sem decisão de negócio, deixe o item pendente e formule uma pergunta.

## Restrições

- Não escreva o teste nem a implementação.
- Não selecione vários cenários como “primeiro teste”.
- Não use cobertura percentual como critério para escolher este primeiro ciclo.

## Saída obrigatória

Retorne somente este bloco, mantendo os rótulos e valores de status:

```yaml
status: FECHADO # Valores permitidos: FECHADO, PENDENTE
Se `FECHADO`, `dado` começa com o único próximo cenário e pode terminar com `demais: ...`. Se não houver critério para selecionar sem adivinhar, use `PENDENTE`.
item: proximo_cenario
dado: "Um único cenário inicial; demais cenários ficam identificados separadamente."
evidencia: "usuário | caminho e referência no repositório | cenário derivado do comportamento confirmado"
pendencia: "nenhuma | uma pergunta objetiva que bloqueia escolher o resultado esperado"
```

Na saída real, escreva `dado:` sem espaço inicial antes do rótulo. Se `FECHADO`, `dado` começa com o único próximo cenário e pode terminar com `demais: ...`. Se não houver critério para selecionar sem adivinhar, use `PENDENTE`.

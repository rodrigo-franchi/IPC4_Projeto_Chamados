---
name: tdd-intake-behavior
description: "Capture o comportamento desejado para preparar uma tarefa de TDD. Use para transformar uma necessidade em uma descrição observável, sem propor implementação nem inventar regras."
argument-hint: "Descreva a mudança de comportamento que deseja."
user-invocable: true
---

# Coletar comportamento desejado

## Entrada aceita

Uma descrição livre, requisito, história de usuário ou exemplo do comportamento pretendido. Aceite informação parcial. Não exija assinatura, solução técnica ou todos os casos de teste.

## Procedimento

1. Identifique quem/qual interface usa o comportamento, quando aplicável, e o resultado observável desejado.
2. Preserve os termos e regras informados; não deduza comportamento não declarado.
3. Se o comportamento ainda não puder ser distinguido do estado atual, faça uma pergunta objetiva. Não peça detalhes de implementação.

## Restrições

- Não escolha arquitetura, algoritmo, estrutura de dados ou assinatura de função.
- Não crie testes nem código.
- Registre cada regra não confirmada como pendência, sem transformá-la em expectativa.

## Saída obrigatória

Retorne somente este bloco, mantendo os rótulos e valores de status:

```yaml
status: FECHADO # Valores permitidos: FECHADO, PENDENTE
item: comportamento_desejado
dado: "Uma frase que descreve o resultado observável, ou 'não informado'."
evidencia: "usuário | caminho e referência no repositório | nenhuma"
pendencia: "nenhuma | uma pergunta objetiva necessária para fechar o item"
```

Use `FECHADO` quando o resultado observável estiver claro. Use `PENDENTE` se faltar informação essencial; nesse caso, faça somente a pergunta contida em `pendencia`.

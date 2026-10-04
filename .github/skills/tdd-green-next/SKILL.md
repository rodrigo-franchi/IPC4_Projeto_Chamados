---
name: tdd-green-next
description: "Continue um ciclo TDD Python após o teste unitário RED: leia a ficha salva em docs/ e o teste correspondente, confirme que a falha é funcional e implemente somente o código de produção mínimo para esse teste passar. Pare em GREEN, sem refatorar nem alterar testes."
argument-hint: "Indique o projeto, o caminho da ficha TDD ou o teste RED."
user-invocable: false
disable-model-invocation: false
---

# Implementar o próximo passo GREEN

## Objetivo

Dar continuidade a um ciclo TDD iniciado por um teste RED: confirmar que o teste direcionado falha por comportamento de produção ainda ausente, escrever o mínimo de código de produção para fazê-lo passar e parar em GREEN. Refatorar é um passo separado e não pertence a este workflow.

## Entrada necessária

Localize e leia no projeto-alvo:

1. A ficha de intake datada em `docs/YYYY-MM-DD-tdd-intake.md`.
2. O teste unitário RED criado para o próximo cenário dessa ficha.

Use caminho informado explicitamente quando disponível. Senão, use o projeto indicado no pedido/contexto e encontre a ficha e o teste correspondentes. Não peça para colarem novamente conteúdos acessíveis no workspace. Se o projeto ou os arquivos pertinentes não forem identificáveis, se houver múltiplas fichas/testes candidatos, ou se a ficha não estiver pronta, pergunte pelo caminho/decisão e não edite.

## Procedimento

1. Leia a ficha, o teste e somente os arquivos/configurações do projeto estritamente necessários para entender como executar o teste e onde a API pública se integra.
2. Execute apenas o teste RED direcionado antes da implementação quando possível. Examine a falha integralmente.
3. Prossiga somente se o teste coletar corretamente e falhar por falta da implementação/comportamento de produção. Erros de sintaxe, import path incorreto do teste, dependências ausentes, configuração ou ambiente não provam RED funcional: pare, relate a causa e não altere produção para contornar o problema.
4. Determine a menor alteração de produção que satisfaz o comportamento exercitado pelo teste, consistente com os requisitos confirmados na ficha. O teste atual é o limite executável; não implemente cenários futuros descritos na lista da ficha antes de testes próprios.
5. Faça a mudança mínima e legível nos arquivos de produção necessários. Se ainda não houver pacote, módulo ou export e o teste já definir uma fronteira pública concreta, crie somente a estrutura mínima necessária para esse import/API. Não crie configuração do projeto ou dependências.
6. Não altere o arquivo de teste: não reescreva, remova, enfraqueça, pule ou acrescente asserts para forçar o verde. Não adicione testes neste passo.
7. Execute somente o mesmo teste direcionado após a mudança.
8. Se passar, pare imediatamente: GREEN alcançado. Não faça refatoração, mesmo que veja oportunidades. Se falhar por causa diferente, diagnostique e faça no máximo a correção de produção mínima que continua diretamente necessária para o mesmo comportamento; pare se a falha revelar ambiguidade, escopo novo ou problema de ambiente. Não avance para outro teste.

## Princípios TDD

- Respeite o ciclo curto Red-Green-Refactor: um teste falhando, a menor produção que o satisfaz, e refatoração depois, com os testes verdes.
- “Mínimo” significa a menor solução de produção que atende o comportamento público exercitado, não código deliberadamente ruim, arquitetura artificial ou hacks de uma linha.
- Preserve o contrato documentado e não invente resultados, validações, exceções, mensagens, prioridades, estruturas ou comportamentos não cobertos pelo teste/ficha.
- Não confunda erro de coleta/importação ou indisponibilidade de pytest com falha funcional RED.

## Limites absolutos

- Altere somente código de produção essencial para passar o teste RED corrente.
- Nunca edite testes, documentos, configuração, dependências, lockfiles ou pipelines.
- Nunca crie testes adicionais, implemente cenários não testados, faça refatoração, otimização, cobertura, lint ou rode a suíte completa.
- Não esconda falhas nem acrescente fallbacks que contrariem o contrato.

## Entrega

Se bloqueado antes da edição, informe a causa observada e que nenhum arquivo foi alterado.

Se alcançou GREEN, informe os arquivos de produção alterados, o teste direcionado executado e o resultado. Se não foi possível executar a verificação, declare isso claramente; não afirme que o passo está verde sem evidência do teste passando.

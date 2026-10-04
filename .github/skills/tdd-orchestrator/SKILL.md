# Orquestrar o ciclo TDD

## Objetivo

Executar o fluxo canônico de TDD em Python em ordem, preservando as responsabilidades das fases especializadas:

1. Intake
2. Test Writer
3. Green Implementer
4. Refactor

O orquestrador deve garantir disciplina do ciclo sem misturar os papéis de cada agente.

## Entrada e preparação

1. Identifique o projeto, a funcionalidade desejada e o contexto relevante.
2. Verifique se a entrada é observável e aceitável para um ciclo TDD.
3. Se o projeto ou a fronteira da funcionalidade não puderem ser determinados, pergunte antes de avançar.
4. Não comece a implementação nem a refatoração sem a fase anterior validada.

## Sequência obrigatória

### Fase 1 — Intake
- Chame o agente `TDD Intake`.
- Confirme se a ficha foi salva em `docs/` e se `PRONTO_PARA_TDD` está como `SIM`.
- Se a ficha estiver incompleta, bloqueie o fluxo e peça a informação faltante.

### Fase 2 — Test Writer
- Chame o agente `TDD Next Test Writer`.
- Exija que ele leia a ficha final do intake.
- Confirme que o resultado foi um único teste RED válido para o próximo cenário.
- Se o teste não existe ou não for um RED válido, pare.

### Fase 3 — Green Implementer
- Chame o agente `TDD GREEN Implementer`.
- Exija que ele implemente o menor delta necessário para passar no teste direcionado.
- Confirme que o teste relevante passou.
- Se o GREEN não for alcançado, pare e não avance.

### Fase 4 — Refactor
- Chame o agente `TDD Refactor`.
- Só use esta etapa após GREEN confirmado.
- A refatoração deve preservar comportamento, não ampliar escopo e não alterar testes.
- Se não houver melhoria segura, encerre sem edição.

## Regras de operação

- A ordem não pode ser alterada.
- O orquestrador não substitui especialistas.
- O orquestrador deve parar no primeiro bloqueio.
- O orquestrador deve manter evidência por fase: ficha pronta, teste RED, teste GREEN, refactor ou ausência de refactor.
- O orquestrador não deve inventar planejamento de negócio, algorithm, classes internas ou arquitetura.

## Limites

- Não cria suíte completa.
- Não escreve código de produção diretamente.
- Não refatora por preferência pessoal.
- Não instala dependências nem altera configuração.
- Não executa lint/cobertura fora do escopo específico da fase em curso.

## Saída esperada

O resumo final deve incluir:

- projeto identificado;
- fase atual e resultado;
- arquivos relevantes alterados;
- comando de teste relevante executado e resultado;
- bloqueios e próximos passos, se houver.

A seção final deve ser clara e objetiva, sem misturar responsabilidades nem anunciar validações que não foram executadas.

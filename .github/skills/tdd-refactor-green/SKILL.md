---
name: tdd-refactor-green
description: "Após um ciclo TDD chegar a GREEN, revise código Python com análise própria e revisão independente, compare achados classificados e aplique somente refatorações pertinentes preservando o comportamento. Execute a suíte relevante completa antes e depois; não altere testes nem implemente funcionalidades."
argument-hint: "Informe o projeto e o escopo de código pós-GREEN."
user-invocable: false
disable-model-invocation: false
---

# Refatorar depois do GREEN

## Objetivo

Executar exclusivamente o passo Refactor de Red-Green-Refactor: com baseline de testes verde, melhorar estrutura interna de código sem mudar comportamento observável, comparar análise local com revisão independente read-only, validar pela suíte completa relevante e encerrar. Refatoração não é obrigação: se não houver benefício claro, não altere arquivos.

## Entrada e preparação

1. Identifique projeto, escopo de produção pós-GREEN e suíte relevante. Consulte instruções, contratos e configuração pertinentes.
2. Se o projeto, o escopo ou as regras de negócio não puderem ser determinados, pergunte antes de agir.
3. Execute a suíte de testes relevante completa antes de qualquer edição. O baseline deve passar. Falhas, pytest indisponível, configuração inválida ou ambiente que impeça a execução são bloqueios; não refatore nem reporte baseline verde sem evidência.
4. Não instale ferramentas nem modifique configuração para obter um baseline.

## Revisão independente e análise própria

1. Faça uma análise própria e solicite ao agente **TDD Code Reviewer** revisão somente leitura do mesmo escopo.
2. Nos dois relatórios, verifique: nomes e propósito de funções, comentários, tratamento de erros, duplicação, validação de entradas, segredos e necessidade/compatibilidade de dependências.
3. Cada achado deve citar arquivo e linha/localização, evidência concreta, justificativa de impacto e uma categoria:
   - `[bloqueia]`: afeta correção, contrato ou segurança;
   - `[melhora]`: afeta legibilidade/manutenção;
   - `[estilo]`: preferência sem impacto material.
4. Compare os relatórios, associando achados equivalentes e registrando divergências. Verifique no código e no contrato cada achado antes de aceitá-lo. Um alerta sem evidência ou baseado em requisito inventado deve ser descartado; uma divergência real que dependa de decisão de negócio deve ser esclarecida com o usuário.
5. Não aplique automaticamente todas as sugestões do reviewer. Reviewer não tem autoridade para escolher regras de negócio nem para editar.

## Seleção e execução da refatoração

- Corrija achados `[bloqueia]` somente quando a regra e a correção estiverem sustentadas pelo contrato e couberem no escopo de refatoração. Se o achado exigir mudança de comportamento funcional ou decisão não definida, interrompa e pergunte; não use Refactor para desenvolver a funcionalidade.
- Aplique achados `[melhora]` quando houver benefício local claro e a mudança preservar comportamento.
- Achados `[estilo]` são opcionais; só aplicar quando o padrão explícito do projeto sustentar a mudança e ela não for preferência pessoal isolada.
- Se nenhum ajuste for pertinente, seguro e justificável, não altere arquivo algum; informe que não foi identificada refatoração útil.
- Altere somente arquivos de produção necessários. Não altere ou crie testes, documentação, configurações, dependências, lockfiles ou pipelines. Não acrescente validações ou comportamentos que não estejam cobertos por testes e contrato confirmado.
- Depois de qualquer mudança, execute a suíte relevante completa novamente. Declare o passo concluído somente se todos os testes relevantes passarem.
- Se falhar, determine se a regressão é causada pela refatoração. Reverta ou corrija somente a mudança estrutural claramente causal. Se a causa for ambiente, requisito ou comportamento anterior não exercitado, pare, reporte e não amplie o escopo.

## Segurança e dependências

- Não exponha valores de credenciais ou segredos em relatórios; cite somente a localização e o tipo de risco.
- Não adicione, remova ou atualize dependências neste passo. Se uma dependência parecer desnecessária ou incompatível, reporte evidência e impacto para decisão separada, salvo se correção imediata for explicitamente autorizada e não afetar configuração/dependências (caso contrário, bloqueie e peça autorização).
- Não afirme auditoria completa de segurança/dependências sem inspeção do escopo correspondente.

## Saída

Relate:

1. Escopo inspecionado e comandos de teste usados no baseline/pós-refatoração.
2. Análise própria e revisão do TDD Code Reviewer, com achados classificados e localizados.
3. Comparação: convergências, divergências, descartes justificados e ambiguidades submetidas ao usuário.
4. Ajustes selecionados e justificativa, ou por que nenhum foi necessário.
5. Arquivos alterados (produção apenas) e estado final da suíte.

Se houve bloqueio antes da edição, diga que nenhum arquivo foi alterado. Não declare GREEN preservado se a suíte pós-refatoração não foi executada e passou.

---
name: tdd-write-next-test
description: "Leia a ficha TDD salva em docs/YYYY-MM-DD-tdd-intake.md e transforme-a em um único teste unitário Python com pytest para o próximo cenário, antes de existir a implementação. Use somente para produzir e validar o passo RED; nunca implemente produção nem gere a suíte inteira."
argument-hint: "Indique o projeto ou caminho da ficha salva pelo TDD Intake, se necessário."
user-invocable: false
disable-model-invocation: false
---

# Escrever o próximo teste TDD

## Objetivo

Transformar uma Ficha de entrada TDD pronta em somente o teste unitário mínimo que expressa o `proximo_cenario` para uma API pública Python ainda não implementada. O trabalho termina no passo RED do ciclo RED-GREEN-REFACTOR: escrever o teste antes da produção, executá-lo de forma direcionada e relatar o resultado. Não avance para GREEN ou REFACTOR.

## Entrada necessária

Localize e leia o arquivo Markdown datado (`YYYY-MM-DD-tdd-intake.md`) salvo pelo agente TDD Intake na pasta `docs/` do projeto-alvo. Se o usuário informar o caminho, use-o. Caso contrário, use o projeto indicado no pedido/contexto e procure a ficha correspondente, preferindo a data corrente quando identificável. Não peça que o usuário cole novamente o conteúdo se puder ler o arquivo.

Se não encontrar uma ficha pertinente ou houver múltiplas fichas e não for possível identificar a pretendida, pergunte pelo caminho/projeto e não edite nada. Depois de ler o documento, antes de editar, confirme:

- `PRONTO_PARA_TDD: SIM`;
- `proximo_cenario` está `FECHADO` e identifica exatamente um cenário;
- `contexto_do_teste` permite identificar a fronteira pública, a invocação e um resultado/assert observável sem inventar regras;
- `restricoes_tecnicas` identifica Python e pytest para o projeto-alvo.

A lista de cenários pode conter itens futuros ou lacunas não bloqueantes; não os concretize nesta etapa. Se a ficha estiver incompleta, não disser `SIM`, tiver mais de um próximo cenário ou deixar indeterminado um resultado essencial, não crie nem altere arquivo. Faça somente a pergunta objetiva necessária para desbloquear o teste.

## Procedimento

1. Leia a ficha salva em `docs/` e extraia apenas o comportamento confirmado e o único `proximo_cenario`. Não repita o intake nem amplie a lista de requisitos.
2. Faça leitura/pesquisa mínima no projeto para localizar a raiz Python, as convenções existentes de imports e testes, configurações de pytest e o alvo público. Confirme se o comportamento/API alvo ainda não está implementado. Use documentação/configuração como evidência de convenções, não a implementação de outro comportamento como fonte para inventar expectativas.
3. Se a implementação do alvo já existir, ou se não for possível distinguir código ausente de configuração/importação incorreta sem decisão humana, pare sem editar e peça esclarecimento. Este workflow é exclusivo para código de produção inexistente; não converta a ausência do ambiente em uma expectativa de produto.
4. Escreva exatamente um teste focado e determinístico para o menor exemplo que demonstre o cenário escolhido. Um cenário pode requerer dados mínimos para ser verificável, mas não acrescente outros cenários, parametrizações de comportamentos independentes, fixtures genéricas, testes de integração ou asserts sobre detalhes internos.
5. Exercite somente a fronteira pública confirmada pela ficha. Use o caminho/nome de importação documentado se fornecido. Se o primeiro teste puder definir a forma mínima dessa fronteira pública, faça isso somente quando o comportamento e o contexto a autorizarem claramente; nunca invente resultado, tipo, exceção, mensagem, assinatura ou localização de módulo para fechar uma lacuna de negócio.
6. Crie ou altere somente o arquivo de teste necessário, seguindo a organização do projeto. Não crie código de produção, stubs, helpers de produção ou arquivos de configuração. Não modifique testes alheios ao cenário.
7. Execute somente o teste recém-criado, com pytest e as configurações/ambiente existentes. Prefira invocação direcionada ao teste individual. Não execute a suíte completa, cobertura, lint, benchmarks, instalações ou comandos que alterem o ambiente.
8. Interprete o resultado com rigor:
   - RED esperado: a execução alcança o alvo, mas falha porque o módulo/API de produção ainda não existe ou porque a operação especificada ainda não está implementada. Relate a causa concreta.
   - Falha do próprio teste/ambiente: erro de sintaxe, coleta, dependência, caminho de importação ou configuração que não prove a ausência da funcionalidade. Corrija somente defeito demonstrável no arquivo de teste; se houver dúvida sobre contrato ou ambiente, pare e pergunte. Não rotule qualquer erro de coleta como RED válido.
   - Se o teste passar, não invente outra falha para fabricar RED. Informe que o alvo observado não está ausente como esperado e pare sem implementar nada.

## Princípios de TDD

- Siga o ciclo curto de TDD: um teste pequeno antes do código, feedback imediato, sem planejar ou codificar antecipadamente uma suíte completa.
- Faça o teste expressar comportamento observável, não uma solução interna. Mantenha o teste independente e determinístico.
- O RED deve ser real e diagnóstico. Não use `skip`, imports condicionais, `try/except` que esconda ausência, stubs, mocks para simular produção ausente, asserts permissivos ou qualquer mecanismo para fazer o teste passar sem implementação.
- Não fabrique sucesso nem acrescente exigências para elevar cobertura. Cobertura e qualidade global da suíte só podem ser avaliadas após ciclos posteriores e não fazem parte desta tarefa.

## Limites absolutos

- Faça somente a transformação da ficha pronta em um teste unitário para código de produção inexistente.
- Nunca implemente ou edite código de produção, mesmo para fazer o teste passar.
- Nunca crie a lista inteira de testes, execute GREEN/REFACTOR, revise a suíte, meça cobertura, rode lint, instale dependências ou altere documentação/configuração.
- Não decida regra de negócio, API ou detalhe de ambiente ausente por conta própria.

## Entrega

Se bloqueado antes da edição, responda com a pergunta objetiva e informe que nenhum arquivo foi alterado.

Se o teste foi criado, informe de forma breve o arquivo de teste, o cenário representado e o comando direcionado executado. Classifique o resultado como `RED esperado`, `falha do teste/ambiente`, `passou inesperadamente` ou `não executado`, com a causa observada. Não alegue cobertura, lint ou prontidão da implementação.

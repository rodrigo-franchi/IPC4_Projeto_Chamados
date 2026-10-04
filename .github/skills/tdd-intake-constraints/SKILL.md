---
name: tdd-intake-constraints
description: "Colete restrições de linguagem, ambiente e validação que afetam a escrita e execução dos testes TDD. Use para registrar versões, framework, lint, cobertura e comandos sem escolher ferramentas não aprovadas."
argument-hint: "Informe linguagem/versão suportada, framework de teste e requisitos de qualidade ou execução."
user-invocable: true
---

# Coletar restrições técnicas

## Entrada aceita

Linguagem e versões suportadas; ambiente de execução; framework de testes; dependências permitidas; linters, métricas ou comandos exigidos; CI ou limitações de plataforma. Pode haver dados parciais.

## Procedimento

1. Registre somente restrições confirmadas pelo usuário ou projeto.
2. No workspace, procure configurações existentes antes de perguntar: manifesto do projeto, configuração de testes/lint/cobertura e workflows.
3. Distinga versão mínima/matriz suportada de versão instalada localmente. Não interprete “última estável” como número fixo sem verificar a fonte/data pertinente.
4. Não escolha ferramenta ausente nem instale dependências. Se a restrição não estiver definida e não bloquear a seleção de um teste simples, registre-a como pendente, não bloqueante.

## Restrições

- Não recomende desenho de produção com base apenas na ferramenta de testes.
- Não declare que uma meta foi atingida sem medição.
- Não altere arquivos de configuração ou código.

## Saída obrigatória

Retorne somente este bloco, mantendo os rótulos e valores de status:

```yaml
status: FECHADO # Valores permitidos: FECHADO, PENDENTE
Use `PENDENTE` para restrições necessárias ao ambiente solicitado que ainda não foram informadas nem encontradas. Requisitos não essenciais podem ser listados como “não informado”.
item: restricoes_tecnicas
dado: "linguagem_versao: ...; testes: ...; cobertura: ...; lint: ...; execucao: ..."
evidencia: "usuário | caminhos de configuração no repositório | nenhuma"
pendencia: "nenhuma | pergunta objetiva sobre restrição essencial ausente"
```

Na saída real, escreva `dado:` sem espaço inicial antes do rótulo. Use `PENDENTE` para restrições necessárias ao ambiente solicitado que ainda não foram informadas nem encontradas. Requisitos não essenciais podem ser listados como “não informado”.

---
name: tdd-intake-test-context
description: "Especifique o contexto mínimo para tornar o próximo cenário TDD um teste concreto: interface pública, preparação, invocação e resultado verificável. Use antes de escrever o teste."
argument-hint: "Informe como o comportamento é acessado e um exemplo de entrada e resultado esperado."
user-invocable: true
---

# Coletar contexto do teste

## Entrada aceita

O cenário escolhido e qualquer contexto conhecido sobre a interface, os dados necessários e o resultado observável. O nome exato da interface pode ser decidido ao escrever o teste, desde que a fronteira pública esteja clara.

## Procedimento

1. Registre: interface/fronteira pública a exercitar; preparação/entrada; ação/invocação; resultado/assert observável.
2. Se o código já existir, aceite referências à API pública documentada. Se ainda não existir, não exija path de import ou detalhes internos; explicite o que ainda precisará ser definido pelo primeiro teste.
3. Para API HTTP, capture método/rota, entrada relevante e resposta/efeito esperado somente quando especificados.
4. Marque como pendente qualquer parte necessária para executar o teste cujo resultado não possa ser inferido com segurança.

## Restrições

- Não desenhe a implementação interna nem imponha mocks, fixtures ou ferramentas específicas.
- Não invente assinatura, dados, retorno, exceção ou status HTTP.
- Não escreva código ou testes.

## Saída obrigatória

Retorne somente este bloco, mantendo os rótulos e valores de status:

```yaml
status: FECHADO # Valores permitidos: FECHADO, PENDENTE
Use `FECHADO` se o primeiro teste puder ser escrito sem adivinhar comportamento; incerteza de nome interno não bloqueia se a fronteira pública for clara.
item: contexto_do_teste
dado: "interface_publica: ...; preparacao_entrada: ...; invocacao: ...; resultado_assert: ..."
evidencia: "usuário | caminho e referência no repositório | nenhuma"
pendencia: "nenhuma | pergunta objetiva sobre a informação essencial ausente"
```

Na saída real, escreva `dado:` sem espaço inicial antes do rótulo. Use `FECHADO` se o primeiro teste puder ser escrito sem adivinhar comportamento; incerteza de nome interno não bloqueia se a fronteira pública for clara.

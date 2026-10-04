# Ficha de entrada TDD

## 1. Comportamento desejado
```yaml
status: FECHADO
item: comportamento_desejado
dado: "Receber uma lista de chamados com id, nome, prioridade e status e devolver a mesma lista reordenada por prioridade alta, média e baixa, preservando a ordem de chegada entre prioridades iguais. Prioridades desconhecidas geram erro identificando os IDs inválidos, com mensagem singular para um chamado e plural para vários. Lista vazia retorna lista vazia."
evidencia: "usuário e testes validados"
pendencia: "nenhuma"
```

## 2. Lista inicial de cenários
```yaml
status: FECHADO
item: lista_de_cenarios
dado: "1. Chamados com prioridades alta, média e baixa — ordenar nessa sequência. 2. Chamados com a mesma prioridade — preservar ordem de chegada. 3. Um chamado com prioridade desconhecida — erro singular com seu ID. 4. Vários chamados com prioridades desconhecidas — erro plural com seus IDs. 5. Lista vazia — retorna lista vazia."
evidencia: "usuário e testes validados"
pendencia: "nenhuma"
```

## 3. Próximo cenário
```yaml
status: FECHADO
item: proximo_cenario
dado: "Dada uma lista com um chamado de cada prioridade, recebida na ordem baixa, alta, média, devolver os mesmos chamados na ordem alta, média, baixa; demais: estabilidade entre prioridades iguais, lista vazia, e erro para prioridades desconhecidas com mensagem singular/plural conforme a quantidade de IDs inválidos."
evidencia: "usuário; cenário derivado do comportamento confirmado e validado por testes"
pendencia: "nenhuma"
```

## 4. Contexto do teste
```yaml
status: FECHADO
item: contexto_do_teste
dado: "interface_publica: operação de uma biblioteca Python que recebe uma lista de chamados; nome e caminho de importação poderão ser definidos pelo primeiro teste. preparacao_entrada: chamados com id, nome, prioridade e status; prioridades válidas 'alta', 'média' e 'baixa'. invocacao: fornecer chamados na ordem baixa, alta, média; também listas vazias e listas com prioridades inválidas. resultado_assert: receber os mesmos chamados, com os dados preservados, na ordem alta, média, baixa; para lista vazia, retornar [] sem erro; para prioridades desconhecidas, levantar ValueError com mensagem singular ou plural com os IDs inválidos."
evidencia: "usuário e testes validados"
pendencia: "nenhuma"
```

## 5. Restrições técnicas
```yaml
status: FECHADO
item: restricoes_tecnicas
dado: "linguagem_versao: Python; versão suportada não informada. testes: pytest, preferência deste fluxo; configuração do projeto-alvo não identificada. cobertura: linhas estritamente superior a 80%, preferência deste fluxo; não medida. lint: Ruff E, F, I, B, preferência deste fluxo; configuração do projeto-alvo não identificada. execucao: não informada."
evidencia: "usuário e preferências deste fluxo; nenhuma configuração identificada para esta biblioteca"
pendencia: "nenhuma para o próximo teste; versão e configuração específicas do projeto permanecem não informadas."
```

## Prontidão
- `PRONTO_PARA_TDD`: SIM
- `Bloqueios`: nenhum
- `Pendências não bloqueantes`: nome e caminho da operação pública; versão Python e configuração do projeto.
- `Próximo passo`: handoff ao agente TDD Next Test Writer com esta ficha; não escrever os testes neste agente.

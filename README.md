# Citizen Assist AI

Assistente de terminal em Python que orienta **jovens no primeiro emprego** sobre documentos e direitos básicos e inclui um módulo de **energia e sustentabilidade** para ajudar jovens e suas famílias a compreender o consumo residencial e comparar eficiência energética com geração solar.

## Integrantes
| Nome | RM |
|------|----|
| Aneliza Rondina Bonafé | 572977 |
| Rafaella Ferreira de Moraes | 571030 |

## Público e problema
- **Público:** jovens que estão procurando o primeiro emprego e suas famílias.
- **Problema original:** informações sobre documentos e direitos estão espalhadas e usam linguagem técnica.
- **Contribuição de energia:** orientar o público a identificar desperdício na iluminação doméstica, calcular consumo em kWh e comparar troca por LED com geração solar fotovoltaica.

## Como executar
Requisitos: Python 3 (não usa bibliotecas externas).

```bash
python main.py
```

Menu: 1) perguntar em texto livre, 2) navegar por categorias, 3) ver indicadores, 4) exportar CSV, 5) energia e sustentabilidade, 0) sair.

## Módulo de energia
A opção 5 do menu principal apresenta uma funcionalidade interativa de análise energética.

O usuário pode escolher entre:

**1. Ver análise do cenário de referência**

Apresenta uma análise considerando:
- Cinco lâmpadas convencionais de 60 W.
- Cinco horas de utilização por dia.
- Trinta dias de utilização por mês.
- Substituição por lâmpadas LED de 9 W.

**2. Calcular meu consumo e comparar alternativas**

Permite informar:
- Quantidade de lâmpadas.
- Potência das lâmpadas atuais em watts.
- Potência das lâmpadas LED em watts.
- Horas de utilização por dia.
- Dias de utilização por mês.
- Tarifa de energia em R$/kWh.

Com essas informações, o sistema calcula:

- Consumo mensal antes da substituição.
- Consumo mensal após a substituição por LED.
- Economia mensal em kWh.
- Percentual de redução do consumo.
- Economia financeira estimada.
- Custo ilustrativo da substituição das lâmpadas.
- Estimativa de geração fotovoltaica.
- Potência teórica necessária para o sistema solar.
- Custo indicativo e retorno simples estimado.

  ### Exemplo de cálculo

Considerando cinco lâmpadas de 60 W, utilizadas cinco horas por dia durante trinta dias:

Consumo convencional:

45 kWh/mês.

Consumo com lâmpadas LED de 9 W:

6,75 kWh/mês.

Redução estimada:

38,25 kWh/mês, equivalente a 85%.

Considerando uma tarifa de R$ 0,75468/kWh, a economia estimada é de aproximadamente R$ 28,87 por mês.

### Comparação das alternativas

O sistema compara:

- Eficiência energética: substituição de lâmpadas convencionais por LED.
- Energia renovável: geração de eletricidade por meio de painéis solares fotovoltaicos.

A estimativa solar considera uma produtividade hipotética de 130 kWh/kWp por mês e um custo indicativo de R$ 3,62/Wp.

Esses valores são parâmetros de simulação, não representam orçamento comercial.


## Estrutura
```
citizen-assist-ai/
├── README.md
├── main.py
├── assistente.py
├── orientacao.py
├── base_conhecimento.py
├── energia.py                 # novo módulo de energia
├── docs/
│   └── analise_energetica.md  # relatório técnico da contribuição
├── data/
│   ├── base_conhecimento.json
│   ├── historico.json
│   └── atendimentos.csv
```


## Testes com usuários

### Objetivo
Avaliar a facilidade de utilização, a clareza das informações e a utilidade das funcionalidades do Citizen Assist AI, especialmente do módulo de Energia e Sustentabilidade.

### Metodologia
Foi elaborado um cenário de avaliação com 3 participantes externos à equipe, considerando 10 interações com o assistente. Foram propostas tarefas relacionadas à navegação pelo sistema, consulta de informações e utilização dos cálculos de consumo energético.

### Resultados simulados

| Indicador | Resultado |
|---|---:|
| Participantes considerados | 3 |
| Interações | 10 |
| Tarefas concluídas sem ajuda | 8 |
| Tarefas que necessitaram de orientação | 2 |
| Avaliações positivas de clareza | 8 |
| Avaliações que apontaram dificuldades | 2 |

### Distribuição das avaliações

- 80% das interações foram concluídas sem necessidade de ajuda.
- 80% das avaliações indicaram que as informações apresentadas eram claras.
- 20% apontaram dificuldades na compreensão de alguns resultados.
- Os principais pontos de atenção foram a interpretação dos cálculos de consumo e o entendimento dos custos estimados de energia solar.

### Melhorias propostas

A partir dos resultados, foram identificadas as seguintes oportunidades de melhoria:

1. Simplificar a explicação das fórmulas utilizadas nos cálculos de consumo.
2. Destacar que os valores de economia e instalação solar são estimativas.
3. Melhorar a apresentação das comparações entre as alternativas energéticas.
4. Utilizar linguagem mais acessível para pessoas sem conhecimento técnico sobre eletricidade.

## Fontes da base original
- https://www.gov.br/pt-br/servicos/obter-a-carteira-de-trabalho
- https://www.gov.br/trabalho-e-emprego
- https://www.gov.br/receitafederal
- https://www.tse.jus.br
- https://www.caixa.gov.br
- https://meu.inss.gov.br
- https://www.gov.br

Os campos `verificado_em` da base original ainda estão como `A CONFERIR` e devem ser atualizados após checagem das páginas oficiais.

## Vídeo técnico
Link (YouTube, não listado, até 3 minutos): (preencher)

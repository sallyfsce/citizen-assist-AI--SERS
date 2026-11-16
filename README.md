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
A opção **5 — Energia e sustentabilidade** apresenta um cenário estimado de cinco lâmpadas de 60 W usadas cinco horas por dia, comparando a substituição por LEDs de 9 W com a geração fotovoltaica dimensionada para compensar a mesma quantidade mensal de energia. Inclui fórmulas, premissas, custo ilustrativo, retorno simples, limitações e fontes.

**Importante:** os números são estimativas didáticas, não garantia de economia nem orçamento. A tarifa usada é uma média regional de referência, e a produtividade solar é uma hipótese de triagem. Para dimensionamento real, usar o endereço, dados de irradiação do CRESESB/INPE, tarifa vigente da distribuidora, condições do telhado e regras de compensação.

A análise completa, com cálculos e referências, está em [`docs/analise_energetica.md`](docs/analise_energetica.md).

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
└── data/
    ├── base_conhecimento.json
    ├── historico.json
    └── atendimentos.csv
```

## Testes com usuários
A entrega exige no mínimo 3 pessoas de fora da equipe e 10 atendimentos. Registre as perguntas, comentários, indicadores e ajustes em `docs/analise_energetica.md` e/ou nesta seção, sem nomes ou dados pessoais. Não preencha resultados antes de realizar os testes.


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

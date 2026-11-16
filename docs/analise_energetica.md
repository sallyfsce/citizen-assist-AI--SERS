# Contribuição da disciplina — Energia e sustentabilidade

## 1. Público e necessidade

O Citizen Assist AI original orienta jovens no primeiro emprego sobre documentos e direitos básicos. A contribuição de energia mantém esse público e amplia o apoio para jovens e suas famílias que desejam compreender e reduzir o consumo doméstico de eletricidade, com linguagem acessível e sem exigir dados pessoais.

**Problema delimitado:** gasto evitável com iluminação residencial. O recorte permite demonstrar potência (W), energia (kWh), eficiência energética e comparação com uma alternativa renovável.

## 2. Dados e premissas

O cenário é **estimado**, não uma medição de uma residência real:

- 5 lâmpadas incandescentes de 60 W;
- substituição por 5 lâmpadas LED de 9 W, mantendo a mesma quantidade de pontos e o mesmo tempo de iluminação;
- uso de 5 horas por dia e 30 dias por mês;
- tarifa de referência de R$ 0,75468/kWh, correspondente à tarifa média residencial do Sudeste divulgada pelo MME para dezembro de 2025 (R$ 754,68/MWh). Não representa a tarifa final de uma unidade consumidora específica.

Fórmula: `Energia (kWh) = Potência (W) × horas/dia × dias × quantidade ÷ 1.000`.

## 3. Cálculo do consumo

**Situação inicial:**

`5 × 60 W × 5 h/dia × 30 dias ÷ 1.000 = 45,00 kWh/mês`.

**Com LED:**

`5 × 9 W × 5 h/dia × 30 dias ÷ 1.000 = 6,75 kWh/mês`.

**Economia:** `45,00 − 6,75 = 38,25 kWh/mês`, ou `38,25 ÷ 45 × 100 = 85%`.

**Economia financeira estimada:** `38,25 × R$ 0,75468 = R$ 28,87/mês` (aproximadamente R$ 346,40/ano), antes de considerar particularidades da fatura.

## 4. Comparação de alternativas para a mesma necessidade

As alternativas são comparadas pela mesma referência: evitar ou compensar aproximadamente 38,25 kWh por mês associados ao serviço de iluminação.

| Critério | Alternativa A — eficiência (LED) | Alternativa B — solar fotovoltaica |
|---|---|---|
| Ação | Trocar cinco lâmpadas de 60 W por LED de 9 W | Instalar geração fotovoltaica conectada à rede |
| Resultado energético | Reduz o consumo em 38,25 kWh/mês | Dimensionamento preliminar para gerar cerca de 38,25 kWh/mês |
| Potência/quantidade | 5 LEDs de 9 W | `38,25 ÷ 130 = 0,294 kWp` (aprox. 294 Wp) |
| Custo usado no exemplo | R$ 50,00 estimados (R$ 10 por lâmpada; hipótese didática) | R$ 1.065 estimados (294 Wp × R$ 3,62/Wp) |
| Retorno simples | Cerca de 1,7 mês | Cerca de 36,9 meses |
| Viabilidade | Baixo custo e instalação simples; aplicável a quem controla a iluminação | Requer área sem sombra, telhado/estrutura adequada, projeto, conexão e investimento inicial |
| Impacto ambiental | Menor demanda de eletricidade e menor necessidade de geração na rede | Gera eletricidade renovável; há impactos de fabricação, transporte e descarte dos módulos e inversor |

**Como interpretar custos e retorno:** o preço de R$ 3,62/Wp é a média publicada pela Greener para sistemas residenciais de 2 kWp em junho de 2026. Aplicá-lo a um sistema muito menor que 2 kWp é uma extrapolação matemática, não um preço de mercado confirmado; o custo real por Wp de um sistema pequeno pode ser maior e talvez nem exista oferta comercial nesse porte. O custo das LEDs também é uma hipótese (R$ 10/unidade), a substituir por cotação local. Retorno simples = custo inicial ÷ economia mensal estimada. Não inclui manutenção, financiamento, degradação, custo de disponibilidade, compensação de créditos, Fio B, impostos ou reajustes tarifários.

## 5. Recomendação ao usuário

Para quem deseja reduzir a conta com pouco investimento, priorizar lâmpadas LED eficientes e desligar luzes desnecessárias é a recomendação inicial mais acessível. A energia solar pode ser considerada quando houver imóvel adequado, permanência de longo prazo e capital ou financiamento viável; antes de decidir, solicitar propostas de empresas qualificadas e simulação com dados do endereço e da distribuidora. Não afirmar que a conta ficará zerada.

## 6. Integração ao Citizen Assist AI

Foi acrescentada a opção **5 — Energia e sustentabilidade** no menu do programa. Ela apresenta público, problema, fórmula, consumo inicial e após a troca, economia, comparação entre LED e geração fotovoltaica, custos estimados, limitações e referências. O módulo fica em `energia.py`, separado da base original de orientações sobre trabalho e documentos.

## 7. Referências

1. Ministério de Minas e Energia (MME). *Informativo Tarifário do Setor Elétrico — ano 2025*, Tabela 7, tarifa média residencial de dezembro de 2025. https://www.gov.br/mme/pt-br/assuntos/secretarias/secretaria-nacional-energia-eletrica/informativo-tarifario-do-setor-eletrico/informativo-tarifario-do-setor-eletrico-ano-2025.pdf
2. Greener. *Estudo Estratégico de Soluções Energéticas Distribuídas — 2º semestre de 2026*, tabela de preços médios de sistemas fotovoltaicos, junho de 2026. https://greenerstorage.blob.core.windows.net/public/estudos/SED_2S_2026.pdf
3. INPE/LABREN. *Atlas Brasileiro de Energia Solar*. Base pública de potencial solar com dados climatológicos por localidade. https://www.gov.br/pt-br/servicos/obter-dados-do-atlas-brasileiro-de-energia-solar-atlas-solar
4. CRESESB/CEPEL. *SunData*. Ferramenta de consulta de irradiação solar por localidade; a própria ferramenta alerta que os valores são indicativos. https://www.cresesb.cepel.br/index.php?section=sundata
5. ANEEL. *Tarifas e Informações Econômico-Financeiras*. Consultar tarifa vigente da distribuidora; os valores homologados não incluem necessariamente tributos, bandeiras e demais itens da fatura. https://www.gov.br/aneel/pt-br/centrais-de-conteudos/relatorios-e-indicadores/tarifas-e-informacoes-economico-financeiras

## 9. Limitações gerais

O cenário de iluminação é ilustrativo e deve ser substituído por potência, quantidade, tempo de uso e tarifa da residência real. A produtividade solar de 130 kWh/kWp/mês é uma hipótese de triagem para o exemplo, não uma extração de dados de um endereço específico. Para um projeto real, consultar SunData/Atlas para a localidade e solicitar avaliação técnica. A geração e a economia variam com sazonalidade, orientação, inclinação, sombras, perdas, regras de compensação e contrato com a distribuidora.

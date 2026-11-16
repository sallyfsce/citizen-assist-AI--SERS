"""Módulo didático de energia e sustentabilidade do Citizen Assist AI.

Os valores-padrão são um cenário estimado e editável, não uma proposta comercial.
"""

# Cenário de referência: 5 lâmpadas incandescentes de 60 W substituídas por LED de 9 W.
QUANTIDADE_LAMPADAS = 5
POTENCIA_ANTIGA_W = 60
POTENCIA_LED_W = 9
HORAS_DIA = 5
DIAS_MES = 30
TARIFA_R_KWH = 0.75468  # média residencial Sudeste, MME/ANEEL, dez/2025

# Sistema FV: aproximação didática. O dimensionamento real depende do endereço,
# orientação/inclinação, sombras, perdas, distribuidora e regras de compensação.
PRODUTIVIDADE_KWH_KWP_MES = 130.0
PRECO_SISTEMA_R_WP = 3.62  # Greener, sistema residencial 2 kWp, jun/2026


def consumo_mensal(potencia_w, horas_dia, dias_mes=30, quantidade=1):
    """Retorna kWh/mês: potência (W) × horas/dia × dias × quantidade / 1000."""
    return potencia_w * horas_dia * dias_mes * quantidade / 1000


def analisar():
    antigo = consumo_mensal(POTENCIA_ANTIGA_W, HORAS_DIA, DIAS_MES, QUANTIDADE_LAMPADAS)
    led = consumo_mensal(POTENCIA_LED_W, HORAS_DIA, DIAS_MES, QUANTIDADE_LAMPADAS)
    economia = antigo - led
    economia_reais = economia * TARIFA_R_KWH

    # Potência FV teórica para compensar a energia economizada no cenário de iluminação.
    potencia_fv_kwp = economia / PRODUTIVIDADE_KWH_KWP_MES
    potencia_fv_wp = potencia_fv_kwp * 1000
    custo_fv_estimado = potencia_fv_wp * PRECO_SISTEMA_R_WP
    retorno_fv_meses = custo_fv_estimado / economia_reais if economia_reais else None

    # Estimativa ilustrativa de aquisição das cinco lâmpadas LED a R$ 10 cada.
    custo_led_estimado = QUANTIDADE_LAMPADAS * 10.0
    retorno_led_meses = custo_led_estimado / economia_reais if economia_reais else None

    return {
        "consumo_antigo_kwh_mes": antigo,
        "consumo_led_kwh_mes": led,
        "economia_kwh_mes": economia,
        "economia_percentual": economia / antigo * 100 if antigo else 0,
        "economia_reais_mes": economia_reais,
        "potencia_fv_kwp": potencia_fv_kwp,
        "geracao_fv_kwh_mes": economia,
        "custo_led_estimado": custo_led_estimado,
        "retorno_led_meses": retorno_led_meses,
        "custo_fv_estimado": custo_fv_estimado,
        "retorno_fv_meses": retorno_fv_meses,
    }


def exibir():
    r = analisar()
    print("\n=== ENERGIA E SUSTENTABILIDADE ===")
    print("Público: jovens no primeiro emprego e suas famílias, buscando reduzir a conta de luz.")
    print("Necessidade analisada: iluminação de cinco pontos por cinco horas ao dia.")
    print("\nCENÁRIO DE CONSUMO (estimado)")
    print(f"5 lâmpadas de 60 W: {r['consumo_antigo_kwh_mes']:.2f} kWh/mês")
    print(f"5 lâmpadas LED de 9 W: {r['consumo_led_kwh_mes']:.2f} kWh/mês")
    print(f"Redução: {r['economia_kwh_mes']:.2f} kWh/mês ({r['economia_percentual']:.1f}%)")
    print(f"Economia estimada: R$ {r['economia_reais_mes']:.2f}/mês")

    print("\nCOMPARAÇÃO DE ALTERNATIVAS PARA A MESMA ECONOMIA DE ENERGIA")
    print("1) Eficiência: trocar cinco lâmpadas de 60 W por LED de 9 W.")
    print(f"   Custo ilustrativo das LEDs (R$ 10/unidade): R$ {r['custo_led_estimado']:.2f}.")
    print(f"   Retorno simples estimado: {r['retorno_led_meses']:.1f} meses.")
    print("   Vantagens: baixo investimento, instalação simples e menor consumo contínuo.")
    print("   Limites: depende das horas de uso e da potência real das lâmpadas substituídas.")
    print("2) Fonte renovável: microgeração solar fotovoltaica conectada à rede.")
    print(
        f"   Potência teórica para gerar cerca de {r['geracao_fv_kwh_mes']:.2f} kWh/mês: {r['potencia_fv_kwp']:.3f} kWp.")
    print(
        f"   Custo indicativo por extrapolação: R$ {r['custo_fv_estimado']:.2f}; retorno simples: {r['retorno_fv_meses']:.1f} meses.")
    print("   Vantagens: geração renovável e redução da energia comprada da rede.")
    print("   Limites: exige telhado/área adequada, investimento inicial, projeto e aprovação da distribuidora.")

    print("\nPREMISSAS E LIMITAÇÕES")
    print("- 30 dias/mês; 5 h/dia; cinco lâmpadas; 60 W antigas e 9 W LED.")
    print(
        f"- Tarifa de referência: R$ {TARIFA_R_KWH:.5f}/kWh (média residencial Sudeste, dez/2025; não é a tarifa individual).")
    print(f"- Produtividade solar de 130 kWh/kWp/mês é uma hipótese de triagem, não simulação do telhado.")
    print(
        "- Custo solar usa R$ 3,62/Wp, média Greener para sistema residencial de 2 kWp (jun/2026), extrapolada para potência menor; não é orçamento e pode subestimar o custo de um sistema pequeno.")
    print(
        "- Retorno simples ignora manutenção, degradação, financiamento, custo de disponibilidade, Fio B, tributos e mudanças tarifárias.")
    print(
        "- A geração real varia com cidade, orientação, inclinação, sombras, clima e perdas. Consulte CRESESB/SunData e um profissional.")
    print("\nFONTES")
    print(
        "MME/ANEEL – Informativo Tarifário 2025: https://www.gov.br/mme/pt-br/assuntos/secretarias/secretaria-nacional-energia-eletrica/informativo-tarifario-do-setor-eletrico/informativo-tarifario-do-setor-eletrico-ano-2025.pdf")
    print(
        "Greener – Pesquisa SED, junho/2026: https://greenerstorage.blob.core.windows.net/public/estudos/SED_2S_2026.pdf")
    print(
        "INPE – Atlas Brasileiro de Energia Solar: https://www.gov.br/pt-br/servicos/obter-dados-do-atlas-brasileiro-de-energia-solar-atlas-solar")
    print("CRESESB/CEPEL – SunData: https://www.cresesb.cepel.br/index.php?section=sundata")
    print(
        "ANEEL – Tarifas vigentes por distribuidora: https://www.gov.br/aneel/pt-br/centrais-de-conteudos/relatorios-e-indicadores/tarifas-e-informacoes-economico-financeiras")
    print("\nAviso: os resultados são estimativas educacionais, não garantias de economia ou geração.")
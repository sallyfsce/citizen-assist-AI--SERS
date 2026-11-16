"""Módulo interativo de análise energética do Citizen Assist AI.

Os cálculos são estimativas educacionais. Tarifas e custos devem ser
substituídos por dados reais antes de uma decisão de compra ou instalação.
"""

# Premissas editáveis do cenário de referência
QUANTIDADE_LAMPADAS = 5
POTENCIA_ANTIGA_W = 60
POTENCIA_LED_W = 9
HORAS_DIA = 5
DIAS_MES = 30
TARIFA_R_KWH = 0.75468

# Hipóteses para estimativa fotovoltaica (não constituem orçamento)
PRODUTIVIDADE_KWH_KWP_MES = 130.0
PRECO_SISTEMA_R_WP = 3.62
PRECO_LED_UNIDADE = 10.0


def consumo_mensal(potencia_w, horas_dia, dias_mes=30, quantidade=1):
    """Calcula consumo em kWh/mês."""
    return potencia_w * horas_dia * dias_mes * quantidade / 1000


def analisar(quantidade=QUANTIDADE_LAMPADAS,
             potencia_antiga_w=POTENCIA_ANTIGA_W,
             potencia_led_w=POTENCIA_LED_W,
             horas_dia=HORAS_DIA,
             dias_mes=DIAS_MES,
             tarifa=TARIFA_R_KWH):
    """Calcula o cenário LED e a estimativa solar para a mesma iluminação."""
    consumo_antigo = consumo_mensal(
        potencia_antiga_w, horas_dia, dias_mes, quantidade
    )
    consumo_led = consumo_mensal(
        potencia_led_w, horas_dia, dias_mes, quantidade
    )
    economia = max(consumo_antigo - consumo_led, 0)
    economia_reais = economia * tarifa
    custo_led = quantidade * PRECO_LED_UNIDADE
    retorno_led = custo_led / economia_reais if economia_reais > 0 else None

    # Referência comparável: dimensionar FV para gerar a mesma quantidade
    # de energia que seria economizada pela troca para LED.
    potencia_fv_kwp = (
        economia / PRODUTIVIDADE_KWH_KWP_MES
        if PRODUTIVIDADE_KWH_KWP_MES > 0 else 0
    )
    custo_fv = potencia_fv_kwp * 1000 * PRECO_SISTEMA_R_WP
    economia_solar_reais = economia * tarifa
    retorno_fv = (
        custo_fv / economia_solar_reais
        if economia_solar_reais > 0 else None
    )

    return {
        "consumo_antigo_kwh_mes": consumo_antigo,
        "consumo_led_kwh_mes": consumo_led,
        "economia_kwh_mes": economia,
        "economia_percentual": (
            economia / consumo_antigo * 100 if consumo_antigo > 0 else 0
        ),
        "economia_reais_mes": economia_reais,
        "custo_led_estimado": custo_led,
        "retorno_led_meses": retorno_led,
        "potencia_fv_kwp": potencia_fv_kwp,
        "geracao_fv_kwh_mes": economia,
        "custo_fv_estimado": custo_fv,
        "economia_solar_reais_mes": economia_solar_reais,
        "retorno_fv_meses": retorno_fv,
    }


def _ler_decimal(mensagem, minimo, maximo, inteiro=False):
    """Lê número aceitando vírgula decimal e valida limites."""
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        try:
            valor_float = float(texto)
            if not minimo <= valor_float <= maximo:
                raise ValueError
            if inteiro:
                if not valor_float.is_integer():
                    raise ValueError
                return int(valor_float)
            return valor_float
        except ValueError:
            unidade = "um número inteiro" if inteiro else "um número"
            print(f"Entrada inválida. Digite {unidade} entre {minimo} e {maximo}.")


def _formatar_retorno(meses):
    return f"{meses:.1f} meses" if meses is not None else "não calculável"


def exibir_resultado(r, quantidade, potencia_antiga, potencia_led,
                     horas, dias, tarifa):
    print("\n=== RESULTADO DA ANÁLISE ENERGÉTICA ===")
    print("\nDADOS INFORMADOS")
    print(f"Quantidade de lâmpadas: {quantidade}")
    print(f"Potência antiga: {potencia_antiga} W por lâmpada")
    print(f"Potência LED: {potencia_led} W por lâmpada")
    print(f"Uso diário: {horas:g} hora(s)")
    print(f"Período: {dias} dias/mês")
    print(f"Tarifa informada: R$ {tarifa:.4f}/kWh")

    print("\n1. CONSUMO E EFICIÊNCIA ENERGÉTICA")
    print(f"Consumo antes da troca: {r['consumo_antigo_kwh_mes']:.2f} kWh/mês")
    print(f"Consumo com LED: {r['consumo_led_kwh_mes']:.2f} kWh/mês")
    print(f"Redução estimada: {r['economia_kwh_mes']:.2f} kWh/mês "
          f"({r['economia_percentual']:.1f}%)")
    print(f"Economia financeira estimada: R$ {r['economia_reais_mes']:.2f}/mês")
    print(f"Custo ilustrativo das LEDs: R$ {r['custo_led_estimado']:.2f}")
    print("Retorno simples estimado da troca: "
          f"{_formatar_retorno(r['retorno_led_meses'])}")

    print("\n2. ALTERNATIVA RENOVÁVEL: ENERGIA SOLAR FOTOVOLTAICA")
    print("A estimativa considera gerar a mesma quantidade de energia "
          "que seria economizada pela troca para LED.")
    print(f"Energia de referência: {r['geracao_fv_kwh_mes']:.2f} kWh/mês")
    print(f"Potência fotovoltaica teórica: {r['potencia_fv_kwp']:.3f} kWp")
    print(f"Custo fotovoltaico indicativo: R$ {r['custo_fv_estimado']:.2f}")
    print(f"Valor de energia potencialmente compensada: "
          f"R$ {r['economia_solar_reais_mes']:.2f}/mês")
    print("Retorno simples ilustrativo: "
          f"{_formatar_retorno(r['retorno_fv_meses'])}")

    print("\n3. COMPARAÇÃO E RECOMENDAÇÃO")
    print("- LED: tende a exigir investimento inicial menor e reduz o consumo "
          "diretamente no equipamento.")
    print("- Solar: utiliza fonte renovável para gerar energia, mas exige "
          "projeto, área adequada e investimento inicial maior.")
    print("- Para uma primeira medida de baixo custo, avaliar a substituição "
          "por LED e hábitos de uso consciente.")
    print("- A viabilidade solar depende de análise do imóvel e da distribuidora.")

    print("\n4. PREMISSAS E LIMITAÇÕES")
    print("- O cálculo usa potência nominal, horas de uso e dias informados.")
    print("- O custo LED usa hipótese de R$ 10,00 por unidade; substitua por cotação.")
    print(f"- Solar: produtividade hipotética de "
          f"{PRODUTIVIDADE_KWH_KWP_MES:.0f} kWh/kWp/mês.")
    print(f"- Solar: custo de referência de R$ {PRECO_SISTEMA_R_WP:.2f}/Wp, "
          "extrapolado; não é orçamento.")
    print("- Não considera tributos, bandeiras, custo de disponibilidade, "
          "Fio B, manutenção, financiamento, degradação ou sazonalidade.")
    print("- A geração real varia conforme localidade, orientação, inclinação, "
          "sombras e perdas do sistema.")
    print("- A economia na conta não é necessariamente igual ao valor calculado, "
          "pois a fatura possui outros componentes.")
    print("\n5. REFERÊNCIAS PARA CONFERÊNCIA")
    print("- ANEEL — tarifas por distribuidora: "
          "https://www.gov.br/aneel/pt-br/centrais-de-conteudos/relatorios-e-indicadores/tarifas-e-informacoes-economico-financeiras")
    print("- CRESESB/CEPEL — SunData: "
          "https://www.cresesb.cepel.br/index.php?section=sundata")
    print("- INPE — Atlas Brasileiro de Energia Solar: "
          "https://www.gov.br/pt-br/servicos/obter-dados-do-atlas-brasileiro-de-energia-solar-atlas-solar")
    print("\nAviso: resultados educacionais estimados, não garantias de economia, "
          "geração ou retorno.")


def _coletar_dados():
    print("\nInforme os dados da iluminação. Use valores da sua residência "
          "ou o cenário que deseja simular.")
    quantidade = _ler_decimal("Quantidade de lâmpadas: ", 1, 100, inteiro=True)
    potencia_antiga = _ler_decimal(
        "Potência de cada lâmpada atual (W): ", 1, 500
    )
    potencia_led = _ler_decimal(
        "Potência de cada lâmpada LED (W): ", 1, 200
    )
    horas = _ler_decimal("Horas de uso por dia (0,1 a 24): ", 0.1, 24)
    dias = _ler_decimal("Dias de uso por mês (1 a 31): ", 1, 31, inteiro=True)
    tarifa = _ler_decimal(
        "Tarifa de energia em R$/kWh (veja sua conta): ", 0.01, 10
    )
    return quantidade, potencia_antiga, potencia_led, horas, dias, tarifa


def exibir():
    """Menu de análise: cenário de referência ou simulação personalizada."""
    while True:
        print("\n=== ENERGIA E SUSTENTABILIDADE ===")
        print("1. Ver análise do cenário de referência")
        print("2. Calcular meu consumo e comparar alternativas")
        print("0. Voltar ao menu principal")
        opcao = input("Escolha: ").strip()

        if opcao == "0":
            return
        if opcao == "1":
            dados = (
                QUANTIDADE_LAMPADAS, POTENCIA_ANTIGA_W, POTENCIA_LED_W,
                HORAS_DIA, DIAS_MES, TARIFA_R_KWH
            )
        elif opcao == "2":
            try:
                dados = _coletar_dados()
            except (EOFError, KeyboardInterrupt):
                print("\nSimulação cancelada.")
                return
        else:
            print("Opção inválida. Digite 0, 1 ou 2.")
            continue

        quantidade, antiga, led, horas, dias, tarifa = dados
        resultado = analisar(
            quantidade=quantidade,
            potencia_antiga_w=antiga,
            potencia_led_w=led,
            horas_dia=horas,
            dias_mes=dias,
            tarifa=tarifa,
        )
        exibir_resultado(
            resultado, quantidade, antiga, led, horas, dias, tarifa
        )
        input("\nPressione ENTER para voltar ao menu de energia...")

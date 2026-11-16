import os

from base_conhecimento import BaseConhecimento
from assistente import Assistente
from energia import exibir as exibir_energia

PASTA = os.path.dirname(os.path.abspath(__file__))


def caminho(nome_arquivo):
    return os.path.join(PASTA, "data", nome_arquivo)


def main():
    base = BaseConhecimento(caminho("base_conhecimento.json"))
    base.carregar()  # lê o JSON e cria os objetos Orientacao

    assistente = Assistente("Citizen Assist AI", base,
                            caminho("historico.json"), caminho("atendimentos.csv"))

    print(f"=== {assistente.nome} ===")
    print("Orientação para jovens no primeiro emprego.")
    print("Aviso: este assistente NÃO é um canal oficial e não coleta dados pessoais.")

    try:
        while True:
            print("\n--- Menu ---")
            print("1. Fazer uma pergunta")
            print("2. Navegar por categorias")
            print("3. Ver indicadores")
            print("4. Exportar atendimentos para CSV")
            print("5. Energia e sustentabilidade")
            print("0. Sair")
            opcao = assistente.ler_numero("Escolha: ", 0, 5)
            if opcao == 1:
                assistente.perguntar()
            elif opcao == 2:
                assistente.navegar()
            elif opcao == 3:
                assistente.indicadores()
            elif opcao == 4:
                assistente.exportar_csv()
            elif opcao == 5:
                exibir_energia()
            else:
                assistente.encerrar()
                break
    except (EOFError, KeyboardInterrupt):
        print("\nEncerrando...")
        assistente.encerrar(pedir_nota=False)


if __name__ == "__main__":
    main()
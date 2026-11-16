import csv
import json
import os
import time
from datetime import datetime

AVISO_PESSOAL = "Atenção: não digite CPF, telefone ou e-mail. Reescreva."
CAMPOS_CSV = ["data", "sessao", "origem", "pergunta", "id_orientacao",
              "encontrou", "ajudou", "tentativas", "tempo_segundos",
              "nota_facilidade"]


class Assistente:
    """Quem conversa com o cidadão: atende, guarda o histórico e calcula indicadores."""

    def __init__(self, nome, base, caminho_historico="data/historico.json",
                 caminho_csv="data/atendimentos.csv"):
        self.nome = nome
        self.base = base  # composição: o Assistente TEM uma BaseConhecimento
        self.caminho_historico = caminho_historico
        self.caminho_csv = caminho_csv
        self.sessao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.historico = self.carregar_historico()

        # ---------- entradas seguras (nunca encerram o programa) ----------

    def ler_texto(self, mensagem):
        return input(mensagem).strip()

    def ler_numero(self, mensagem, minimo, maximo):
        while True:
            texto = self.ler_texto(mensagem)
            if texto.isdigit() and minimo <= int(texto) <= maximo:
                return int(texto)
            print(f"Opção inválida. Digite um número de {minimo} a {maximo}.")

    def ler_sim_nao(self, mensagem):
        while True:
            texto = self.ler_texto(mensagem).lower()
            if texto in ("s", "n"):
                return texto == "s"
            print("Resposta inválida. Digite apenas s ou n.")

    @staticmethod
    def contem_dado_pessoal(texto):
        """8 ou mais dígitos, ou um @, é tratado como dado pessoal."""
        digitos = sum(1 for letra in texto if letra.isdigit())
        return digitos >= 8 or "@" in texto

        # ---------- histórico ----------

    def carregar_historico(self):
        try:
            with open(self.caminho_historico, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            if isinstance(dados, list):
                return [item for item in dados if isinstance(item, dict)]
            print("Aviso: histórico em formato inesperado. Começando um novo.")
        except FileNotFoundError:
            pass
        except (json.JSONDecodeError, OSError, UnicodeDecodeError):
            print("Aviso: histórico corrompido. Começando um novo.")
        return []

    def salvar_historico(self):
        try:
            pasta = os.path.dirname(self.caminho_historico)
            if pasta:
                os.makedirs(pasta, exist_ok=True)
            with open(self.caminho_historico, "w", encoding="utf-8") as arquivo:
                json.dump(self.historico, arquivo, ensure_ascii=False, indent=2)
        except OSError:
            print("Aviso: não consegui salvar o histórico.")

    def registrar(self, origem, pergunta, id_orientacao, encontrou, ajudou,
                  tentativas, tempo):
        """Guarda um atendimento (um dicionário) no histórico."""
        atendimento = {
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "sessao": self.sessao,
            "origem": origem,
            "pergunta": pergunta,
            "id_orientacao": id_orientacao,
            "encontrou": encontrou,
            "ajudou": ajudou,
            "tentativas": tentativas,
            "tempo_segundos": tempo,
            "nota_facilidade": None,
        }
        self.historico.append(atendimento)
        self.salvar_historico()

        # ---------- atendimento por pergunta ----------

    def perguntar(self):
        inicio = time.time()
        tentativas = 0
        encontrou = False
        ajudou = False
        ultima_pergunta = ""
        pergunta_resposta = ""
        ultimo_id = None
        tempo_encontrar = None

        while True:
            texto = self.ler_texto("\nDigite sua dúvida (0 para voltar): ")
            if texto == "0":
                break
            if texto == "":
                print("Você não digitou nada. Tente de novo.")
                continue
            if self.contem_dado_pessoal(texto):
                print(AVISO_PESSOAL)  # não conta e não é registrado
                continue

            tentativas += 1
            ultima_pergunta = texto
            resultados = self.base.buscar(texto)

            if not resultados or resultados[0][0] < 3:
                print("\nNão encontrei uma orientação para essa dúvida.")
                print("Tente outras palavras (ex.: 'carteira de trabalho', "
                      "'CPF', 'FGTS') ou navegue pelas categorias:")
                for categoria in self.base.categorias():
                    print(f"  - {categoria}")
                continue

            pontos, melhor = resultados[0]
            if not encontrou:
                encontrou = True
                tempo_encontrar = round(time.time() - inicio, 1)
            pergunta_resposta = texto
            ultimo_id = melhor.id

            confianca = "ALTA" if pontos >= 6 else "MÉDIA"
            print(f"\nConfiança da resposta: {confianca} ({pontos} pontos)")
            melhor.exibir()

            alternativas = [(p, o) for p, o in resultados[1:3] if p >= 3]
            if alternativas:
                print("\nOutras orientações que podem ajudar:")
                for p, o in alternativas:
                    print(f"  - {o.titulo} [{o.categoria}] ({p} pontos)")

            if self.ler_sim_nao("\nEssa orientação respondeu sua dúvida? (s/n): "):
                ajudou = True
                break
        if tentativas > 0:  # só registra se a pessoa chegou a perguntar
            if tempo_encontrar is not None:
                tempo = tempo_encontrar
            else:
                tempo = round(time.time() - inicio, 1)
            pergunta = pergunta_resposta if encontrou else ultima_pergunta
            self.registrar("pergunta", pergunta, ultimo_id, encontrou, ajudou,
                           tentativas, tempo)

            # ---------- atendimento por categorias ----------

    def navegar(self):
        categorias = self.base.categorias()
        if not categorias:
            print("A base de conhecimento está vazia.")
            return
        while True:
            print("\n=== Categorias ===")
            for numero, categoria in enumerate(categorias, 1):
                print(f"{numero}. {categoria}")
            print("0. Voltar")
            opcao = self.ler_numero("Escolha uma categoria: ", 0, len(categorias))
            if opcao == 0:
                return
            self.navegar_categoria(categorias[opcao - 1])

    def navegar_categoria(self, categoria):
        orientacoes = self.base.por_categoria(categoria)
        inicio = time.time()
        while True:
            print(f"\n=== {categoria} ===")
            for numero, orientacao in enumerate(orientacoes, 1):
                print(f"{numero}. {orientacao.titulo}")
            print("0. Voltar")
            opcao = self.ler_numero("Escolha uma orientação: ", 0, len(orientacoes))
            if opcao == 0:
                return
            orientacao = orientacoes[opcao - 1]
            orientacao.exibir()
            tempo = round(time.time() - inicio, 1)
            ajudou = self.ler_sim_nao("\nEssa orientação respondeu sua dúvida? (s/n): ")
            self.registrar("categoria", "", orientacao.id, True, ajudou, 1, tempo)
            inicio = time.time()

            # ---------- indicadores ----------

    def indicadores(self):
        total = len(self.historico)
        print("\n=== Indicadores ===")
        if total == 0:
            print("Ainda não há atendimentos registrados.")
            return

        encontrados = [r for r in self.historico if r.get("encontrou")]
        ajudados = [r for r in self.historico if r.get("ajudou")]

        print(f"Atendimentos registrados: {total}")
        print(f"Resposta encontrada: {len(encontrados) / total * 100:.0f}%")
        print(f"Taxa de acerto (ajudou): {len(ajudados) / total * 100:.0f}%")

        tempos = [r.get("tempo_segundos", 0) for r in encontrados]
        if tempos:
            print(f"Tempo médio para encontrar: {sum(tempos) / len(tempos):.1f} s")
        else:
            print("Tempo médio para encontrar: sem dados")

        tentativas = [r.get("tentativas", 1) for r in self.historico]
        print(f"Tentativas por atendimento: {sum(tentativas) / total:.1f}")

        notas = {}  # uma nota por sessão de uso
        for r in self.historico:
            if r.get("nota_facilidade") is not None:
                notas[r.get("sessao")] = r["nota_facilidade"]
        if notas:
            media = sum(notas.values()) / len(notas)
            print(f"Facilidade de uso (1 a 5): {media:.1f}")
        else:
            print("Facilidade de uso (1 a 5): sem notas ainda")

        sem_solucao = []
        for r in self.historico:
            pergunta = r.get("pergunta", "")
            if not r.get("ajudou") and pergunta and pergunta not in sem_solucao:
                sem_solucao.append(pergunta)
        print("Dúvidas sem solução:")
        if sem_solucao:
            for pergunta in sem_solucao:
                print(f"  - {pergunta}")
        else:
            print("  (nenhuma)")

            # ---------- CSV e encerramento ----------

    def exportar_csv(self):
        try:
            pasta = os.path.dirname(self.caminho_csv)
            if pasta:
                os.makedirs(pasta, exist_ok=True)
            with open(self.caminho_csv, "w", newline="", encoding="utf-8") as arquivo:
                escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS_CSV)
                escritor.writeheader()
                for r in self.historico:
                    escritor.writerow({c: r.get(c, "") for c in CAMPOS_CSV})
            print(f"CSV exportado em {self.caminho_csv}")
        except OSError:
            print("Aviso: não consegui exportar o CSV.")

    def pedir_nota(self):
        """Ao sair, pede a nota de facilidade (1 a 5) e guarda na sessão."""
        desta_sessao = [r for r in self.historico if r.get("sessao") == self.sessao]
        if not desta_sessao:
            return
        nota = self.ler_numero("Dê uma nota de facilidade de uso, de 1 a 5: ", 1, 5)
        for r in desta_sessao:
            r["nota_facilidade"] = nota
        self.salvar_historico()

    def encerrar(self, pedir_nota=True):
        if pedir_nota:
            self.pedir_nota()
        self.exportar_csv()
        print("Obrigado por usar o assistente. Até logo!")
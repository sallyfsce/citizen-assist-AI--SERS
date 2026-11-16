import json
from orientacao import Orientacao

ACENTOS = {"á": "a", "à": "a", "ã": "a", "â": "a", "é": "e", "ê": "e",
           "í": "i", "ó": "o", "õ": "o", "ô": "o", "ú": "u", "ç": "c",
           "º": "o", "ª": "a"}

CAMPOS = ["id", "categoria", "titulo", "palavras_chave", "resposta",
          "documentos", "onde", "fonte", "verificado_em"]


def normalizar(texto):
    """Deixa o texto em minúsculas, sem acentos e sem pontuação."""
    texto = texto.lower().strip()
    for letra, troca in ACENTOS.items():
        texto = texto.replace(letra, troca)
    for sinal in "?!.,;:()-/\"'":
        texto = texto.replace(sinal, " ")
    return " " + " ".join(texto.split()) + " "


class BaseConhecimento:
    """O conjunto de todas as orientações."""

    def __init__(self, caminho):
        self.caminho = caminho
        self.orientacoes = []  # lista de objetos Orientacao

    def carregar(self):
        """Lê o JSON e cria os objetos Orientacao. Nunca trava o programa."""
        self.orientacoes = []
        try:
            with open(self.caminho, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            print(f"Aviso: o arquivo {self.caminho} não foi encontrado.")
            return False
        except (json.JSONDecodeError, OSError, UnicodeDecodeError):
            print(f"Aviso: o arquivo {self.caminho} está corrompido ou ilegível.")
            return False

        if not isinstance(dados, list):
            print("Aviso: a base de conhecimento deve ser uma lista de orientações.")
            return False

        ignoradas = 0
        for item in dados:
            if isinstance(item, dict) and all(campo in item for campo in CAMPOS):
                self.orientacoes.append(Orientacao(
                    item["id"], item["categoria"], item["titulo"],
                    item["palavras_chave"], item["resposta"],
                    item["documentos"], item["onde"], item["fonte"],
                    item["verificado_em"]))
            else:
                ignoradas += 1
        if ignoradas:
            print(f"Aviso: {ignoradas} registro(s) incompleto(s) foram ignorados.")
        return len(self.orientacoes) > 0

    def categorias(self):
        """Lista as categorias, sem repetir e em ordem alfabética."""
        return sorted(set(o.categoria for o in self.orientacoes))

    def por_categoria(self, categoria):
        """Devolve as orientações de uma categoria."""
        return [o for o in self.orientacoes if o.categoria == categoria]

    def pontuar(self, pergunta, orientacao):
        """Dá pontos de uma orientação para uma pergunta.  
        +3 por palavra-chave que aparece na pergunta        +1 por palavra da pergunta (4+ letras) que aparece no título."""
        pergunta_norm = normalizar(pergunta)
        pontos = 0
        for chave in orientacao.palavras_chave:
            chave_norm = normalizar(chave)
            if chave_norm.strip() and chave_norm in pergunta_norm:
                pontos += 3
        titulo_norm = normalizar(orientacao.titulo)
        for palavra in set(pergunta_norm.split()):
            if len(palavra) >= 4 and f" {palavra} " in titulo_norm:
                pontos += 1
        return pontos

    def buscar(self, pergunta):
        """Devolve lista de tuplas (pontos, orientacao), da maior para a menor."""
        resultados = []
        for orientacao in self.orientacoes:
            pontos = self.pontuar(pergunta, orientacao)
            if pontos > 0:
                resultados.append((pontos, orientacao))
        resultados.sort(key=lambda tupla: tupla[0], reverse=True)
        return resultados

from colorama import init, Fore, Style

# Inicializa a biblioteca Colorama
init(autoreset=True)

# Lista com os níveis de água do reservatório
niveis_agua = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)"},
    {"nivel": 2, "situacao": "Baixo"},
    {"nivel": 3, "situacao": "Médio"},
    {"nivel": 4, "situacao": "Alto"},
    {"nivel": 5, "situacao": "Muito alto (alerta)"}
]


# Função que define a cor conforme o nível da água
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE


# Simulação do monitoramento do reservatório
print("=== CONTROLE DE NÍVEIS DE ÁGUA ===\n")

for item in niveis_agua:
    nivel = item["nivel"]
    situacao = item["situacao"]
    cor = definir_cor(nivel)

    mensagem = f"Nível {nivel}: {situacao}"
    print(cor + mensagem + Style.RESET_ALL)

# Define o nível atual do reservatório
nivel_atual = 3

print("\n=== SITUAÇÃO ATUAL DO RESERVATÓRIO ===")

for item in niveis_agua:
    if item["nivel"] == nivel_atual:
        cor = definir_cor(nivel_atual)
        mensagem = f"Nível atual: {item['nivel']} - {item['situacao']}"
        print(cor + mensagem + Style.RESET_ALL)
        break

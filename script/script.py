import subprocess
import csv

qtTestes = int(input('Digite a quantidade de testes que serão realizados: '))

def simularServico(taxaChegadaMedia, tempoServicoMedio, numServidores, tempoObservacao):
    output = subprocess.run(
    [
        "java",
        "-cp",
        "../bin;../lib\*",
        "ServidorWeb",
        str(taxaChegadaMedia),
        str(tempoServicoMedio),
        str(numServidores),
        str(tempoObservacao)
    ], capture_output=True, text=True)
    return output

results = []
simulacoes = [
    {
        'taxaChegadaMedia': taxaChegadaMedia,
        'tempoServicoMedio': 0.84, 
        'numServidores': 10, 
        'tempoObservacao': 30
    } for taxaChegadaMedia in range(1, qtTestes+1)]

for i in range(0, len(simulacoes)):
    results.append(simularServico(
        simulacoes[i]['taxaChegadaMedia'],
        simulacoes[i]['tempoServicoMedio'],
        simulacoes[i]['numServidores'],
        simulacoes[i]['tempoObservacao']).stdout)

# Salvar resultados em um arquivo CSV
with open('resultados.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    # escrever o cabeçalho
    writer.writerow(['Taxa de chegada média', 'Tempo de serviço médio', 'Número de servidores', 'Requisições submetidas', 'Requisições concluídas', 'Tempo médio de resposta', 'Tamanho médio da fila'])
    # escrever cada linha de resultados
    for result in results:
        # remover o cabeçalho do resultado antes de escrever no arquivo CSV
        linhas_resultado = result.strip().split('\n')[1:]
        for linha in linhas_resultado:
            colunas = linha.split()
            writer.writerow(colunas)
import subprocess
import csv
import threading

qtTestes = int(input('Digite a quantidade de testes que serão realizados: '))

def simularServico(taxaChegadaMedia, tempoServicoMedio, numServidores, tempoObservacao):
    # Definir a função da simulação
    def simular():
        subprocess.run(
        [
            "java",
            "-cp",
            "../bin;../lib\*",
            "ServidorWeb",
            str(taxaChegadaMedia),
            str(tempoServicoMedio),
            str(numServidores),
            str(tempoObservacao)
        ])
    
    # Criar uma nova thread para executar a simulação
    thread = threading.Thread(target=simular)
    thread.start()
    return thread

simulacoes = [
    {
        'taxaChegadaMedia': taxaChegadaMedia,
        'tempoServicoMedio': 0.84, 
        'numServidores': 10, 
        'tempoObservacao': 30
    } for taxaChegadaMedia in range(1, qtTestes+1)]

threads = []
for i in range(0, len(simulacoes)):
    threads.append(simularServico(
        simulacoes[i]['taxaChegadaMedia'],
        simulacoes[i]['tempoServicoMedio'],
        simulacoes[i]['numServidores'],
        simulacoes[i]['tempoObservacao']))

resultados = [thread.join() for thread in threads]
print(resultados)

# # Salvar resultados em um arquivo CSV
# with open('resultados.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
#     writer = csv.writer(arquivo_csv)
#     # escrever o cabeçalho
#     writer.writerow(['Taxa de chegada média', 'Tempo de serviço médio', 'Número de servidores', 'Requisições submetidas', 'Requisições concluídas', 'Tempo médio de resposta', 'Tamanho médio da fila'])
#     # escrever resultados na tabela
#     writer.writerow(threads)
import subprocess

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
    } for taxaChegadaMedia in range(1, 11)]

for i in range(0, 1):
    results.append(simularServico(
        simulacoes[i]['taxaChegadaMedia'],
        simulacoes[i]['tempoServicoMedio'],
        simulacoes[i]['numServidores'],
        simulacoes[i]['tempoObservacao']))

def salvar_em_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)

for i in range(0, len(results)):
    nome_arquivo = "results.txt"
    conteudo = str(results)
    salvar_em_arquivo(nome_arquivo, conteudo)

# -*- coding: utf-8 -*-
"""
Atividade Agenda 11 - Desenvolvimento de Sistemas I (DSI)
Aluno: Lucas Andrade (Recuperação)

Este script simula um sistema de monitoramento para o nível de água de um reservatório.
Eu utilizei a biblioteca 'colorama' para destacar visualmente os alertas no terminal, 
facilitando a leitura e a identificação de situações críticas ou normais.
"""

import sys
# Eu importo as ferramentas necessárias da biblioteca colorama.
# O 'Fore' serve para mudar a cor da fonte do texto, e o 'Style' para resetar a formatação.
from colorama import init, Fore, Style

# Eu inicializo o colorama para garantir que ele funcione corretamente tanto no Windows
# quanto em outros sistemas operacionais.
init()


def monitorar_reservatorio(nivel: int) -> tuple[str, str]:
    """
    Esta função recebe o nível atual da água (de 1 a 5) e retorna a descrição 
    do estado e a cor correspondente do colorama para exibição no console.
    
    Eu estruturei essa lógica usando uma matriz de mapeamento bem simples para
    evitar muitos 'ifs' encadeados e deixar o código mais limpo.
    """
    # Eu criei um dicionário que mapeia o número do nível para a descrição e a cor correspondente.
    # Essa matriz segue exatamente a especificação exigida pela atividade da ETEC.
    matriz_niveis = {
        1: ("Nível 1: Muito baixo (crítico)", Fore.RED),
        2: ("Nível 2: Baixo", Fore.YELLOW),
        3: ("Nível 3: Médio", Fore.GREEN),
        4: ("Nível 4: Alto", Fore.CYAN),
        5: ("Nível 5: Muito alto (alerta)", Fore.BLUE)
    }
    
    # Eu busco o nível na matriz. Se o usuário passar um nível inválido,
    # eu retorno um status padrão e a cor cinza/padrão para evitar quebras.
    return matriz_niveis.get(nivel, ("Nível desconhecido / inválido", Style.RESET_ALL))


def executar_simulacao():
    """
    Esta função executa a simulação automática passando pelos 5 níveis obrigatórios,
    mostrando como o sistema se comporta em tempo real.
    
    Eu optei por fazer uma simulação interna sem input manual para que o script
    possa rodar e ser verificado de forma rápida e automatizada pela professora.
    """
    print("=" * 60)
    print("SISTEMA DE MONITORAMENTO DE RESERVATÓRIO DE ÁGUA - SIMULAÇÃO")
    print("=" * 60)
    
    # Eu declarei a lista com os 5 níveis obrigatórios exigidos pela ETEC para a simulação.
    niveis_para_simular = [1, 2, 3, 4, 5]
    
    for nivel in niveis_para_simular:
        descricao, cor = monitorar_reservatorio(nivel)
        
        # Eu exibo a mensagem colorida no terminal. 
        # IMPORTANTE: Eu concateno 'Style.RESET_ALL' no final para restaurar a cor padrão 
        # do terminal e garantir que os próximos textos não continuem com a cor anterior.
        print(f"Status atual: {cor}{descricao}{Style.RESET_ALL}")
        
    print("=" * 60)
    print("Simulação concluída com sucesso!")


if __name__ == "__main__":
    # Eu chamo a função que executa a simulação interna.
    executar_simulacao()

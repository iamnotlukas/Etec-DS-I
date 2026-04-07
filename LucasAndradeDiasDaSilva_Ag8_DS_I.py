# Nome do arquivo: AnaClara_Ag8_DS_I.py

print("--- Pesquisa de Satisfação: TudoWeb ---")

# Inicializando os contadores
excelente = 0
ruim = 0

# Estrutura de repetição FOR para coletar os dados
# Para testar com 10 pessoas, usamos range(1, 11)
# Para a entrega final de 50 pessoas, use range(1, 51)
for i in range(1, 11):
    print(f"\nEntrevistado nº {i}")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    print("Opinião sobre o atendimento:")
    print("1: EXCELENTE | 2: BOM | 3: RUIM")
    opiniao = int(input("Sua escolha: "))

    # Estrutura de decisão para verificar a opinião
    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1
    # Note: O valor 2 (BOM) não precisa ser contado conforme o enunciado

# Exibição dos resultados finais
print("\n" + "="*30)
print("RESULTADO DA PESQUISA")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")
print("="*30)
print("Bem vindo à Loja de Tintas do seu ZÉ")
metros_quadrados = input("Qual a área em m²?\n")
metros_quadrados = float(metros_quadrados)


qtd_de_latas = (metros_quadrados//54)
if (metros_quadrados%54 != 0):
    qtd_de_latas = qtd_de_latas +1 
valor_total = qtd_de_latas * 80 

print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}") 

Salário_Bruto= float(input("digite o valor do seu salário bruto em Reais: "))

inss = 0.08
sindicato = 0.05
ir1 = 0.075
ir2 = 0.15
ir3 = 0.225
ir4 = 0.275

if Salário_Bruto  <= 2112 :
    Salário = Salário_Bruto - (Salário_Bruto * inss) - (Salário_Bruto * sindicato)
    print(f"Seu salário está isento de imposto de renda, e seu salário final é R$ {Salário:.2f}")
    print("Os valores descontados foram:")
    print(f"INSS = R${(Salário_Bruto * inss):.2f}")
    print(f"Sindicato = R${(Salário_Bruto * sindicato):.2f}")

elif Salário_Bruto >2112 and Salário_Bruto <= 2826.65:
    Salário = Salário_Bruto - (Salário_Bruto * ir1) - (Salário_Bruto * inss) - (Salário_Bruto * sindicato)
    print(f"Seu salário será taxado no imposto de renda em 7.5%, e seu salário final é R$ {Salário:.2f}")
    print("Os valores descontados foram:")
    print(f"I.R. = {(Salário_Bruto* ir1):.2f}")
    print(f"INSS = R${(Salário_Bruto * inss):.2f}")
    print(f"Sindicato = R${(Salário_Bruto * sindicato):.2f}")
    
elif Salário_Bruto >2826.66 and Salário_Bruto <= 3751.05:
    Salário = Salário_Bruto - (Salário_Bruto * ir2) - (Salário_Bruto * inss) - (Salário_Bruto * sindicato)
    print(f"Seu salário será taxado no imposto de renda em 15%, e seu salário final é R$ {Salário:.2f}")
    print("Os valores descontados foram:")
    print(f"I.R. = {(Salário_Bruto* ir2):.2f}")
    print(f"INSS = R${(Salário_Bruto * inss):.2f}")
    print(f"Sindicato = R${(Salário_Bruto * sindicato):.2f}")

elif Salário_Bruto >3751.06 and Salário_Bruto <= 4664.68:
    Salário = Salário_Bruto - (Salário_Bruto * ir3) - (Salário_Bruto * inss) - (Salário_Bruto * sindicato)
    print(f"Seu salário será taxado no imposto de renda em 22,5, e seu salário final é R$ {Salário:.2f}")
    print("Os valores descontados foram:")
    print(f"I.R. = {(Salário_Bruto* ir3):.2f}")
    print(f"INSS = R${(Salário_Bruto * inss):.2f}")
    print(f"Sindicato = R${(Salário_Bruto * sindicato):.2f}")

elif Salário_Bruto >4664.68:
    Salário = Salário_Bruto - (Salário_Bruto * ir4) - (Salário_Bruto * inss) - (Salário_Bruto * sindicato)
    print(f"Seu salário será taxado no imposto de renda em 27,5, e seu salário final é R$ {Salário:.2f}")
    print("Os valores descontados foram:")
    print(f"I.R. = {(Salário_Bruto* ir4):.2f}")
    print(f"INSS = R${(Salário_Bruto * inss):.2f}")
    print(f"Sindicato = R${(Salário_Bruto * sindicato):.2f}")
    
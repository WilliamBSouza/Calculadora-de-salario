import tkinter as tk

def calcular_salario():
    try:
        salario_bruto = float(entry_salario_bruto.get())

        inss = 0.08
        sindicato = 0.05
        ir1 = 0.075
        ir2 = 0.15
        ir3 = 0.225
        ir4 = 0.275

        if salario_bruto <= 2112:
            salario = salario_bruto - (salario_bruto * inss) - (salario_bruto * sindicato)
            resultado_label.config(text=f"Seu salário está isento de imposto de renda. \n E seu salário final é R$ {salario:.2f}")
            descontos_label.config(text=f"INSS = R${salario_bruto * inss:.2f}\nSindicato = R${salario_bruto * sindicato:.2f}")

        elif salario_bruto > 2112 and salario_bruto <= 2826.65:
            salario = salario_bruto - (salario_bruto * ir1) - (salario_bruto * inss) - (salario_bruto * sindicato)
            resultado_label.config(text=f"Seu salário será taxado no imposto de renda em 7.5%.\n E seu salário final é R$ {salario:.2f}")
            descontos_label.config(text=f"I.R. = R${salario_bruto * ir1:.2f}\nINSS = R${salario_bruto * inss:.2f}\nSindicato = R${salario_bruto * sindicato:.2f}")

        elif salario_bruto > 2826.66 and salario_bruto <= 3751.05:
            salario = salario_bruto - (salario_bruto * ir2) - (salario_bruto * inss) - (salario_bruto * sindicato)
            resultado_label.config(text=f"Seu salário será taxado no imposto de renda em 15%. \n E seu salário final é R$ {salario:.2f}")
            descontos_label.config(text=f"I.R. = R${salario_bruto * ir2:.2f}\nINSS = R${salario_bruto * inss:.2f}\nSindicato = R${salario_bruto * sindicato:.2f}")

        elif salario_bruto > 3751.06 and salario_bruto <= 4664.68:
            salario = salario_bruto - (salario_bruto * ir3) - (salario_bruto * inss) - (salario_bruto * sindicato)
            resultado_label.config(text=f"Seu salário será taxado no imposto de renda em 22.5%. \n E seu salário final é R$ {salario:.2f}")
            descontos_label.config(text=f"I.R. = R${salario_bruto * ir3:.2f}\nINSS = R${salario_bruto * inss:.2f}\nSindicato = R${salario_bruto * sindicato:.2f}")

        elif salario_bruto > 4664.68:
            salario = salario_bruto - (salario_bruto * ir4) - (salario_bruto * inss) - (salario_bruto * sindicato)
            resultado_label.config(text=f"Seu salário será taxado no imposto de renda em 27.5%. \n E seu salário final é R$ {salario:.2f}")
            descontos_label.config(text=f"I.R. = R${salario_bruto * ir4:.2f}\nINSS = R${salario_bruto * inss:.2f}\nSindicato = R${salario_bruto * sindicato:.2f}")

    except ValueError:
        resultado_label.config(text="Por favor, insira um valor válido para o salário bruto.")

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de Salário")
root.geometry("300x200")

# Widgets
label_instrucao = tk.Label(root, text="Digite o valor do seu salário bruto em Reais:")
entry_salario_bruto = tk.Entry(root)
calcular_button = tk.Button(root, text="Calcular Salário", command=calcular_salario)
resultado_label = tk.Label(root, text="")
descontos_label = tk.Label(root, text="")

# Layout dos widgets
label_instrucao.pack()
entry_salario_bruto.pack()
calcular_button.pack()
resultado_label.pack()
descontos_label.pack()

# Loop da aplicação
root.mainloop()
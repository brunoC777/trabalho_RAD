import tkinter as tk
from tkinter import messagebox

def converter_moeda():
    try:
        valor = float(entrada_valor.get())
        moeda_origem = lista_moedas_origem.get()
        moeda_destino = lista_moedas_destino.get()
        
     
        taxa_usd_brl = 5.20
        taxa_eur_brl = 6.10
        
        if moeda_origem == "Dólar (USD)" and moeda_destino == "Real (BRL)":
            resultado = valor * taxa_usd_brl
        elif moeda_origem == "Euro (EUR)" and moeda_destino == "Real (BRL)":
            resultado = valor * taxa_eur_brl
        elif moeda_origem == "Real (BRL)" and moeda_destino == "Dólar (USD)":
            resultado = valor / taxa_usd_brl
        elif moeda_origem == "Real (BRL)" and moeda_destino == "Euro (EUR)":
            resultado = valor / taxa_eur_brl
        else:
            messagebox.showerror("Erro", "Conversão não suportada.")
            return
        
        label_resultado.config(text=f"Resultado: {resultado:.2f} {moeda_destino}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Conversor de Moedas")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Valor:").grid(row=0, column=0)
entrada_valor = tk.Entry(frame)
entrada_valor.grid(row=0, column=1)

tk.Label(frame, text="De:").grid(row=1, column=0)
lista_moedas_origem = tk.StringVar()
lista_moedas_origem.set("Dólar (USD)")
menu_moeda_origem = tk.OptionMenu(frame, lista_moedas_origem, "Dólar (USD)", "Euro (EUR)", "Real (BRL)")
menu_moeda_origem.grid(row=1, column=1)

tk.Label(frame, text="Para:").grid(row=2, column=0)
lista_moedas_destino = tk.StringVar()
lista_moedas_destino.set("Real (BRL)")
menu_moeda_destino = tk.OptionMenu(frame, lista_moedas_destino, "Dólar (USD)", "Euro (EUR)", "Real (BRL)")
menu_moeda_destino.grid(row=2, column=1)

botao_converter = tk.Button(frame, text="Converter", command=converter_moeda)
botao_converter.grid(row=3, columnspan=2, pady=10)

label_resultado = tk.Label(frame, text="")
label_resultado.grid(row=4, columnspan=2)

root.mainloop()

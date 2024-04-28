import tkinter as tk
from tkinter import messagebox

def calcular_media():
    nota1 = float(entry_nota1.get())
    nota2 = float(entry_nota2.get())
    media = (nota1 + nota2) / 2
    messagebox.showinfo("Média do Aluno", f"A média do aluno é: {media:.2f}")

# Configuração da janela principal
root = tk.Tk()
root.title("Cálculo da Média do Aluno")

# Frame para organização dos widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Labels e entradas para as notas
label_nota1 = tk.Label(frame, text="Nota 1:")
label_nota1.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_nota1 = tk.Entry(frame)
entry_nota1.grid(row=0, column=1, padx=5, pady=5)

label_nota2 = tk.Label(frame, text="Nota 2:")
label_nota2.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_nota2 = tk.Entry(frame)
entry_nota2.grid(row=1, column=1, padx=5, pady=5)

# Botão para calcular a média
btn_calcular = tk.Button(frame, text="Calcular Média", command=calcular_media)
btn_calcular.grid(row=2, columnspan=2, padx=5, pady=5)

# Loop principal da aplicação
root.mainloop()

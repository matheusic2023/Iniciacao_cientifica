"""import tkinter as tk

def calcular():
    resultado = ""
    for i in range(num_var.get()):
        resultado += str(float(entries[i].get())) + "*x" + str(i+1) + " + "
    resultado = resultado[:-3]  # remove o último " + "
    result_label.config(text="Resultado: " + resultado)

root = tk.Tk()
root.title("Interface Tkinter")

num_var = tk.IntVar()
tk.Label(root, text="Número de variáveis:").pack()
tk.Entry(root, textvariable=num_var).pack()

tk.Button(root, text="Confirmar", command=lambda: criar_entradas(num_var.get())).pack()

entries = []
def criar_entradas(n):
    for i in range(n):
        tk.Label(root, text="Constante para x" + str(i+1) + ":").pack()
        entry = tk.Entry(root)
        entry.pack()
        entries.append(entry)
    tk.Button(root, text="Calcular", command=calcular).pack()

result_label = tk.Label(root, text="Resultado:")
result_label.pack()

root.mainloop()
"""
a = 2
with open('new_test.py', 'w') as arq:
    arq.write('a = ' + str(a) + '\n')
    arq.write('print(a)\n')

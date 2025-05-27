import tkinter as tk

def verificar_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    if texto == texto[::-1]:
        resultado = "Es un palíndromo!!!"
    else:
        resultado = "No es un palíndromo"
    
    etiqueta_resultado.config(text=resultado)

venta = tk.Tk()
venta.title("Diaz Martinez Angel Joel _ Palindromos")
venta.geometry("600x500")
venta.configure(bg="#fc2dff")

etiqueta = tk.Label(venta, text="Ingresa una palabra o frase", bg="#51ffef", font=("Times New Roman Bold", 11))
etiqueta.pack(pady=1)

entrada = tk.Entry(venta)
entrada.pack(pady=10)

botoncito = tk.Button(venta, text="Verificar si es o no", command=lambda: verificar_palindromo(entrada.get()), bg="#ffd000", font=("Times New Roman Bold", 11))
botoncito.pack(pady=1)

etiqueta_resultado = tk.Label(venta, text="", bg="#51ffef", font=("Times New Roman Bold", 11))
etiqueta_resultado.pack(pady=10)

venta.mainloop()

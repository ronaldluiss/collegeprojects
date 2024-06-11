import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self):
        # Criando a janela principal
        self.window = tk.Tk()
        self.window.title("Calculadora de IMC")
        
        # Adicionando os elementos da interface
        self.create_widgets()
        
        # Iniciando o loop principal da interface
        self.window.mainloop()
        
    def create_widgets(self):
        # Rótulo e entrada para o peso
        self.label_peso = tk.Label(self.window, text="Peso (kg):")
        self.label_peso.grid(row=0, column=0, padx=10, pady=10)
        self.entry_peso = tk.Entry(self.window)
        self.entry_peso.grid(row=0, column=1, padx=10, pady=10)
        
        # Rótulo e entrada para a altura
        self.label_altura = tk.Label(self.window, text="Altura (m):")
        self.label_altura.grid(row=1, column=0, padx=10, pady=10)
        self.entry_altura = tk.Entry(self.window)
        self.entry_altura.grid(row=1, column=1, padx=10, pady=10)
        
        # Botão para calcular o IMC
        self.button_calcular = tk.Button(self.window, text="Calcular IMC", command=self.calculate_bmi)
        self.button_calcular.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        # Rótulo para exibir o resultado do IMC
        self.label_resultado = tk.Label(self.window, text="")
        self.label_resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
    def calculate_bmi(self):
        try:
            # Obtendo os valores de peso e altura
            peso = float(self.entry_peso.get())
            altura = float(self.entry_altura.get())
            
            if peso <= 0 or altura <= 0:
                raise ValueError("Peso e altura devem ser maiores que zero.")
            
            # Calculando o IMC
            imc = peso / (altura ** 2)
            self.show_bmi_category(imc)
        
        except ValueError as e:
            # Tratando valores inválidos
            messagebox.showerror("Erro de entrada", str(e))
    
    def show_bmi_category(self, imc):
        # Determinando a categoria do IMC
        if imc < 18.5:
            categoria = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            categoria = "Peso normal"
        elif 25 <= imc < 29.9:
            categoria = "Sobrepeso"
        else:
            categoria = "Obesidade"
        
        # Exibindo o resultado e a categoria
        self.label_resultado.config(text=f"Seu IMC é: {imc:.2f}\nClassificação: {categoria}")

# Executando o programa principal
if __name__ == "__main__":
    BMICalculator()

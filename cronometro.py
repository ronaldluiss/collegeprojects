import tkinter as tk

class Stopwatch:
    def __init__(self):
        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        # Criando a janela principal
        self.window = tk.Tk()
        self.window.title("Cronômetro")

        # Adicionando os elementos da interface
        self.create_widgets()

        # Iniciando o loop principal da interface
        self.window.mainloop()

    def create_widgets(self):
        # Rótulo para mostrar o tempo do cronômetro
        self.label = tk.Label(self.window, text=self.time_string(), font=("Helvetica", 48))
        self.label.pack(pady=20)

        # Botão para iniciar o cronômetro
        self.start_button = tk.Button(self.window, text="Iniciar", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)

        # Botão para parar o cronômetro
        self.stop_button = tk.Button(self.window, text="Parar", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        # Botão para resetar o cronômetro
        self.reset_button = tk.Button(self.window, text="Resetar", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def time_string(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def update_time(self):
        if self.running:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
                if self.minutes == 60:
                    self.minutes = 0
                    self.hours += 1
            self.label.config(text=self.time_string())
            self.window.after(1000, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        if not self.running:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
            self.label.config(text=self.time_string())

# Executando o programa principal
if __name__ == "__main__":
    Stopwatch()

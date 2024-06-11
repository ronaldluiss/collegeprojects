import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self):
        # Criando a janela principal
        self.window = tk.Tk()
        self.window.title("Lista de Tarefas")
        
        # Lista de tarefas
        self.tasks = []
        
        # Adicionando os elementos da interface
        self.create_widgets()
        
        # Iniciando o loop principal da interface
        self.window.mainloop()
    
    def create_widgets(self):
        # Rótulo para solicitar a tarefa
        self.label = tk.Label(self.window, text="Digite uma tarefa:")
        self.label.grid(row=0, column=0, padx=10, pady=10)
        
        # Entrada para o usuário digitar a tarefa
        self.entry_task = tk.Entry(self.window, width=40)
        self.entry_task.grid(row=0, column=1, padx=10, pady=10)
        
        # Botão para adicionar a tarefa à lista
        self.button_add = tk.Button(self.window, text="Adicionar Tarefa", command=self.add_task)
        self.button_add.grid(row=0, column=2, padx=10, pady=10)
        
        # Listbox para exibir as tarefas
        self.listbox_tasks = tk.Listbox(self.window, height=10, width=50)
        self.listbox_tasks.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        # Botão para remover a tarefa selecionada
        self.button_remove = tk.Button(self.window, text="Remover Tarefa", command=self.remove_task)
        self.button_remove.grid(row=1, column=2, padx=10, pady=10)
    
    def add_task(self):
        # Obtendo a tarefa da entrada
        task = self.entry_task.get()
        
        if task != "":
            # Adicionando a tarefa à lista
            self.tasks.append(task)
            # Atualizando a exibição da lista
            self.update_tasks_listbox()
            # Limpando a entrada
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Você deve digitar uma tarefa.")
    
    def remove_task(self):
        try:
            # Obtendo a tarefa selecionada
            selected_task_index = self.listbox_tasks.curselection()[0]
            # Removendo a tarefa da lista
            self.tasks.pop(selected_task_index)
            # Atualizando a exibição da lista
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Aviso", "Você deve selecionar uma tarefa.")
    
    def update_tasks_listbox(self):
        # Limpando a Listbox
        self.listbox_tasks.delete(0, tk.END)
        
        # Adicionando todas as tarefas na Listbox
        for task in self.tasks:
            self.listbox_tasks.insert(tk.END, task)

# Executando o programa principal
if __name__ == "__main__":
    ToDoListApp()

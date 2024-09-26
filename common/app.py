import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestão Escolar")
        self.root.geometry("800x600")
        self.tabs = ttk.Notebook(root)

        # Abas: Gerenciamento de Salas, Alunos, Trabalhos e Relatório
        self.tab_salas = ttk.Frame(self.tabs)
        self.tab_alunos = ttk.Frame(self.tabs)
        self.tab_trabalhos = ttk.Frame(self.tabs)
        self.tab_relatorio = ttk.Frame(self.tabs)

        self.tabs.add(self.tab_salas, text="Salas")
        self.tabs.add(self.tab_alunos, text="Alunos")
        self.tabs.add(self.tab_trabalhos, text="Trabalhos")
        self.tabs.add(self.tab_relatorio, text="Relatório por Bimestre")
        self.tabs.pack(expand=1, fill="both")

        # Dados em memória para armazenar salas, alunos e trabalhos
        self.salas = []
        self.alunos = []
        self.trabalhos = []

        # Criar Salas
        self.create_salas_ui()
        # Criar Alunos
        self.create_alunos_ui()
        # Criar Trabalhos
        self.create_trabalhos_ui()
        # Criar Relatório
        self.create_relatorio_ui()

    def create_salas_ui(self):
        label = tk.Label(self.tab_salas, text="Nome da Sala:")
        label.grid(row=0, column=0, padx=10, pady=10)

        self.sala_name = tk.Entry(self.tab_salas)
        self.sala_name.grid(row=0, column=1, padx=10, pady=10)

        add_sala_button = tk.Button(self.tab_salas, text="Adicionar Sala", command=self.add_sala)
        add_sala_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.salas_listbox = tk.Listbox(self.tab_salas)
        self.salas_listbox.grid(row=2, column=0, columnspan=2, pady=10)

        remove_sala_button = tk.Button(self.tab_salas, text="Remover Sala", command=self.remove_sala)
        remove_sala_button.grid(row=3, column=0, columnspan=2, pady=10)

    def add_sala(self):
        sala_name = self.sala_name.get()
        if sala_name:
            self.salas.append(sala_name)
            self.salas_listbox.insert(tk.END, sala_name)
            self.sala_name.delete(0, tk.END)
            self.update_comboboxes()
        else:
            messagebox.showerror("Erro", "Por favor, insira o nome da sala.")

    def remove_sala(self):
        try:
            selected_index = self.salas_listbox.curselection()[0]
            del self.salas[selected_index]
            self.salas_listbox.delete(selected_index)
            self.update_comboboxes()
        except IndexError:
            messagebox.showerror("Erro", "Selecione uma sala para remover.")

    def create_alunos_ui(self):
        label = tk.Label(self.tab_alunos, text="Nome do Aluno:")
        label.grid(row=0, column=0, padx=10, pady=10)

        self.aluno_name = tk.Entry(self.tab_alunos)
        self.aluno_name.grid(row=0, column=1, padx=10, pady=10)

        label_aniversario = tk.Label(self.tab_alunos, text="Aniversário:")
        label_aniversario.grid(row=1, column=0, padx=10, pady=10)

        self.aluno_birthday = tk.Entry(self.tab_alunos)
        self.aluno_birthday.grid(row=1, column=1, padx=10, pady=10)

        label_sala = tk.Label(self.tab_alunos, text="Sala:")
        label_sala.grid(row=2, column=0, padx=10, pady=10)

        self.aluno_sala = ttk.Combobox(self.tab_alunos, values=self.salas)
        self.aluno_sala.grid(row=2, column=1, padx=10, pady=10)

        add_aluno_button = tk.Button(self.tab_alunos, text="Adicionar Aluno", command=self.add_aluno)
        add_aluno_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.alunos_listbox = tk.Listbox(self.tab_alunos)
        self.alunos_listbox.grid(row=4, column=0, columnspan=2, pady=10)

        remove_aluno_button = tk.Button(self.tab_alunos, text="Remover Aluno", command=self.remove_aluno)
        remove_aluno_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_aluno(self):
        nome = self.aluno_name.get()
        aniversario = self.aluno_birthday.get()
        sala = self.aluno_sala.get()

        if nome and aniversario and sala:
            aluno = {'nome': nome, 'aniversario': aniversario, 'sala': sala, 'notas': {'participação': 0, 'prova': 0, 'trabalhos': 0}}
            self.alunos.append(aluno)
            self.alunos_listbox.insert(tk.END, f"{nome} ({sala})")
            self.aluno_name.delete(0, tk.END)
            self.aluno_birthday.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Por favor, preencha todas as informações.")

    def remove_aluno(self):
        try:
            selected_index = self.alunos_listbox.curselection()[0]
            del self.alunos[selected_index]
            self.alunos_listbox.delete(selected_index)
        except IndexError:
            messagebox.showerror("Erro", "Selecione um aluno para remover.")

    def create_trabalhos_ui(self):
        label = tk.Label(self.tab_trabalhos, text="Nome do Trabalho:")
        label.grid(row=0, column=0, padx=10, pady=10)

        self.trabalho_name = tk.Entry(self.tab_trabalhos)
        self.trabalho_name.grid(row=0, column=1, padx=10, pady=10)

        label_pontos = tk.Label(self.tab_trabalhos, text="Pontos por fazer:")
        label_pontos.grid(row=1, column=0, padx=10, pady=10)

        self.trabalho_pontos = tk.Entry(self.tab_trabalhos)
        self.trabalho_pontos.grid(row=1, column=1, padx=10, pady=10)

        label_bimestre = tk.Label(self.tab_trabalhos, text="Bimestre:")
        label_bimestre.grid(row=2, column=0, padx=10, pady=10)

        self.trabalho_bimestre = ttk.Combobox(self.tab_trabalhos, values=["1º Bimestre", "2º Bimestre", "3º Bimestre", "4º Bimestre"])
        self.trabalho_bimestre.grid(row=2, column=1, padx=10, pady=10)

        label_salas = tk.Label(self.tab_trabalhos, text="Salas que fizeram:")
        label_salas.grid(row=3, column=0, padx=10, pady=10)

        self.trabalho_salas = ttk.Combobox(self.tab_trabalhos, values=self.salas)
        self.trabalho_salas.grid(row=3, column=1, padx=10, pady=10)

        add_trabalho_button = tk.Button(self.tab_trabalhos, text="Adicionar Trabalho", command=self.add_trabalho)
        add_trabalho_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.trabalhos_listbox = tk.Listbox(self.tab_trabalhos)
        self.trabalhos_listbox.grid(row=5, column=0, columnspan=2, pady=10)

        remove_trabalho_button = tk.Button(self.tab_trabalhos, text="Remover Trabalho", command=self.remove_trabalho)
        remove_trabalho_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.alunos_trabalho_button = tk.Button(self.tab_trabalhos, text="Adicionar Alunos ao Trabalho", command=self.adicionar_alunos_trabalho)
        self.alunos_trabalho_button.grid(row=7, column=0, columnspan=2, pady=10)

    def add_trabalho(self):
        nome = self.trabalho_name.get()
        pontos = self.trabalho_pontos.get()
        bimestre = self.trabalho_bimestre.get()
        sala = self.trabalho_salas.get()

        if nome and pontos and bimestre and sala:
            trabalho = {'nome': nome, 'pontos': int(pontos), 'bimestre': bimestre, 'sala': sala, 'alunos_fizeram': []}
            self.trabalhos.append(trabalho)
            self.trabalhos_listbox.insert(tk.END, f"{nome} - {sala} ({bimestre})")
            self.trabalho_name.delete(0, tk.END)
            self.trabalho_pontos.delete(0, tk.END)
            self.trabalho_bimestre.set('')  # Limpar o Combobox de bimestre
            self.trabalho_salas.set('')      # Limpar o Combobox de sala
        else:
            messagebox.showerror("Erro", "Preencha todas as informações corretamente.")

    def remove_trabalho(self):
        try:
            selected_index = self.trabalhos_listbox.curselection()[0]
            del self.trabalhos[selected_index]
            self.trabalhos_listbox.delete(selected_index)
        except IndexError:
            messagebox.showerror("Erro", "Selecione um trabalho para remover.")

    def adicionar_alunos_trabalho(self):
        try:
            selected_index = self.trabalhos_listbox.curselection()[0]
        except IndexError:
            messagebox.showerror("Erro", "Selecione um trabalho!")
            return

        trabalho = self.trabalhos[selected_index]

        self.alunos_trabalho_window = tk.Toplevel(self.root)
        self.alunos_trabalho_window.title("Adicionar Alunos ao Trabalho")

        self.alunos_trabalho_listbox = tk.Listbox(self.alunos_trabalho_window)
        self.alunos_trabalho_listbox.grid(row=0, column=0, columnspan=2)

        for aluno in self.alunos:
            self.alunos_trabalho_listbox.insert(tk.END, aluno['nome'])

        tk.Label(self.alunos_trabalho_window, text="Nota Recebida:").grid(row=1, column=0)
        self.nota_trabalho_entry = tk.Entry(self.alunos_trabalho_window)
        self.nota_trabalho_entry.grid(row=1, column=1)

        tk.Button(self.alunos_trabalho_window, text="Adicionar ao Trabalho", command=lambda: self.adicionar_aluno_fez_trabalho(trabalho)).grid(row=2, column=0, columnspan=2)

    def adicionar_aluno_fez_trabalho(self, trabalho):
        try:
            selected_index = self.alunos_trabalho_listbox.curselection()[0]
        except IndexError:
            messagebox.showerror("Erro", "Selecione um aluno!")
            return

        aluno = self.alunos[selected_index]
        nota = self.nota_trabalho_entry.get()

        if nota and float(nota) <= trabalho['pontos']:
            trabalho['alunos_fizeram'].append({'nome': aluno['nome'], 'nota': float(nota)})
            messagebox.showinfo("Sucesso", f"{aluno['nome']} adicionado ao trabalho {trabalho['nome']} com nota {nota}.")
            self.nota_trabalho_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Insira uma nota válida que não exceda os pontos do trabalho.")

    def create_relatorio_ui(self):
        label = tk.Label(self.tab_relatorio, text="Selecione o Bimestre:")
        label.grid(row=0, column=0, padx=10, pady=10)

        self.bimestre_select = ttk.Combobox(self.tab_relatorio, values=["1º Bimestre", "2º Bimestre", "3º Bimestre", "4º Bimestre"])
        self.bimestre_select.grid(row=0, column=1, padx=10, pady=10)

        gerar_relatorio_button = tk.Button(self.tab_relatorio, text="Gerar Relatório", command=self.gerar_relatorio_bimestre)
        gerar_relatorio_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.relatorio_text = tk.Text(self.tab_relatorio, height=20, width=60)
        self.relatorio_text.grid(row=2, column=0, columnspan=2, pady=10)

    def gerar_relatorio_bimestre(self):
        bimestre = self.bimestre_select.get()
        if not bimestre:
            messagebox.showerror("Erro", "Selecione um bimestre.")
            return

        relatorio = f"Relatório de Notas - {bimestre}:\n\n"
        for trabalho in self.trabalhos:
            if trabalho['bimestre'] == bimestre:
                relatorio += f"Trabalho: {trabalho['nome']} - Sala: {trabalho['sala']} - Pontos: {trabalho['pontos']}\n"
                if trabalho['alunos_fizeram']:
                    for aluno in trabalho['alunos_fizeram']:
                        relatorio += f"  Aluno: {aluno['nome']} - Nota: {aluno['nota']}\n"
                else:
                    relatorio += "  Nenhum aluno registrado.\n"
                relatorio += "\n"

        if relatorio.strip() == f"Relatório de Notas - {bimestre}:\n\n":
            relatorio += "Nenhum trabalho registrado para este bimestre."

        self.relatorio_text.delete(1.0, tk.END)  # Limpar texto anterior
        self.relatorio_text.insert(tk.END, relatorio)

    def update_comboboxes(self):
        """Atualiza os comboboxes de salas em Alunos e Trabalhos."""
        self.aluno_sala['values'] = self.salas
        self.trabalho_salas['values'] = self.salas

# Iniciar a aplicação
root = tk.Tk()
app = App(root)
root.mainloop()
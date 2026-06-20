from abc import ABC, abstractmethod
import tkinter as tk

class ProposalApp(ABC):
    def __init__(self, title="Proposal App"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("400x300")
        self.root.configure(bg='#FFE4E1')

    @abstractmethod
    def create_widgets(self):
        pass

    @abstractmethod
    def yes_clicked(self):
        pass

    @abstractmethod
    def no_clicked(self):
        pass

    def run(self):
        self.root.mainloop()

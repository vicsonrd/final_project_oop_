import tkinter as tk
from tkinter import messagebox
import sys
import subprocess
import os
from abc import ABC, abstractmethod

# Abstraction: Base class for proposals
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


# Inheritance: ValentineProposal inherits from ProposalApp
class ValentineProposal(ProposalApp):
    def __init__(self):
        super().__init__("Valentine's Proposal")
        self.__yes_size = 14   # Encapsulation: private attribute
        self.create_widgets()

    # Getter/Setter for encapsulation
    def get_yes_size(self):
        return self.__yes_size

    def set_yes_size(self, size):
        if size > 0:
            self.__yes_size = size

    def create_widgets(self):
        title = tk.Label(
            self.root,
            text="Will you be my Valentine?",
            font=('Comic Sans MS', 20, 'bold'),
            bg='#FFE4E1',
            fg='#FF69B4'
        )
        title.pack(pady=30)

        button_frame = tk.Frame(self.root, bg='#FFE4E1')
        button_frame.pack(expand=True)

        self.yes_button = tk.Button(
            button_frame,
            text="YES",
            font=('Comic Sans MS', self.__yes_size, 'bold'),
            command=self.yes_clicked,
            bg='#98FB98',
            fg='white',
            relief=tk.RAISED,
            borderwidth=3
        )
        self.yes_button.pack(side=tk.LEFT, padx=10)

        self.no_button = tk.Button(
            button_frame,
            text="NO",
            font=('Comic Sans MS', 14, 'bold'),
            command=self.no_clicked,
            bg='#FF6B6B',
            fg='white',
            relief=tk.RAISED,
            borderwidth=3
        )
        self.no_button.pack(side=tk.LEFT, padx=10)

    def yes_clicked(self):
        messagebox.showinfo(
            "Thank you, baby ❤️",
            "You have made me the happiest man!\n\nNow a surprise for you 🌻"
        )
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            ale_path = os.path.join(script_dir, "sunflower.py")
            subprocess.Popen([sys.executable, ale_path])
        except Exception as e:
            messagebox.showerror("Error", f"Could not execute sunflower.py: {str(e)}")

        self.root.quit()
        sys.exit()

    def no_clicked(self):
        # Polymorphism: different behavior when NO is clicked
        self.set_yes_size(int(self.get_yes_size() * 1.5))
        self.yes_button.configure(font=('Comic Sans MS', self.get_yes_size(), 'bold'))


if __name__ == "__main__":
    app = ValentineProposal()
    app.run()

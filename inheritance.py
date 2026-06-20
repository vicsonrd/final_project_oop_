import tkinter as tk
from tkinter import messagebox
import sys, subprocess, os
from abstraction import ProposalApp
from encapsulation import YesButtonSize

class ValentineProposal(ProposalApp):
    def __init__(self):
        super().__init__("Valentine's Proposal")
        self.size_manager = YesButtonSize()
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(
            self.root,
            text="Will you be my Forever Valentine?",
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
            font=('Comic Sans MS', self.size_manager.get_size(), 'bold'),
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
            bg='#FF6B6B',
            fg='white',
            relief=tk.RAISED,
            borderwidth=3,
            command=self.no_clicked
        )
        self.no_button.pack(side=tk.LEFT, padx=10)

    def yes_clicked(self):
        messagebox.showinfo("Thank you ❤️", "You have made me the happiest person!")
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            sunflower_path = os.path.join(script_dir, "sunflower.py")
            subprocess.Popen([sys.executable, sunflower_path])
        except Exception as e:
            messagebox.showerror("Error", f"Could not execute sunflower.py: {str(e)}")

        self.root.quit()
        sys.exit()

    def no_clicked(self):
        pass  # overridden by polymorphism

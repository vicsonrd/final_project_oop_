from encapsulation import YesButtonSize

class PolymorphismDemo:
    def __init__(self, yes_button, size_manager: YesButtonSize):
        self.yes_button = yes_button
        self.size_manager = size_manager

    def no_clicked(self):
        # Polymorphism: different behavior when NO is clicked
        self.size_manager.set_size(int(self.size_manager.get_size() * 1.5))
        self.yes_button.configure(font=('Comic Sans MS', self.size_manager.get_size(), 'bold'))

from inheritance import ValentineProposal
from polymorphism import PolymorphismDemo

if __name__ == "__main__":
    # Create the Valentine GUI app
    app = ValentineProposal()

    # Attach polymorphism behavior to NO button
    poly = PolymorphismDemo(app.yes_button, app.size_manager)
    app.no_button.configure(command=poly.no_clicked)

    # Run the GUI loop
    app.run()

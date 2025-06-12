class Expense:
    def __init__ (self, name, type, amount) -> None:
        self.name = name
        self.type = type
        self.amount = amount

    def __str__(self):
        return f"Expense(name={self.name}, type={self.type}, amount={self.amount})"
    def __repr__(self):
        return f"Expenser(name={self.name}, type={self.type}, amount={self.amount})"
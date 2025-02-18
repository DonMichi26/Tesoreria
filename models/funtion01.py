import datetime

# Clase para generar un reporte bancario
class BankReport:
    def __init__(self, bank_name, account_number, starting_balance):
        # Inicializa el reporte bancario con el nombre del banco, número de cuenta y saldo inicial
        self.bank_name = bank_name
        self.account_number = account_number
        self.starting_balance = starting_balance
        self.transactions = []  # Lista para almacenar las transacciones

    def add_transaction(self, date, description, amount):
        # Añade una transacción a la lista de transacciones
        self.transactions.append({
            'date': date,  # Fecha de la transacción
            'description': description,  # Descripción de la transacción
            'amount': amount  # Monto de la transacción
        })

    def generate_report(self):
        # Genera un reporte bancario en formato de texto
        report = f"Bank Report for {self.bank_name}\n"
        report += f"Account Number: {self.account_number}\n"
        report += f"Starting Balance: {self.starting_balance}\n"
        report += "Transactions:\n"
        report += "Date\t\tDescription\t\tAmount\n"
        report += "-"*50 + "\n"
        
        # Añade cada transacción al reporte
        for transaction in self.transactions:
            report += f"{transaction['date']}\t{transaction['description']}\t{transaction['amount']}\n"
        
        # Calcula el saldo final sumando el saldo inicial y los montos de las transacciones
        ending_balance = self.starting_balance + sum(t['amount'] for t in self.transactions)
        report += "-"*50 + "\n"
        report += f"Ending Balance: {ending_balance}\n"
        
        return report  # Devuelve el reporte generado

# Ejemplo de uso
if __name__ == "__main__":
    # Crea un nuevo reporte bancario
    report = BankReport("Bank of Python", "123456789", 1000.00)
    # Añade algunas transacciones
    report.add_transaction(datetime.date(2023, 10, 1), "Deposit", 500.00)
    report.add_transaction(datetime.date(2023, 10, 2), "Withdrawal", -200.00)
    # Genera y muestra el reporte
    print(report.generate_report())
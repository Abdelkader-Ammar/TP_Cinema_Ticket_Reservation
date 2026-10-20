class PaymentRepository:
    def __init__(self):
        self.payments = {}

    def save(self, payment_id, amount, status):
        self.payments[payment_id] = {"payment_id": payment_id, "amount": amount, "status": status}

    def get(self, payment_id):
        return self.payments.get(payment_id)

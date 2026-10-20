class PaymentService:
    def __init__(self, repository):
        self.repository = repository

    def process_payment(self, payment_id, amount):
        self.repository.save(payment_id, amount, "completed")
        return self.repository.get(payment_id)

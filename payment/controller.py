class PaymentController:
    def __init__(self, service):
        self.service = service

    def handle_payment(self, payment_id, amount):
        return self.service.process_payment(payment_id, amount)

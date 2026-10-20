import unittest
from payment.controller import PaymentController
from payment.service import PaymentService
from payment.data_access import PaymentRepository


class TestPayment(unittest.TestCase):
    def test_process_payment(self):
        repository = PaymentRepository()
        service = PaymentService(repository)
        controller = PaymentController(service)

        result = controller.handle_payment("pay_1", 100)

        self.assertEqual(result["payment_id"], "pay_1")
        self.assertEqual(result["amount"], 100)
        self.assertEqual(result["status"], "completed")


if __name__ == "__main__":
    unittest.main()

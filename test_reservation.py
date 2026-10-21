import unittest
from reservation.controller import ReservationController
from reservation.service import ReservationService
from reservation.data_access import ReservationRepository


class TestReservationUnit(unittest.TestCase):
    def setUp(self):
        self.repository = ReservationRepository()
        self.service = ReservationService(self.repository)
        self.controller = ReservationController(self.service)

    def test_create_reservation_success(self):
        result = self.controller.handle_create_reservation(1, 101, 5)
        self.assertEqual(result["status"], "pending")
        self.assertEqual(result["client_id"], 1)
        self.assertEqual(result["seance_id"], 101)
        self.assertEqual(result["place_number"], 5)

    def test_create_reservation_place_taken(self):
        self.controller.handle_create_reservation(1, 101, 5)
        result = self.controller.handle_create_reservation(2, 101, 5)
        self.assertEqual(result, {"error": "place_deja_prise"})

    def test_confirm_reservation_success(self):
        created = self.controller.handle_create_reservation(1, 101, 5)
        result = self.controller.handle_confirm_reservation(created["reservation_id"])
        self.assertEqual(result["status"], "confirmed")

    def test_confirm_reservation_not_found(self):
        result = self.controller.handle_confirm_reservation(999)
        self.assertEqual(result, {"error": "reservation_introuvable"})

    def test_confirm_reservation_already_confirmed(self):
        created = self.controller.handle_create_reservation(1, 101, 5)
        self.controller.handle_confirm_reservation(created["reservation_id"])
        result = self.controller.handle_confirm_reservation(created["reservation_id"])
        self.assertEqual(result, {"error": "reservation_deja_traitee"})

    def test_cancel_reservation_success(self):
        created = self.controller.handle_create_reservation(1, 101, 5)
        result = self.controller.handle_cancel_reservation(created["reservation_id"])
        self.assertEqual(result["status"], "cancelled")

    def test_cancel_reservation_already_cancelled(self):
        created = self.controller.handle_create_reservation(1, 101, 5)
        self.controller.handle_cancel_reservation(created["reservation_id"])
        result = self.controller.handle_cancel_reservation(created["reservation_id"])
        self.assertEqual(result, {"error": "reservation_deja_annulee"})

    def test_get_my_reservations(self):
        self.controller.handle_create_reservation(1, 101, 5)
        self.controller.handle_create_reservation(1, 102, 8)
        self.controller.handle_create_reservation(2, 101, 3)
        mine = self.controller.handle_get_my_reservations(1)
        self.assertEqual(len(mine), 2)
        for r in mine:
            self.assertEqual(r["client_id"], 1)


class TestReservationIntegration(unittest.TestCase):
    def test_nominal_flow_reserve_and_confirm(self):
        repository = ReservationRepository()
        service = ReservationService(repository)
        controller = ReservationController(service)

        created = controller.handle_create_reservation(42, 201, 12)
        self.assertEqual(created["status"], "pending")

        confirmed = controller.handle_confirm_reservation(created["reservation_id"])
        self.assertEqual(confirmed["status"], "confirmed")

        stored = repository.get(created["reservation_id"])
        self.assertIsNotNone(stored)
        self.assertEqual(stored["status"], "confirmed")
        self.assertEqual(stored["client_id"], 42)
        self.assertEqual(stored["seance_id"], 201)
        self.assertEqual(stored["place_number"], 12)

    def test_nominal_flow_reserve_then_cancel(self):
        repository = ReservationRepository()
        service = ReservationService(repository)
        controller = ReservationController(service)

        created = controller.handle_create_reservation(7, 301, 1)
        self.assertEqual(created["status"], "pending")

        cancelled = controller.handle_cancel_reservation(created["reservation_id"])
        self.assertEqual(cancelled["status"], "cancelled")

        stored = repository.get(created["reservation_id"])
        self.assertEqual(stored["status"], "cancelled")


if __name__ == "__main__":
    unittest.main()

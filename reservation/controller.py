class ReservationController:
    def __init__(self, service):
        self.service = service

    def handle_create_reservation(self, client_id, seance_id, place_number):
        return self.service.create_reservation(client_id, seance_id, place_number)

    def handle_confirm_reservation(self, reservation_id):
        return self.service.confirm_reservation(reservation_id)

    def handle_cancel_reservation(self, reservation_id):
        return self.service.cancel_reservation(reservation_id)

    def handle_get_my_reservations(self, client_id):
        return self.service.get_reservations_by_client(client_id)

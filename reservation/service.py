class ReservationService:
    def __init__(self, repository):
        self.repository = repository

    def create_reservation(self, client_id, seance_id, place_number):
        if self.repository.place_is_taken(seance_id, place_number):
            return {"error": "place_deja_prise"}
        reservation = self.repository.save(
            client_id, seance_id, place_number, "pending"
        )
        return reservation

    def confirm_reservation(self, reservation_id):
        reservation = self.repository.get(reservation_id)
        if not reservation:
            return {"error": "reservation_introuvable"}
        if reservation["status"] != "pending":
            return {"error": "reservation_deja_traitee"}
        return self.repository.update_status(reservation_id, "confirmed")

    def cancel_reservation(self, reservation_id):
        reservation = self.repository.get(reservation_id)
        if not reservation:
            return {"error": "reservation_introuvable"}
        if reservation["status"] == "cancelled":
            return {"error": "reservation_deja_annulee"}
        return self.repository.update_status(reservation_id, "cancelled")

    def get_reservations_by_client(self, client_id):
        return self.repository.get_by_client(client_id)

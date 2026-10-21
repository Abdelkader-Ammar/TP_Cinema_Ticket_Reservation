class ReservationRepository:
    def __init__(self):
        self.reservations = {}
        self.next_id = 1

    def save(self, client_id, seance_id, place_number, status):
        reservation_id = self.next_id
        self.next_id += 1
        self.reservations[reservation_id] = {
            "reservation_id": reservation_id,
            "client_id": client_id,
            "seance_id": seance_id,
            "place_number": place_number,
            "status": status,
        }
        return self.reservations[reservation_id]

    def get(self, reservation_id):
        return self.reservations.get(reservation_id)

    def get_by_client(self, client_id):
        return [
            r for r in self.reservations.values()
            if r["client_id"] == client_id
        ]

    def update_status(self, reservation_id, status):
        if reservation_id in self.reservations:
            self.reservations[reservation_id]["status"] = status
            return self.reservations[reservation_id]
        return None

    def delete(self, reservation_id):
        if reservation_id in self.reservations:
            del self.reservations[reservation_id]
            return True
        return False

    def place_is_taken(self, seance_id, place_number):
        for r in self.reservations.values():
            if (
                r["seance_id"] == seance_id
                and r["place_number"] == place_number
                and r["status"] in ("confirmed", "pending")
            ):
                return True
        return False

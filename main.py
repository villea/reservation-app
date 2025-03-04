
class ReservationApp:

    def __init__(self):
        self.reservations = [None] * 24

    def add_reservation(self, name,start_hour,length_hours):

        if self.reservations[start_hour] is not None:
            print(f"Reservation at {start_hour} is already taken")
            return False
        for i in range(start_hour, start_hour + length_hours):
            self.reservations[i] = name
        return True

    def find_free_spot(self, length_hours):
        start_hour = None
        if length_hours > 24:
            return start_hour
        for i in range(24-length_hours):
            if self.reservations[i] is None:
                is_free = True
                for j in range(length_hours):
                    if self.reservations[i + j] is not None :
                        is_free = False
                        break
                if is_free:
                    start_hour = i
                    break
                    
        return start_hour

    def check_reservation(self, time):
        return self.reservations[time]

if __name__ == "__main__":
    app = ReservationApp()
    print(app.add_reservation("John", 10, 2))
    print(app.check_reservation(10))
    print(app.check_reservation(11))
    print(app.check_reservation(12))
    print(app.add_reservation("John", 10, 2))
    print(app.find_free_spot(4))


        

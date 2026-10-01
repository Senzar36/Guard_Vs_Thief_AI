import solara

class InvalidLocationError(Exception):
    def __init__(self, message):
        super().__init__(message)

def app():
    thief = []
    for i in range(time):
        thief.append(int(input(f"Enter thief location at time {i}: ")))
        if thief[i] < 0 or thief[i] > 9:
            raise InvalidLocationError(f"Invalid location {thief[i]} at time {i}. Location must be between 0 and 9.")
        else:
            continue
        
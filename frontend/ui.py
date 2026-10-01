import solara
from main import time

number = solara.reactive(0)

result = solara.reactive("")

@solara.component
def App():
    def on_change(value):
        number.set(value)
        result.set(f"Number is: {value}")

    return solara.VBox(
        solara.Slider(min=0, max=10, value=number.get(), on_change=on_change),
        solara.Label(result.get()),
    )

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

class Input_Values:
    def location_guard(self, x, y):
        if x < 0 or x > 9 or y < 0 or y > 9:
            raise InvalidLocationError(f"Invalid guard location ({x}, {y}). Location must be between 0 and 9.")
        else:
            self.thief[0].append(x)
            self.thief[1].append(y)
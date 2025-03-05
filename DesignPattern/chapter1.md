# Iterator Pattern

The Iterator Design Pattern is a behavioral design pattern that allows sequential access to elements in a collection (like a list or a set) without exposing the underlying structure. It provides a way to iterate over the elements of an object without knowing how the collection is stored or structured.



# Observer Pattern

The Observer Design Pattern is a behavioral design pattern that defines a one-to-many relationship between objects. When the state of one object (called the subject) changes, all its dependent objects (called observers) are notified and updated automatically. This pattern is particularly useful for implementing distributed event-handling systems, where one object (the subject) maintains a list of observers and notifies them of any state changes, usually by calling one of their methods.

### Common Use Cases:

**Event handling systems** (e.g., GUI frameworks, user interaction events).
**Model-View-Controller** (MVC) design, where the View (observer) reacts to changes in the Model (subject).
**Real-time data systems**, like stock market apps where multiple clients need to be updated when a stock price changes.

```
# Subject Class
class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = None

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify_observers()

# Observer Class
class DisplayDevice:
    def update(self, temperature):
        pass

# Concrete Observer Classes
class PhoneDisplay(DisplayDevice):
    def update(self, temperature):
        print(f"Phone Display: The temperature is {temperature}°C")

class ComputerDisplay(DisplayDevice):
    def update(self, temperature):
        print(f"Computer Display: The temperature is {temperature}°C")

# Usage
weather_station = WeatherStation()

phone_display = PhoneDisplay()
computer_display = ComputerDisplay()

# Register observers
weather_station.register_observer(phone_display)
weather_station.register_observer(computer_display)

# Simulate temperature changes
weather_station.set_temperature(25)  # Both displays will be updated
weather_station.set_temperature(30)  # Both displays will be updated
```

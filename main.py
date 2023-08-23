class Flight:
    def __init__(self, flight_id, from_city, to_city, price):
        self.flight_id = flight_id
        self.from_city = from_city
        self.to_city = to_city
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_city(self, city):
        result = []
        for flight in self.flights:
            if flight.from_city == city or flight.to_city == city:
                result.append(flight)
        return result

    def search_from_city(self, city):
        result = []
        for flight in self.flights:
            if flight.from_city == city:
                result.append(flight)
        return result

    def search_between_cities(self, city1, city2):
        result = []
        for flight in self.flights:
            if (flight.from_city == city1 and flight.to_city == city2) or (flight.from_city == city2 and flight.to_city == city1):
                result.append(flight)
        return result

def main():
    flight_table = FlightTable()

    flight_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]

    for data in flight_data:
        flight = Flight(data[0], data[1], data[2], data[3])
        flight_table.add_flight(flight)

    cities = {
        "BLR": "Bengaluru",
        "BOM": "Mumbai",
        "BBI": "Bhubaneswar",
        "HYD": "Hyderabad",
        "JLR": "Jabalpur"
    }

    print("Options:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        city = input("Enter the city code: ")
        flights = flight_table.search_by_city(city)
    elif choice == 2:
        city = input("Enter the city code: ")
        flights = flight_table.search_from_city(city)
    elif choice == 3:
        city1 = input("Enter the first city code: ")
        city2 = input("Enter the second city code: ")
        flights = flight_table.search_between_cities(city1, city2)

    if flights:
        print("Flight ID\tFrom\tTo\tPrice")
        for flight in flights:
            print(f"{flight.flight_id}\t{cities[flight.from_city]}\t{cities[flight.to_city]}\t{flight.price}")
    else:
        print("No flights found.")

if __name__ == "__main__":
    main()

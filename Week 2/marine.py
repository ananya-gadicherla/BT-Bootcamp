
class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def __str__(self):
        return f"Customer[id={self.customer_id}, name={self.name}]"


class Booking:
    def __init__(self, customer, ship, amount):
        self.customer = customer
        self.ship = ship
        self.amount = amount


class Ship:
    def __init__(self, ship_id, name):
        self.ship_id = ship_id
        self.name = name
        self.bookings = []

    def add_booking(self, booking):
        self.bookings.append(booking)

    def get_total_amount(self):
        return sum(b.amount for b in self.bookings)


class CruiseShip(Ship):
    pass


class CargoShip(Ship):
    pass


class MarineCompany:
    def __init__(self, name):
        self.name = name
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)



class BookingController:
    def __init__(self, company):
        self.company = company

    def get_total_amount_collected(self):
        total = 0
        for ship in self.company.ships:
            total += ship.get_total_amount()
        return total

    def get_amount_per_ship(self):
        result = {}
        for ship in self.company.ships:
            result[ship.name] = ship.get_total_amount()
        return result

    def get_customers_for_cruise_ship(self, cruise_ship_name):
        customers = []
        for ship in self.company.ships:
            if isinstance(ship, CruiseShip) and ship.name == cruise_ship_name:
                for booking in ship.bookings:
                    customers.append(booking.customer)
        return customers

# Create company
company = MarineCompany("Oceanic Marine")

# Create ships
cruise1 = CruiseShip(1, "Blue Pearl")
cargo1 = CargoShip(2, "Cargo King")

company.add_ship(cruise1)
company.add_ship(cargo1)

# Create customers
c1 = Customer(101, "Ananya")
c2 = Customer(102, "ABC")
c3 = Customer(103, "XYZ")

# Create bookings
b1 = Booking(c1, cruise1, 5000)
b2 = Booking(c2, cruise1, 6000)
b3 = Booking(c3, cargo1, 8000)

cruise1.add_booking(b1)
cruise1.add_booking(b2)
cargo1.add_booking(b3)

# Controller
controller = BookingController(company)

# Outputs
print("Total amount collected:", controller.get_total_amount_collected())
print("Amount per ship:", controller.get_amount_per_ship())

print("Customers for cruise ship 'Blue Pearl':")
for customer in controller.get_customers_for_cruise_ship("Blue Pearl"):
    print(customer)

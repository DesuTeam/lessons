from Library import Customer


class CustomerStore:
    def __init__(self):
        self.customers = []

    def count(self) -> int:
        return len(self.customers)

    def add(self, customer: Customer):
        self.customers.append(customer)
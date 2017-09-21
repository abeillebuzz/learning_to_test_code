class Employee():
    """Collect employee data and give info about salary."""
    
    def __init__(self, first_name, last_name, salary):
        """Store employee info."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def give_raise(self, increase=5000):
        """Add raise to annual salary."""
        salary += increase
        return salary


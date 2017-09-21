import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""
    
    def setUp(self):
        """
        Create an employee and salary for use in all test methods.
        """
        first_name = 'tiffany'
        last_name = 'gay'
        salary = 51000
        self.sample_employee = Employee(first_name, last_name, salary)
        
    def test_give_default_raise(self):
        """Test that give_raise method works with default raise value."""
        self.sample_employee.give_raise()
        
        self.assertEqual(56000, self.sample_employee.salary)
        
    def test_give_custom_raise(self):
        """Test that give_raise method works with custom raise value."""
        self.sample_employee.give_raise(7000)
        
        self.assertEqual(58000, self.sample_employee.salary)

unittest.main()

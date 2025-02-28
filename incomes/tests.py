from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from incomes.models import Incomes

User = get_user_model()

class IncomeTestCase(TestCase):
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass")

        self.income1 = Incomes.objects.create(
            user=self.user,
            source="Freelance",
            amount=1500.00,
            frequency="monthly",
            description="Freelance work payment",
        )

        self.income2 = Incomes.objects.create(
            user=self.user,
            source="Salary",
            amount=2500.00,
            frequency="monthly",
            description="Monthly salary",
        )

    # Model Tests
    def test_income_creation(self):
        """Test if an income record is created properly"""
        self.assertEqual(self.income1.source, "Freelance")
        self.assertEqual(self.income1.amount, 1500.00)
        self.assertEqual(self.income1.user, self.user)

    def test_income_str_method(self):
        """Test the string representation of Incomes"""
        self.assertEqual(str(self.income1), "testuser - Freelance (1500.00)")

    # View Tests
    def test_income_list_view(self):
        """Test API response for listing incomes"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.get("/api/incomes/")

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertEqual(len(response.json()), 2)

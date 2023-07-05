from django.test import TestCase, Client
from django.urls import reverse
from pastries.models import Cake, CakeType, Taste, Filling, Topping  # Импортируйте необходимые модели


class TestPastriesView(TestCase):
    def setUp(self):
        self.client = Client()

        # Создаем тестовые данные для использования в тестах
        self.test_cake_type = CakeType.objects.create(name="Test Cake Type")
        self.test_taste = Taste.objects.create(name="Test Taste")
        self.test_filling = Filling.objects.create(name="Test Filling")
        self.test_topping = Topping.objects.create(name="Test Topping")

        self.test_cake = Cake.objects.create(
            cake_type=self.test_cake_type,
            taste=self.test_taste,
            weight=1,
            price=100,
            available=True
        )
        self.test_cake.fillings.add(self.test_filling)
        self.test_cake.toppings.add(self.test_topping)

    def test_pastries_view_returns_200(self):
        response = self.client.get(
            reverse('pastries'))  # замените 'pastries' на реальное имя URL вашего представления, если это необходимо
        self.assertEqual(response.status_code, 200)

    def test_pastries_view_displays_cakes(self):
        response = self.client.get(
            reverse('pastries'))  # замените 'pastries' на реальное имя URL вашего представления, если это необходимо
        self.assertContains(response, self.test_cake_type.name)
        self.assertContains(response, self.test_taste.name)

    def test_pastries_view_filters_cakes(self):
        response = self.client.get(reverse('pastries'), {
            'q': self.test_cake_type.name})  # замените 'pastries' на реальное имя URL вашего представления, если это необходимо
        self.assertContains(response, self.test_cake_type.name)

    def test_pastries_view_paginates_cakes(self):
        response = self.client.get(reverse('pastries'), {
            'page': 2})  # замените 'pastries' на реальное имя URL вашего представления, если это необходимо
        # В зависимости от того, сколько тортов вы создали в тестовых данных, здесь может понадобиться более сложная логика проверки
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.driver_admin = get_user_model().objects.create_superuser(
            username="admin",
            password="testpassword",
        )
        self.client.force_login(self.driver_admin)
        self.driver = get_user_model().objects.create_user(
            username="driver",
            password="testdriver",
            license_number="QWE12345",
        )

    def test_driver_license_number_listed(self):
        url = reverse("admin:taxi_driver_changelist")
        result = self.client.get(url)
        self.assertContains(result, self.driver.license_number)

    def test_driver_detail_license_number_listed(self):
        url = reverse("admin:taxi_driver_change", args=[self.driver.id])
        result = self.client.get(url)
        self.assertContains(result, self.driver.license_number)

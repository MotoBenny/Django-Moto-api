from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Moto


class MotoTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_moto = Moto.objects.create(
            model="Model",
            brand='KTM',
            year="2020",
            engine_size="125",
            owner=testuser1
        )
        test_moto.save()

    def test_moto_model(self):
        moto = Moto.objects.get(id=1)
        actual_model = str(moto.model)
        actual_brand = str(moto.brand)
        actual_year = str(moto.year)
        actual_owner = str(moto.owner)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_brand, "KTM")
        self.assertEqual(actual_model, "Model")
        self.assertEqual(actual_year, '2020')

    def test_get_moto_list(self):
        url = reverse("moto_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        things = response.data
        self.assertEqual(len(things), 1)
        self.assertEqual(things[0]["model"], "Model")

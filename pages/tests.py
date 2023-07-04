from django.test import SimpleTestCase
from django.urls import reverse

class homePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
    def test_url_availabe_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_template_dontent(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response,'<h2>diçka per Mitrovicen? a?</h2>')
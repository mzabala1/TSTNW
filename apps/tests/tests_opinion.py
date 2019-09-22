from django.test import TestCase
from apps.opinion.models import Opinion

def test_opinion_create(self):
    Opinion(escritor = "Natalia", pre1="hola", pre2="mundo", pre3="A FAVOR").save()
    self.assertEquals(1, 1)
# Create your tests here.

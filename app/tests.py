from django.test import TestCase, RequestFactory
from app.views import HomePageView

from matplotlib.figure import Figure

import numpy as np

class HelloWorldTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_home_page(self):
        request = self.factory.get('/')
        response = HomePageView.as_view()(request)
        self.assertEqual(response.get('content-type'), 'text/html; charset=utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Congratulations')

        """
        Creates a simple sine wave plot
        """

        fig = Figure()
        a = fig.add_subplot(111)
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2*np.pi*t)
        a.plot(t, s)
        fig.savefig('app/static/app/img/plot.svg')

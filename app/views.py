 # app/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.staticfiles import finders
import matplotlib.pyplot as plt
import mpld3

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):

        '''
        fig, ax = plt.subplots()
        plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
        fig_html = mpld3.fig_to_html(fig)
        '''

        html_file_path = finders.find("app/img/Carolyn3.html")
        searched_locations = finders.searched_locations
        f = open(html_file_path, "r")
        fig_html = f.read()
        print(fig_html)
        return render(request, 
                      'index.html',
                        {
                            'title' : "Family Viewer About",
                            'content' : fig_html
                        })

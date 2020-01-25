from django.shortcuts import render
from django.contrib import messages
from airtable import Airtable
import os

AIRTABLE_MOVIESTABLE_BASE_ID='appnmJlwnGQvu1iLY'
AIRTABLE_API_KEY='key2fEpOGmPi9WJki'


# Create your views here.
AT = Airtable(os.environ.get('AIRTABLE_MOVIESTABLE_BASE_ID', AIRTABLE_MOVIESTABLE_BASE_ID),
              'Table%201',
              api_key=os.environ.get('AIRTABLE_API_KEY', AIRTABLE_API_KEY),
              )


def home_page(request):
    user_query = str(request.GET.get('query',''))
    search_result = AT.get_all(formula="FIND('" + user_query.lower() + "', LOWER({Name}))")
    start_for_frontend ={'search_result':search_result}
    return  render(request, 'movies/movies_stuff.html', start_for_frontend)

import requests
from datetime import datetime, date, timedelta
from pprint import pprint


class Services:
    URL_BASE = "https://api.themoviedb.org/3/"
    KEY = "api_key=e4c6a6f5fbd60b0316b7ff30e73bec74"
    SEARCH = 'search/tv?'
    DISCOVER = 'discover/tv?'
    FIND = 'find/tv?'

    def __init__(self):
        pass


    def search_series_names(self, query):
        """
        Function that searches the Series by name and returns all the Series names that include the string in input
        """
        url_final = Services.URL_BASE + Services.SEARCH + Services.KEY + '&query=' + query
        req = requests.get(url_final)
        result = []
        for item in req.json()['results']:
            result.append(item['name'])
        return result


    def researchPerson(self, Person):
        """
        Returns XXX to check
        """
        url_search_person = Services.URL_BASE + '/search/person?api_key=' + Services.KEY + '>>&language=en-US&query=' + Person + '&include_adult=false'


    def discover_best_series(self):
        """
        Function that gives the user the 20 most popular series (there are 20 series displayed by page)
        """
        url_final = Services.URL_BASE + Services.DISCOVER + Services.KEY + '&sort_by=popularity.desc&page=1&include_null_first_air_dates=false'
        req = requests.get(url_final)
        result = []
        for item in req.json()['results']:
            result.append(item['name'])
        print("The {} most popular series are: ".format(len(result)))
        print(result)





    def effacerFavori(self, user):
        """TODO : fonction qui efface les favori d'un user"""


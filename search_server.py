import requests
import json


'''
Basic server-side search maker.

ZPXD, Łukasz Pintal.
'''


places = {
    'google' : 'https://www.google.com/search?q=google.com+{}&start={}',
    '' : '',
}

class Search():

    def __init__(self):
        self.search_n_results = 100 # recode it later
        self.search_n_pages = self.search_n_results / 10

    def first_launch(self): # setup
        sth = None
        if not sth:
            pass
        pass

    def pre_search(self):
        pass

    def get_any_search_identifyier():
        pass

    def clean_search_phrase(self, search_phrase):
        pass

    def searches(self, search_phrases, search_config=None):
        search_results = {}
        for search_phrase in search_phrases:
            search_results['search_phrase'] = search(search_phrase, search_config=None)
        return search_results

    def search(self, search_phrase, search_config=None):
        search_depth = 10
        search_phrase = search_phrase.replace(' ', '+')
        search_results = {}    
        if not search_config:
            for place in places.keys():
                for page in range(self.search_n_pages):
                    if page == 0: page = None
                    results = requests.get(places[place].format(search_phrase, str(page*10)))
                    search_results[place].append(results)
        else:
            pass
        return search_results

    def save_search_results(search_results):        
        json.dumps(search_results)

    def send_search_results():
        pass

    def post_search(self, ):
        pass

    def search_it(self, what):
        self.first_launch()
        self.pre_search()
        search_results = self.searches(what)
        self.save_search_results(search_results)
        self.post_search()

    def decider(self, ):
        pass

if __name__ == "__main__":
    S = Search()
    if '-s' in sys.argv:
        what = sys.argv[sys.argv.find('-s')+1]
        S.search_it(what)
    elif '-l' in sys.argv:
        what = sys.argv[sys.argv.find('-l')+1]
        what = open(what).readlines()
    else
        what = input('What?')
    S.search_it(what)

search(search_phrase, search_config=None)

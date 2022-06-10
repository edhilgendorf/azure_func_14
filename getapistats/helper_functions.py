from array import array
import requests
import logging

class URLHelper:
    def __init__(self, request_object):
        self.request_object = request_object
        self.item_dict = {}

    def get_urls_from_request(self):
        urls = []
        for url in self.request_object.get_json():
            urls.append(url)
        return urls

class GetURLData:
    def __init__(self, url):
        self.url = url
        self.num_of_items = 0
        self.full_dict = {}
        self.first_item = {}
        self.get_data_from_url()
        print("test")

    def get_data_from_url(self):
        try:
            r = requests.get(self.url)
            self.status_code = r.status_code
            if self.status_code == 200:
                json_data = r.json()
                self.full_dict = json_data        
                self.num_of_items = len(json_data)
                self.first_item_name = json_data[0]["item_name"]            
                self.last_item_name = json_data[-1]["item_name"]            
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            self.status_code = "Failed to Connect"

class TestURLS:
    def __init__(self, urls):
        self.urls = urls
        self.build_test_data()

    def build_test_data(self):
        url_items = []
        for url in self.urls:
            thing = GetURLData(url)
            if thing.status_code == 200:
                url_items.append({ 
                    url : 
                        { 
                            "status" : thing.status_code,
                            "number_of_items" : thing.num_of_items, 
                            "first_item" : str(thing.first_item_name),
                            "last_item" : str(thing.last_item_name),

                        } 
                })
            else:
                url_items.append({ 
                    url : 
                        { 
                            "status" : thing.status_code,
                        }
                })
        self.test_data = url_items

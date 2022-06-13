import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse('''[  
        {
            "item_name" : "test_one_name", 
            "item_info" : "some random info", 
            "item_number" : "1",
            something:something,
        },
        {
            "item_name": "test_two_name",
            "item_info" : "some other random info", 
            "item_number" : "2"
        },
        {
            "item_name": "test_three_name",
            "item_info" : "third random info", 
            "item_number" : "3"
        }
    ] 
    ''')


    #return func.HttpResponse('{ "test_list": ["item_one", "item_two"] }')
import logging
import json
from . import helper_functions
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        reqo = helper_functions.URLHelper(req)
        urls = reqo.get_urls_from_request()
        get_test_data = helper_functions.TestURLS(urls)
    except Exception as e:
        logging.debug(e)
        return func.HttpResponse("Error, see logs!" + repr(e), status_code=200)
    return func.HttpResponse(str(get_test_data.test_data), status_code=200)

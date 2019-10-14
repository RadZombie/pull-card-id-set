import json
import requests
import setListPull

request_url = str(setListPull.request_url)

def data_page_pull(url):
    response_json = requests.get(url)
    response = json.loads(response_json.text)
    page_number = 1
    full_response = []
    more_pages = response["next_page"]
    if response["has_more"] == True:
        print("Request is multiple pages.")
    else:
        print("Request is a single page.")
    while response["has_more"] == True:
        #print("Page " + str(page_number) + " going through while loop.")
        response_json = requests.get(url)
        response = json.loads(response_json.text)
        full_response.append(response)
        url = response["next_page"]
        print("Page " + str(page_number) + " done.")
        page_number = page_number + 1
        response_json = requests.get(url)
        response = json.loads(response_json.text)
    else:
        #print("hitting up else from that while loop with " + url)
        response_json = requests.get(url)
        response = json.loads(response_json.text)
        print("Page " + str(page_number) + " done.")
        full_response.append(response)
    print("All pages pulled.")
    return full_response


collated_pages = data_page_pull(request_url)

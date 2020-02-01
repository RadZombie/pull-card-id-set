import json
import requests
#need to figure this one out another time in case set data extends past a single page
#import pagifySetData

##get refreshed list of set codes and set names
#pull data from scryfall
response = requests.get("https://api.scryfall.com/sets")
cards_data_page = json.loads(response.text)

#isolate the set data from response
set_data = cards_data_page["data"]

#initialize set_code list and populate
set_codes = []
for set in set_data:
    set_codes.append(set.get("code"))

##initialize set_name list and populate
set_names = []
for set in set_data:
    set_names.append(set.get("name"))

set_dictionary = {}
set_dictionary = dict(zip(set_names, set_codes))

#print(set_dictionary.get("Ravnica Allegiance"))

#with open("set_dictionary.json", 'w') as outfile:
#    json.dump(set_dictionary, outfile)

#exit()

#combine set_codes and set_lists into one list
set_names_and_codes = []
set_names_and_codes.extend(set_codes)
set_names_and_codes.extend(set_names)

###requested_set_code = input(
###    "Provide the set code or name that you want to query: ")

validated_set_code = None

while validated_set_code == None:
    requested_set = input(
        "Provide the set code or name that you want to query: ")
    if set_names_and_codes.count(requested_set) > 0:
        print(requested_set + " is a valid set.")
        if set_codes.count(requested_set) == 0:
            validated_set_code = set_dictionary.get(requested_set)
        else:
            validated_set_code = requested_set
    else:
        print(
            requested_set +
            " is not a valid set input, please provide a set code or name from the following list:"
        )
        #request_for_code_list = None
        #
        #        request_for_code_list = input(
        #        "Would you like to see a list of valid set codes and names? (Y/N)")
        #            if requested_for_code_list = "Y"
        #                print(set_names_and_codes)
        #            else
        print(*set_names_and_codes, sep="\n")
#used for debug/testing
#with open("set_date.json", 'w') as outfile:
#    json.dump(cards_data_page, outfile)

#request set code from user

#pull set codes and names and put them into list

#ensure requested set is a valid set code.
#if requested_set_code in :
#    requested_set_valid = true

request_url = ("https://api.scryfall.com/cards/search?order=cmc&q=set%3A" +
               validated_set_code)

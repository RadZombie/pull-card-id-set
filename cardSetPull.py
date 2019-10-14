import json
import requests
import setListPull
import pagify
import csv

#collect the de-paginated data from pagify
collated_pages = pagify.collated_pages

#initialize list for each card entry
card_lists = []

#initiliaze list for card ids
scryfall_ids = []

#pull the value for key "data" and add them to the card_lists list
for page in collated_pages:
    card_data = page["data"]
    card_lists.extend(card_data)

#pull the value for key "data" and add them to the card_lists list
for card in card_lists:
    scryfall_ids.append(card.get("id"))

#print(collated_pages[1])
#for page in collated_pages:
#    card_data = page["data"]

#    for key in collated_pages[page]:
#        if key = "data":
#            card_lists.extend()
#    card_lists.append(collated_pages[page]["data"])

print(len(scryfall_ids))

print(*scryfall_ids, sep="\n")

f = open(setListPull.valid_set_code + "_output2.csv", 'w')
print(*scryfall_ids, sep="\n", file=f)  # Python 3.x


exit()

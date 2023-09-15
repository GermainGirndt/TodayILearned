

import requests


locales = ["en_US",
"en_GB",
"en_CA",
"en_AU",
"fr_FR",
"fr_CA",
"de_DE",
"es_ES",
"es_MX",
"pt_BR",
"pt_PT",
"zh_CN",
"zh_TW",
"ja_JP",
"ko_KR",
"ru_RU"]

def get_movie_details(title, locale):
    base_url = "https://apis.justwatch.com/content/titles/"

    search_url = f"{base_url}{locale}/popular?body={{\"query\":\"{title}\",\"content_types\":[\"movie\"]}}"
    
    # Search for the movie
    search_response = requests.get(search_url)
    search_data = search_response.json()

    # Check if there are results
    if not search_data['items']:
        return f"No results found for '{title}'."
    
    # Get the first matching movie's details
    movie_id = search_data['items'][0]['id']
    details_url = f"{base_url}movie/{movie_id}/locale/{locale}"
    details_response = requests.get(details_url)
    details_data = details_response.json()

    # Retrieve the offering details
    offers = details_data.get('offers')

    #print(details_data)

    # Check if there are results
    if not offers:
        return f"No offers found for '{title}'."

    result = []
    for offer in offers:
        #print(offer)
        platform = offer['monetization_type']
        url_pieces = offer['urls'].get('standard_web').split('/')[1:3]
        url = "".join(url_pieces)


        result.append({ "platform" : platform, "url": url})
    
    return result

# Usage
title = "Baki"

for locale in locales:
    print(f"\n\n{locale}:")
    movie_details = get_movie_details(title, locale)
    print(movie_details)
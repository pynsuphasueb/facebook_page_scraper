#import Facebook_scraper class from facebook_page_scraper
from facebook_page_scraper import Facebook_scraper
import json
#instantiate the Facebook_scraper class

page_name = "kfcth"
posts_count = 1
browser = "firefox"

KFC_scrape = Facebook_scraper(page_name,posts_count,browser)

#call the scrap_to_json() method
json_data = KFC_scrape.scrap_to_json()
print(json_data)

# data = []
# for line in json_data:
#     data.append(json.loads(line))

# print(data)

import requests
import json
import urllib 

def buildPost():
	encoded = urllib.parse.urlencode({'query': 'gucci flames', 'hitsPerPage':'100', 'page':'0'}, safe='/', quote_via=urllib.parse.quote)
	filters = ['(strata%3A\'grailed\'', 'strata%3A\'hype\'', 'strata%3A\'basic\')']
	marketplaces = ['grailed','heroine']
	queryParameters = {'x-algolia-agent': 'Algolia for vanilla JavaScript 3.21.1', 'x-algolia-application-id': 'MNRWEFSS2Q', 'x-algolia-api-key':'a3a4de2e05d9e9b463911705fb6323ad'}
	filtersConcat = "%20OR%20".join(filters) + '%20AND%20(marketplace%3A' +marketplaces[0]+')'

	payload = {'params':encoded+'&filters='+filtersConcat}
	stringLoad = json.dumps(payload)
	print(json.dumps(payload))

	#each item post has its unique id 
	
	# print(filtersConcat)

	#filters = urllib.parse.urlencode({'filters':'(strata:'grailed')'})
	# print('filters: ' + filters)
	# print(json.dumps(queryParameters))
	headers = {'Content-Type':'application/x-www-form-urlencoded'}
	request = requests.post('https://mnrwefss2q-dsn.algolia.net/1/indexes/Listing_by_date_added_production/query', params=queryParameters, headers=headers,data=stringLoad)
	print(request.text)
	print(request.url)
def main():
	# response = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=10')
	# jsonObj = response.json()
	# print(jsonObj[0]['id'])
	# print(response.text)
	# print('done')
	buildPost()
if __name__ == "__main__":
	main()
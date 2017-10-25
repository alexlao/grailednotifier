import requests
import json
import urllib 

def postSearch(requestedItem):
	encoded = urllib.parse.urlencode({'query': requestedItem, 'hitsPerPage':'100', 'page':'0'}, safe='/', quote_via=urllib.parse.quote)
	filters = ['(strata%3A\'grailed\'', 'strata%3A\'hype\'', 'strata%3A\'basic\')']
	marketplaces = ['grailed','heroine']
	queryParameters = {'x-algolia-agent': 'Algolia for vanilla JavaScript 3.21.1', 'x-algolia-application-id': 'MNRWEFSS2Q', 'x-algolia-api-key':'a3a4de2e05d9e9b463911705fb6323ad'}
	filtersConcat = "%20OR%20".join(filters) + '%20AND%20(marketplace%3A' +marketplaces[0]+')'

	payload = {'params':encoded+'&filters='+filtersConcat}
	stringLoad = json.dumps(payload)
	# print(json.dumps(payload))

	#each item post has its unique id 
	headers = {'Content-Type':'application/x-www-form-urlencoded'}
	request = requests.post('https://mnrwefss2q-dsn.algolia.net/1/indexes/Listing_by_date_added_production/query', params=queryParameters, headers=headers,data=stringLoad)
	#print(request.text)
	responseDict = json.loads(request.text)
	return responseDict

def main():
	searchItem = 'gucci flames'
	results = postSearch(searchItem)
	for arr in results['hits']:
		print(arr['id'])
	print(len(results['hits']))
if __name__ == "__main__":
	main()

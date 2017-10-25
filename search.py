import requests
import json
import urllib 

def postSearch(requestedItem):
	encoded = urllib.parse.urlencode({'query': requestedItem.get('name'), 'hitsPerPage':'100', 'page':'0'}, safe='/', quote_via=urllib.parse.quote)
	filters2 = '('
	if requestedItem.get('marketType') == None:
		# apply all filters
		print('none')
	else:
		# apply specified filters
		marketSize = len(requestedItem.get('marketType'))
		marketTypes = requestedItem.get('marketType')
		for x in range(marketSize-1):
			#do this
			filters2 = filters2 + 'strata%3A'+'\''+ marketTypes[x] + '\'%20OR%20'
		filters2 = filters2 + 'strata%3A' + '\''+marketTypes[marketSize-1] + '\')'
		print(filters2)
		print('############################################################')
	marketplaces = ['grailed','heroine']
	queryParameters = {'x-algolia-agent': 'Algolia for vanilla JavaScript 3.21.1', 'x-algolia-application-id': 'MNRWEFSS2Q', 'x-algolia-api-key':'a3a4de2e05d9e9b463911705fb6323ad'}
	filtersConcat = filters2 + '%20AND%20(marketplace%3A' +marketplaces[0]+')' #sizes, tops/pieces filters are appended
	#filters format: (types of grailed) AND (marketplace) AND (itemfilters)
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
	#dictionary with name, filters, etc
	searchItem = {'name': 'gucci flames', 'marketType':['grailed','basic','hype'], 'itemType':['category_path_size:\'footwear.lowtop_sneakers.10\'']}
	# print(searchItem.get('itemType')[0])
	# searchItem = 'gucci flames'
	results = postSearch(searchItem)
	for arr in results['hits']:
		print(arr['id'])
	print(len(results['hits']))
if __name__ == "__main__":
	main()

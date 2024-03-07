import requests, json


bold_start = '\033[1m'
bold_end = '\033[0m'

vendor = input('What is the vendor that you are looking for? ')

def breached_hackernews():
    for page in range(0,40):
        api = f'http://hn.algolia.com/api/v1/search?query="{vendor}""breached"&tags=story&page={page}&numericFilters=created_at_i>1577923200'
        res = requests.get(api)
        if res.status_code == 200:
            res_data = res.json()
            for results in res_data['hits']:
                if ("HN" or "Please") in results['title']:
                    continue
                elif results['url'] is None:
                    print(f"{results['points']} points - {results['title']}")
                elif results['points'] > 500:
                    print(f"{bold_start}{results['points']} points - {results['title']}:{bold_end} {results['url']}")
                else:
                    print(f"{results['points']} points - {results['title']}: {results['url']}")

breached_hackernews()
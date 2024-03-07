import requests, sys
from bs4 import BeautifulSoup
from urllib.parse import urljoin



visited_urls = set()

def urlSpider(url, keyword):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'html.parser')
            a_tag = soup.find_all('a')
            urls = []
            for tag in a_tag:
                href = tag.get('href')
                if href is not None and href != '':
                    urls.append(href)
            #print(set(urls))
        else:
            print(f'{resp.status_code} - {url}')

        for urls2 in urls:
            #print(urls2)
            if urls2 not in visited_urls:
                visited_urls.add(urls2)
                #print(visited_urls)
                #url_join = url.join(urls2.strip('/'))
                url_join = urljoin(url, urls2)
                if keyword in url_join:
                    with open('./found_urls.txt', 'a') as f:
                        f.writelines(url_join + '\n')
                        #print(url_join)
            else:
                pass
    except KeyboardInterrupt:
        sys.exit()

def filter_urls(url):
    pass
    
fqdn = input('FQDN for scaping: ')
domain_kw = input('Scaping keyword: ')
urlSpider(fqdn, domain_kw)


import requests, sys, json

bold_start = '\033[1m'
bold_end = '\033[0m'

def check_vendor_breach(vendor):
    api = f'https://haveibeenpwned.com/api/v3/breach/{vendor}'
    res = requests.get(api)
    if res.status_code == 200:
        res_data = res.json()
        data = {
            "Title": res_data['Title'], 
            "Domain": res_data['Domain'], 
            "BreachDate": res_data['BreachDate'], 
            "BreachData": res_data['DataClasses'], 
            "isVerified": res_data['IsVerified'], 
            "isSensitive": res_data['IsSensitive']
        }
        #print(json.dumps(data, indent=2))
        print(f'\n> The vendor "{bold_start}{vendor}{bold_end}" has a breached on {bold_start}{data["BreachDate"]}{bold_end}')
    else:
        print(f'\n> The vendor "{bold_start}{vendor}{bold_end}" does not have any data breaches recently.')


def check_cves_nvd(vendor):
    api = f'https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={vendor}'
    res = requests.get(api)
    res_data = res.json()
    if res.status_code == 200 and res_data['totalResults'] > 0:
        print(f'\n> The vendor "{bold_start}{vendor}{bold_end}" had {res_data["totalResults"]} CVE(s). Those are: ')
        for index, cve in enumerate(res_data['vulnerabilities']):
            CVE_ID = cve['cve']['id']
            CVE_Desc = cve['cve']['descriptions'][0]['value']
            CVE_Metrics = cve['cve']['metrics']
            CVE_Ref = cve['cve']['references']
            data = {
                'CVE': CVE_ID,
                'Descriptions': CVE_Desc,
                'Metrics': CVE_Metrics,
                'Reference': CVE_Ref
            }
            print(f'\n\t{CVE_ID} - {CVE_Desc}')
            for index, poc in enumerate(CVE_Ref):
                try:
                    if 'Exploit' in poc['tags']:
                        print(f"\t>> {bold_start}POC{bold_end}: {poc['url']}")
                except KeyError as err:
                    continue
    else:
        print(f'\n> The vendor "{bold_start}{vendor}{bold_end}" does not have any CVE.')

def scanSummary(vendor):
    summary_banner = f'| Summary about "{vendor}" breach & CVE(s) |'
    print('*' * len(summary_banner))
    print(f'{bold_start}{summary_banner}{bold_end}')
    print('*' * len(summary_banner))
    check_vendor_breach(vendor)
    check_cves_nvd(vendor)

if __name__ == '__main__':
    scanSummary(sys.argv[1])
    
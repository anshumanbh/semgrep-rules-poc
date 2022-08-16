import sys
import requests
import os

defect_dojo_token = os.getenv('DEFECT_DOJO_TOKEN')
defect_dojo_domain = os.getenv('DEFECT_DOJO_DOMAIN')
defect_dojo_engagement_value = os.getenv('DEFECT_DOJO_ENGAGEMENT_VALUE')
defect_dojo_scan_type = os.getenv('DEFECT_DOJO_SCAN_TYPE')

url = "https://{}/api/v2/import-scan/".format(defect_dojo_domain)
headers = {"Authorization": "Token {}".format(defect_dojo_token)}

files = {'file': open(sys.argv[1], 'rb').read()}

values = {
  'engagement' : defect_dojo_engagement_value,
  'scan_type': defect_dojo_scan_type
  }

try:
  r = requests.post(url, headers=headers, files=files, data=values, verify=True)
  r.raise_for_status()
  if (r.status_code == 201):
    print("Scan Import was successful\n")
    print(r.json())
  else:
    print("Something went wrong..")
except requests.exceptions.RequestException as e:  # This is the correct syntax
    raise SystemExit(e)

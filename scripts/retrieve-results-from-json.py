import json
import sys
f = open(sys.argv[1])
data = json.load(f)
with open(sys.argv[2], 'w') as r:
  if data['results']:
    for i in data['results']:
      r.write('\n')
      r.write('====================================')
      r.write('\n')
      r.write("Check ID: {}".format(i['check_id']))
      r.write('\n')
      r.write("Lines: {}".format(i['extra']['lines']))
      r.write('\n')
      r.write("Message: {}".format(i['extra']['message']))
      r.write('\n')
      r.write("Path: {}".format(i['path']))
      r.write('\n')
      r.write("Start Line: {}".format(i['start']['line']))
      r.write('\n')
      r.write('\n')
r.close()
r.close()

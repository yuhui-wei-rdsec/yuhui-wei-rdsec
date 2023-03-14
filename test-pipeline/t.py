tt = 160000/60/60
print(tt)

import json
data = {
    'name' : 'myname',
    'age' : 100,
}
json_str = json.dumps(data)
print(json_str)

MailBody='Dear user, \n\nWelcome to ChinaSDZ, please refer to user guide to config your environment. \nUser guide link: https://wiki.jarvis.trendmicro.com/display/RDSEC/China+SDZ+User+Guideline \n\nFirst time, you must change your password.\nYour AAD Account credential is:\nUser name: {0}\nPassword: {1} \n\nBest Regards,\nCDC RDSec infra team'
# print(MailBody)

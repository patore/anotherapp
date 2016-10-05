""" any partner we want can connect with our api keyfor 2 hours.  
10 unsuccessful attempts and we get locked out."""


import configs
import requests as req
import xmltodict as xmtd

headers = {'Content-Type': 'application/xml',
                   'Finicity-App-Key': configs['fincity-app-key'],
                   'Finicity-App-Token': configs['fincity-app-token']}
    
def get_2hr_token(self):
    url = "{}/v2/partners/authentication".format(configs[fincity_url])
    xml = """<credentials> <partnerId>{}</partnerId> 
    <partnerSecret>{}</partnerSecret> 
    </credentials>""".format(configs[fincity_partner_id], fincity_partner_secret)
    r = req.post(url, data=xml, headers=headers)
    if r.status_code == 200:
        data = xmtd.parse(r.text)
        return data['access']['token']
    else:
        raise ValueError('bad return status: {}'.format(r.status_code))
    


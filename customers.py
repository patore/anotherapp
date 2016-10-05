# application headers must be xml
# must include fincity-app-key
# fincity-app-Token
# in the <body>
#    - include <customer>
#                  <username>MYUSERNAME</username>
#    -             <firstName>FirstNameHere</firstName>
#    -             <lastName>lastNameHere</lastName>
#               </customer>

# success is when you get a http 201
# an XML record is returned with the customer and ID with the createddate
# sample record
#  <customer>
#  <id>41442</id>
#  <createdDate>1412792539</createdDate>
# </customer>
import xml2dict as xmtd
import requests as req
from configs import config

class customer():
    """ a fake customer has fake bank accounts
    a actual customer has actual accounts and we know about them (they don't want anonymity) so 
    because of this we will actually make a customer record that we will get billed for"""

    self.headers = {'Content-Type': 'application/xml',
                   'Finicity-App-Key': config['fincity_app_key'],
                   'Finicity-App-Token': config['fincity_app_token']}


    @classmethod
    def get_customers(self, search='*', start=1, limit=25, type=configs['type']):
        """returns all your current customers"""
        url = '{}/v1/customers'.format(config['finicity_url'])
        data = {start:start,
                search:search,
                limit:limit,
                type:type
                }
        r = req.get(url, data=data)
        if r.status_code == 200:
            return xmtd.parse(r.data)
        

    
    @classmethod
    def create_fake(self, username, first_name, last_name):
        url = '{}/v1/customers/testing'.format(fincity_url)
        self.create_new(username, first_name, last_name, url) 

    @classmethod
    def delete_customer(self):
        """Completely remove a customer from the system. This will remove the customer and all associated accounts, transactions, and aggregation support tickets.
        USE THIS SERVICE CAREFULLY! It will perform the operation immediately, without pausing for confirmation!
        Success: HTTP 204 (No Content)
        """
        url = '{}/v1/customers/{}'.format(config[fincity_url], customerId)
        req.delete(url, headers=self.headers)
    
    @classmethod
    @property
    def customer(self, customerID, username, first_name, last_name):
        """from the customer ID give the xml which changes the username first_name or last_name"""
        url = '{}/v1/customers/{}'.format(config[fincity_url], customerID)
        xml = """<body><customer>
        <username>{}</username>
        <firstName>{}</firstName>
        <lastName>{}</lastName>
        </customer>
        </body>""".format(username, first_name, last_name)
        r = req.post(url, headers=self.headers)
        if r.status_code == 204:
            return
        else:
            raise ValueError('modification went wrong: {}'.format(r.status_code))

    @classmethod
    @propery.setter()
    def customer(self, username, first_name, last_name, customerID=None, url=None):
        """careful with this call, we get charged per account
        if customerID is set this is a modification
        if not then the customer is created"""
        if not customerID:  # create the acct
            if not url:  # put in for fake accts
                url = '{}/v1/customers/active'.format(config[fincity_url])
            else:
                url = '{}/v1/customers/'
        else:
            url = "{}/v1/customers/{}/accounts/{}".format(customerID, accountID)
        xml = """<body><customer>
        <username>{}</username>
        <firstName>{}</firstName>
        <lastName>{}</lastName>
        </customer>
        </body>""".format(username, first_name, last_name)
        
        r = req.post(url, headers=self.headers, data=xml)
        if r.status_code == 201:
            return  # get the customer ID and createdDate
        else:
            raise ValueError('something went wrong in creating a new customer: {}'.format(r.status_code))

        
    @classmethod
    def get_customer_acct(self, customerID, acctID):
        """ this is a customer account number at an institution not the customer themselves"""
        
        url = "{}/v1/customers/{}/accounts/{}".format(url, customerID, accountID)
        r = req.get(url, headers=self.headers)
        if r.status_code == 200:
            return xmtd.parse(r.data)
        else:
            raise ValueError('get_customer_acct returned {}: {}'.format(r.status_code, r.data))
    
    @classmethod
    def get_customer_accts(self, customerID):
        """return all accounts a customer has"""
        
        url = "{}/v1/customers/{}/accounts".format(url, customerID)
        r = req.get(url, headers=self.headers)
        if r.status_code == 200:
            return xmtd.parse(r.data)
        else:
            raise ValueError('get_customer_acct returned {}: {}'.format(r.status_code, r.data))
    
    @classmethod
    @property.setter()
    def customers_acct_creds(self, customerID, accountID):
        url = "{}/v1/customers/{}/accounts/{}/loginForm".format(url, customerId, accountID)
# todo: needs a for loop
        xml = """<loginForm>
  <loginField>
    <id>FIELD_ID_1</id>
    <value>VALUE_1</value>
  </loginField>
  <loginField>
    <id>FIELD_ID_2</id>
    <value>VALUE_2</value>
  </loginField>
</loginForm>""".format(username, first_name, last_name)

        r = req.put(url, data=data, headers=self.headers)
        if r.status_code == 204:
            return
        else:
            raise ValueError('returned {}: {}'.format(r.status_code))
        

    @classmethod
    @property
    def customers_acct_creds(self, customerID, accountID):
        """r.data = <loginForm>
          <loginField>
            <id>101732001</id>
            <name>Banking Userid</name>
            <value>USERNAME</value>
            <mask>false</mask>
            <displayOrder>1</displayOrder>
          </loginField>
          <loginField>
            <id>101732002</id>
            <name>Banking Password</name>
            <value></value>
            <mask>true</mask>
            <displayOrder>2</displayOrder>
          </loginField>
        </loginForm>
        """
        
        url = "{}/v1/customers/{}/accounts/{}/loginForm".format(url, customerId, accountId)
        r = req.get(url, headers=self.headers)
        if r.status_code == 200:
            return xmtd.parse(r.data)
        else:
            raise ValueError('r.status_code returned: {}'.format(r.status_code))
        




    

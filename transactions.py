class transactions():
    def get_customer_transactions(self, customerID, start_date, end_date, index = None, count = None, sort = "asc"): #dates are timestamps
        url = "{}/v2/customers/{}/transactions?fromDate=[{}]&toDate=[{}]&start=[{}]&limit=[{}]&sort={}".format(
                                url, customerID, start_date, end_date, index,  count, sort)
        
        req.get(url, data=data)
        
        
        
        
        
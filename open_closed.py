#illustration of the problem
class CloudService:
    def __init__(self, client):
        pass

    def authenticate(self, client):
        if client == 'aws':
            pass
            #some code to authenticate against aws
        elif client == 'azure':
            pass
            #some code to authenticate against azure
    
    def deploy(self, client):
        if client == 'aws':
            pass
            #some code to deploy to aws
        elif client == 'azure':
            pass
            #some code deploy to azure
        
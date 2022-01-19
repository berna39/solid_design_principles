#illustration of the problem
class CloudService:
    def __init__(self, client):
        self.client = client

    def authenticate(self):
        if self.client == 'aws':
            print('auth to aws')
            #some code to authenticate against aws
        elif self.client == 'azure':
             print('auth to azure')
            #some code to authenticate against azure
    
    def deploy(self):
        if self.client == 'aws':
             print('deploy to aws')
            #some code to deploy to aws
        elif self.client == 'azure':
             print('deploy to azure')
            #some code deploy to azure

service = CloudService('aws') #example of deploying 
service.deploy()
        
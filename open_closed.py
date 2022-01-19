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
        
#now let immagine the case when we add the gcp service to our cloud service
#instead of adding on more condition to our class, let refractor the code
# --------------------------------------------------------------------------
from abc import ABC, abstractmethod

class CloudService(ABC):
    def authenticate(self):
        pass

    def deploy(self):
        pass

#aws service
class AWS(CloudService):
    def authenticate(self):
        return 'auth to aws'

    def deploy(self):
        return 'deploy to aws'

aws = AWS()
print(aws.authenticate())

#azure service
class Azure(CloudService):
    def authenticate(self):
        return 'auth to azure'

    def deploy(self):
        return 'deploy to azure'

azure = Azure()
print(azure.authenticate())

#azure service
class GCP(CloudService):
    def authenticate(self):
        return 'auth to gcp'

    def deploy(self):
        return 'deploy to gcp'

gcp = GCP()
print(gcp.authenticate())